import json
import redis.asyncio as redis
from settings import settings

redis_client = redis.from_url(settings.redis_url, decode_responses=True)

TASK_CHANNEL = "tasks"
RESULT_CHANNEL = "results"


async def subscribe_tasks(callback):
    pubsub = redis_client.pubsub()
    await pubsub.subscribe(TASK_CHANNEL)
    async for message in pubsub.listen():
        if message["type"] == "message":
            await callback(json.loads(message["data"]))


async def publish_result(result_data: dict):
    await redis_client.publish(RESULT_CHANNEL, json.dumps(result_data))