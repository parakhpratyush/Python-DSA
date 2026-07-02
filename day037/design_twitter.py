import heapq
from collections import defaultdict

class Twitter(object):

    def __init__(self):
        self.timestamp = 0
        # user_id → list of (timestamp, tweet_id)
        self.tweets = defaultdict(list)
        # user_id → set of followed user_ids
        self.following = defaultdict(set)

    def postTweet(self, userId, tweetId):
        # Negative timestamp kyunki min heap use kar rahe hain
        # Latest tweet = most negative = top of heap
        self.tweets[userId].append((-self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId):
        # User khud ko follow karta hai
        users = self.following[userId] | {userId}
        
        # Min heap mein saare users ke latest tweets daalo
        heap = []
        for user in users:
            if self.tweets[user]:
                # Latest tweet index
                idx = len(self.tweets[user]) - 1
                time, tweet_id = self.tweets[user][idx]
                heapq.heappush(heap, (time, tweet_id, user, idx))
        
        result = []
        while heap and len(result) < 10:
            time, tweet_id, user, idx = heapq.heappop(heap)
            result.append(tweet_id)
            
            if idx > 0:
                idx -= 1
                time, tweet_id = self.tweets[user][idx]
                heapq.heappush(heap, (time, tweet_id, user, idx))
        
        return result

    def follow(self, followerId, followeeId):
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.following[followerId].discard(followeeId)

#----Testing----
solver = Twitter()
solver.postTweet(1, 5)
print(solver.getNewsFeed(1))   # [5]
solver.follow(1, 2)
solver.postTweet(2, 6)
print(solver.getNewsFeed(1))   # [6, 5]
solver.unfollow(1, 2)
print(solver.getNewsFeed(1))   # [5]