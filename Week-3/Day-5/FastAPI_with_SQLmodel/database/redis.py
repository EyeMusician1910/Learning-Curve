from ..services.config import database_settings

try:
    from redis.asyncio import Redis
    from redis.exceptions import ConnectionError as RedisConnectionError
except ModuleNotFoundError:
    Redis = None
    RedisConnectionError = None


def _get_token_blacklist():
    if Redis is None:
        raise RuntimeError(
            "Redis support is not installed. Install it with: pip install redis"
        )

    return Redis(
        host=database_settings.REDIS_HOST,
        port=database_settings.REDIS_PORT,
        db=0,
    )

async def add_jti_to_blacklist(jti:str):
    token_blacklist = _get_token_blacklist()
    try:
        await token_blacklist.set(jti, "blacklisted")
    except RedisConnectionError as exc:
        raise RuntimeError(
            "Redis is unavailable. Check REDIS_HOST/REDIS_PORT and make sure the Redis server is running."
        ) from exc

async def is_jti_blacklisted(jti:str)-> bool:
    token_blacklist = _get_token_blacklist()
    try:
        return await token_blacklist.exists(jti)
    except RedisConnectionError as exc:
        raise RuntimeError(
            "Redis is unavailable. Check REDIS_HOST/REDIS_PORT and make sure the Redis server is running."
        ) from exc
