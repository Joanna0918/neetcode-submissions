class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCount = Counter(tasks)
        maxHeap = [] # (cnt, task)
        for task, cnt in taskCount.items():
            heapq.heappush(maxHeap, (-cnt, task))

        waitingQ = [] # (readyTime, cnt, task)
        t = 0
        while maxHeap or waitingQ:
            if not maxHeap:
                t = max(t, waitingQ[0][0])
            
            while waitingQ and waitingQ[0][0] <= t:
                readyTime, cnt, task = heapq.heappop(waitingQ)
                heapq.heappush(maxHeap, (cnt, task))
            
            if maxHeap:
                cnt, task = heapq.heappop(maxHeap)
                cnt += 1
                if cnt < 0:
                    heapq.heappush(waitingQ ,(t + n + 1, cnt, task))
            t += 1
            
        return t
        