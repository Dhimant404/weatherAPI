import redis.asyncio as redis
import json
from app.config import REDIS_HOST, REDIS_PORT

redisClient = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)


async def getCache(key: str):
    """
    Check if data is cached and if yes, retrieve it.
    """
    cachedValue = await redisClient.get(key)
    if cachedValue:
        return json.loads(cachedValue)
    return None


async def setCache(key: str, value: dict, ttl: int):
    """
    Set cache value.
    """
    await redisClient.set(key, json.dumps(value), ex=ttl)


async def deleteCache(key: str):
    """
    Delete cached value.
    """
    await redisClient.delete(key)
