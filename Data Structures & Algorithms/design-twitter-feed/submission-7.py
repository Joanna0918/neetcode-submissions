class Twitter:

    def __init__(self):
        self.t = 0
        self.followers = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.t, tweetId])
        self.t += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = [] # time, tweetId
        userList = self.followers[userId] | {userId}

        for uId in userList:
            for t, tweetId in self.tweets[uId]:
                heapq.heappush(minHeap, (t, tweetId))
                while len(minHeap) > 10:
                    heapq.heappop(minHeap)
        
        res = []
        while minHeap:
            res.append(heapq.heappop(minHeap)[1])
        res.reverse()
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        
