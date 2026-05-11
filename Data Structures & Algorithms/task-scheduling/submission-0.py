from collections import deque
from heapq import heappush, heappop
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        minheap = []

        for task, count in counter.items():
            heappush(minheap, -count)
        
        q = deque([])

        time = 0

        while minheap or q:
            time += 1

            if not minheap:
                time = q[0][1]
            else:
                count = 1 + heappop(minheap)

                if count != 0:
                    q.append((count, time + n))
                
            if q and time == q[0][1]:
                c, _ = q.popleft()
                heappush(minheap, c)
        
        return time
