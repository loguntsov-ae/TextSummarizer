import asyncio
from redis_client import subscribe_tasks, publish_result
from domain.factory import get_repository

repo = get_repository()  # динамический выбор модели

async def handle_task(message: dict):
    task_id = message["task_id"]
    text = message["text"]
    print(f"⚙️  [worker] Received task {task_id}")

    try:
        summary = await repo.summarize(text)
        await publish_result({"task_id": task_id, "summary": summary, "text": text})
        print(f"✅  [worker] Finished task {task_id}")
    except Exception as e:
        await publish_result({"task_id": task_id, "summary": f"Error: {str(e)}"})
        print(f"❌  [worker] Failed task {task_id}: {e}")

async def main():
    print("👂  Worker started and waiting for tasks...")
    await subscribe_tasks(handle_task)

if __name__ == "__main__":
    asyncio.run(main())