class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        flightMap = defaultdict(list)
        for from_i, to_i in sorted(tickets, reverse=True):
            flightMap[from_i].append(to_i)
        
        self.res = []
        def dfs(from_i):
            while flightMap[from_i]:
                to_i = flightMap[from_i].pop()
                dfs(to_i)

            self.res.append(from_i)

        dfs("JFK")

        return self.res[::-1]