class Twitter:

    def __init__(self):
        self.time = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        self.time -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        feedHeap = []
        followees = self.followMap[userId] | {userId}
        for followee in followees:
            for tweet in self.tweetMap[followee]:
                heapq.heappush(feedHeap, tweet)
        ans = []

        while feedHeap and len(ans) < 10:
            ans.append(heapq.heappop(feedHeap)[1])
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)