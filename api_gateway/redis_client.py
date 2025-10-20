import json
import redis.asyncio as redis
from settings import settings

redis_client = redis.from_url(settings.redis_url, decode_responses=True)

TASK_CHANNEL = "tasks"
RESULT_CHANNEL = "results"


async def publish_task(task_data: dict):
    await redis_client.publish(TASK_CHANNEL, json.dumps(task_data))


async def subscribe_results(callback):
    pubsub = redis_client.pubsub()
    await pubsub.subscribe(RESULT_CHANNEL)
    async for message in pubsub.listen():
        if message["type"] == "message":
            await callback(json.loads(message["data"]))
