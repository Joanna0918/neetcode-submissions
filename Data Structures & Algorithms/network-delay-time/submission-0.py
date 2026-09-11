class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        nodesMap = {i + 1: [] for i in range(n)}
        for u, v, t in times:
            nodesMap[u].append((v, t))

        q = deque([k])
        wait = set()
        complete = set()
        currTime = 0
        while q or wait:
            for waitNode, waitTime, addTime in list(wait):
                if waitNode in complete:
                    wait.remove((waitNode, waitTime, addTime))
                    continue
                if currTime - addTime >= waitTime:
                    q.append(waitNode)
                    wait.remove((waitNode, waitTime, addTime))
            
            if not q:
                currTime += 1
                continue

            for _ in range(len(q)):
                currNode = q.popleft()
                if currNode in complete:
                    continue
                complete.add(currNode)
                if nodesMap[currNode]:
                    for nei, neiT in nodesMap[currNode]:
                        if nei not in complete:
                            wait.add((nei, neiT, currTime))

            if len(complete) == n:
                return currTime

            currTime += 1
        
        return -1