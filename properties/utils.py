from django.core.cache import cache
from .models import Property

def get_all_properties():
    """
    Fetch all properties from cache or database.
    Cache the result in Redis for 1 hour (3600 seconds).
    """
    # Try to get cached data
    properties = cache.get('all_properties')
    
    if properties is None:
        # Not in cache, fetch from database
        properties = list(Property.objects.all())
        # Store in cache for 1 hour
        cache.set('all_properties', properties, 3600)
    
    return properties


def get_redis_cache_metrics():
    """
    Retrieves Redis cache metrics (hits, misses, hit ratio).
    Logs metrics and returns them as a dictionary.
    """
    # Get low-level Redis client
    client = cache.client.get_client()

    # Get Redis stats
    info = client.info('stats')
    hits = info.get('keyspace_hits', 0)
    misses = info.get('keyspace_misses', 0)

    total_requests = hits + misses

    # Calculate hit ratio without inline else
    if total_requests > 0:
        hit_ratio = hits / total_requests
    else:
        hit_ratio = 0

    metrics = {
        'keyspace_hits': hits,
        'keyspace_misses': misses,
        'hit_ratio': hit_ratio,
    }

    # Log metrics
    print(f"[Redis Cache Metrics] Hits: {hits}, Misses: {misses}, Hit Ratio: {hit_ratio:.2f}")

    return metrics
