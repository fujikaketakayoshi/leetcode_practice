import heapq
class Twitter:
    def __init__(self):
        MAX = 500
        self.user_follows = [set() for _ in range(MAX + 1)]
        self.user_tweets = [[] for _ in range(MAX + 1)]
        self.tweet_pos = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if not userId in self.user_follows[userId]:
            self.user_follows[userId].add(userId)
        self.tweet_pos += 1
        self.user_tweets[userId].append((tweetId, self.tweet_pos))
        
    def getNewsFeed(self, userId: int) -> list[int]:
        users = self.user_follows[userId]
        hq = []
        for userId in users:
            if self.user_tweets[userId]:
                tId, tPos = self.user_tweets[userId][-1]
                hq.append( (-tPos, tId, userId, len(self.user_tweets[userId]) - 1) )
        heapq.heapify(hq)
        
        feeds = []
        while len(feeds) < 10 and len(hq) > 0:
            # print(hq)
            tPos, tId, userId, idx = heapq.heappop(hq)
            # self.user_tweets[userId].pop()
            feeds.append(tId)
            if idx > 0 and self.user_tweets[userId]:
                tId, tPos = self.user_tweets[userId][idx - 1]
                heapq.heappush(hq, (-tPos, tId, userId, idx - 1))
        return feeds

    def follow(self, followerId: int, followeeId: int) -> None:
        if not followeeId in self.user_follows[followerId]:
            self.user_follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.user_follows[followerId]:
            self.user_follows[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)