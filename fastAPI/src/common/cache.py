import redis
from config import redis_host, redis_port, redis_db

redis_client = redis.Redis(host=redis_host, port=redis_port, db=redis_db)
