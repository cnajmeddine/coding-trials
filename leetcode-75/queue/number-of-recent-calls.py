from collections import deque

class RecentCounter:
    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)
        
        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()
        
        # Return the count of requests within the 3000 ms window
        return len(self.requests)
