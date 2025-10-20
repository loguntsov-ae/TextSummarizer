from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from db import SessionLocal, Task
from schemas import TaskResponse, SummarizeRequest
from redis_client import publish_task, subscribe_results
import uuid, asyncio


app = FastAPI(title="Text Summarizer API Gateway")

app.mount("/static", StaticFiles(directory="static"), name="static")

active_connections: set[WebSocket] = set()

# ---------- WebSocket notify ----------
async def notify_all(message: dict):
    for ws in list(active_connections):
        try:
            await ws.send_json(message)
        except Exception:
            active_connections.remove(ws)


# ---------- Redis listener ----------
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


# ---------- API ----------
@app.post("/summarize", response_model=TaskResponse)
async def create_task(request: SummarizeRequest):
    db = SessionLocal()
    task_id = str(uuid.uuid4())
    task = Task(id=task_id, text=request.text)
    db.add(task)
    db.commit()
    db.close()

    await publish_task({"task_id": task_id, "text": request.text})

    # уведомляем всех, что добавлена новая задача
    await notify_all({"task_id": task_id, "status": "queued", "text": request.text})

    return TaskResponse(task_id=task_id, status="queued")


@app.get("/tasks", response_model=list[TaskResponse])
async def list_tasks():
    """Возвращает все задачи из БД."""
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
        # уведомляем всех клиентов, что задача удалена
        await notify_all({"event": "deleted", "task_id": task_id})
        return {"ok": True}
    db.close()
    return {"ok": False, "error": "not_found"}


# ----------- WebSocket -----------
@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    active_connections.add(ws)
    print("🔌 WebSocket connected")
    try:
        while True:
            await ws.receive_text()  # не используем, просто держим соединение
    except WebSocketDisconnect:
        active_connections.remove(ws)
        print("❌ WebSocket disconnected")
