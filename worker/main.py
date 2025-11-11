import asyncio
import logging
from redis_client import subscribe_tasks, publish_result
from domain.factory import get_repository


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

repo = get_repository()


async def handle_task(message: dict):
    task_id = message["task_id"]
    text = message["text"]
    logger.info(f"Worker received task {task_id}")

    try:
        summary = await repo.summarize(text)
        await publish_result({"task_id": task_id, "summary": summary, "text": text})
        logger.info(f"Worker finished task {task_id}")
    except Exception as e:
        await publish_result({"task_id": task_id, "summary": f"Error: {str(e)}"})
        logger.error(f"Worker failed task {task_id}: {e}")


async def main():
    logger.info("Worker started and waiting for tasks...")
    await subscribe_tasks(handle_task)


if __name__ == "__main__":
    asyncio.run(main())