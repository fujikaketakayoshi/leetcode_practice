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
        self.user_tweets[userId].append((self.tweet_pos, tweetId))
        
    def getNewsFeed(self, userId: int) -> list[int]:
        users = self.user_follows[userId]
        feeds = []
        for u in users:
            feeds += self.user_tweets[u]
        feeds.sort(reverse=True)
        ans = []
        for pos, tweetId in feeds[:10]:
            ans.append(tweetId)
        return ans

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