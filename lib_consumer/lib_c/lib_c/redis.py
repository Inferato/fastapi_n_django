import redis


class RedisCahche:
    def __init__(self):
        self.redis_instance = redis.StrictRedis(host='redis', port=6379, db=0)
    
    def write(self, key, value):
        self.redis_instance.setex(key, 60, value)
    
    def read(self, key):
        return self.redis_instance.get(key)
        
