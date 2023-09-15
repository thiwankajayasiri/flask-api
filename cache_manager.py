from flask import Flask
from flask_caching import Cache

app = Flask(__name__)
# Configure cache
cache_config = {
    "CACHE_TYPE": "simple",  # can also use "redis", "memcached", etc.
    "CACHE_DEFAULT_TIMEOUT": 300  # Time in seconds
}
cache = Cache(app, config=cache_config)

# Set to store cache keys
cached_keys = set()

def invalidate_cache(key_pattern):
    keys_to_invalidate = [key for key in cached_keys if key.startswith(key_pattern)]
    for key in keys_to_invalidate:
        cache.delete(key)
        cached_keys.remove(key)

# Other route definitions, application logic, etc.
