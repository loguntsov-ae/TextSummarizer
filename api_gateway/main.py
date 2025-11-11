from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from db import SessionLocal, Task
from schemas import TaskResponse, SummarizeRequest
from redis_client import publish_task, subscribe_results
import uuid
import asyncio
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Text Summarizer API Gateway")

app.mount("/static", StaticFiles(directory="static"), name="static")

active_connections: set[WebSocket] = set()


async def notify_all(message: dict):
    for ws in list(active_connections):
        try:
            await ws.send_json(message)
        except Exception:
            active_connections.remove(ws)


async def handle_result(message: dict):
    task_id = message["task_id"]
    summary = message["summary"]
    text = message["text"]

    db = SessionLocal()
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        task.status = "done"
        task.summary = summary
        db.commit()
    db.close()

    await notify_all({
        "event": "updated",
        "task_id": task_id,
        "status": "done",
        "summary": summary,
        "text": text
    })


@app.on_event("startup")
async def startup_event():
    asyncio.create_task(subscribe_results(handle_result))


@app.post("/summarize", response_model=TaskResponse)
async def create_task(request: SummarizeRequest):
    db = SessionLocal()
    task_id = str(uuid.uuid4())
    task = Task(id=task_id, text=request.text)
    db.add(task)
    db.commit()
    db.close()

    await publish_task({"task_id": task_id, "text": request.text})
    await notify_all({"task_id": task_id, "status": "queued", "text": request.text})

    return TaskResponse(task_id=task_id, status="queued")


@app.get("/tasks", response_model=list[TaskResponse])
async def list_tasks():
    """Return all tasks from database."""
    db = SessionLocal()
    tasks = db.query(Task).order_by(Task.created_at.desc()).all()
    db.close()
    return [
        TaskResponse(
            task_id=t.id, status=t.status, summary=t.summary or "", text=t.text
        )
        for t in tasks
    ]


@app.get("/", response_class=HTMLResponse)
async def index():
    with open("static/index.html") as f:
        return HTMLResponse(f.read())


@app.delete("/tasks/{task_id}")
async def delete_task(task_id: str):
    db = SessionLocal()
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
        db.close()
        await notify_all({"event": "deleted", "task_id": task_id})
        return {"ok": True}
    db.close()
    return {"ok": False, "error": "not_found"}


@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    active_connections.add(ws)
    logger.info("WebSocket connected")
    try:
        while True:
            await ws.receive_text()
    except WebSocketDisconnect:
        active_connections.remove(ws)
        logger.info("WebSocket disconnected")
