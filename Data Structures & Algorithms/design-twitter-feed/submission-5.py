class Twitter:

    def __init__(self):
        self.time = 0 # neg time. smaller, more latest
        self.followersMap = defaultdict(set)
        self.tweetsMap = defaultdict(list) # [time, tweetId]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetsMap[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = [] # (time, userId, tweetId, index - 1)

        self.followersMap[userId].add(userId)
        users = list(self.followersMap[userId])
        for u in users:
            if u in self.tweetsMap:
                index = len(self.tweetsMap[u]) - 1
                t, tweetId = self.tweetsMap[u][index]
                heapq.heappush(heap, (t, u, tweetId, index - 1))
        
        while heap and len(res) < 10:
            t, userId, tweetId, index = heapq.heappop(heap)
            res.append(tweetId)

            if index >= 0:
                t, tweetId = self.tweetsMap[userId][index]
                heapq.heappush(heap, (t, userId, tweetId, index - 1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followersMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followersMap[followerId]:
            self.followersMap[followerId].remove(followeeId)
        
