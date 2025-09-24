# rate_limiter.py
import time
from typing import Optional

class RateLimiter:
    def __init__(self, requests_per_minute: int):
        self.requests_per_minute = requests_per_minute
        self.interval = 60.0 / requests_per_minute
        self.last_request_time: Optional[float] = None
    
    def wait_if_needed(self):
        """Wait if needed to respect rate limits"""
        if self.last_request_time is None:
            self.last_request_time = time.time()
            return
        
        current_time = time.time()
        time_since_last = current_time - self.last_request_time
        
        if time_since_last < self.interval:
            sleep_time = self.interval - time_since_last
            time.sleep(sleep_time)
        
        self.last_request_time = time.time()