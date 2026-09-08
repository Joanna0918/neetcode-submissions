class Twitter:

    def __init__(self):
        self.time = 0 # negative int, the smaller, the more recent
        self.tweetMap = defaultdict(list) # userId -> [time, tweetId]
        self.followMap = defaultdict(set) # userId -> set(followeeId)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        if userId in self.tweetMap:
            for t in self.tweetMap[userId]:
                maxHeap.append(t)
        for followee in self.followMap[userId]:
            if followee in self.tweetMap:
                for t in self.tweetMap[followee]:
                    maxHeap.append(t)
        
        heapq.heapify(maxHeap)
        res = []
        while maxHeap and len(res) < 10:
            newTweet = heapq.heappop(maxHeap)
            res.append(newTweet[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
