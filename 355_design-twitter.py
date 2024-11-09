from collections import defaultdict
import heapq
from typing import List
import unittest


class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((-self.count, tweetId))
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                maxHeap.append((count, tweetId, followeeId, index - 1))
        heapq.heapify(maxHeap)
        while maxHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(maxHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(maxHeap, (count, tweetId, followeeId, index - 1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)


class TestTwitter(unittest.TestCase):

    def test_twitter(self):
        twitter = Twitter()
        twitter.postTweet(1, 5)
        assert twitter.getNewsFeed(1) == [5]
        twitter.follow(1, 2)
        twitter.postTweet(2, 6)
        assert twitter.getNewsFeed(1) == [6, 5]
        twitter.unfollow(1, 2)
        assert twitter.getNewsFeed(1) == [5]
        twitter.postTweet(1, 7)
        twitter.postTweet(1, 8)
        twitter.postTweet(1, 9)
        twitter.postTweet(1, 10)
        twitter.postTweet(1, 11)
        twitter.postTweet(1, 12)
        twitter.postTweet(1, 13)
        twitter.postTweet(1, 14)
        twitter.postTweet(1, 15)
        twitter.postTweet(1, 16)
        twitter.postTweet(1, 17)
        twitter.postTweet(1, 18)
        twitter.postTweet(1, 19)
        twitter.postTweet(1, 20)
        twitter.postTweet(1, 21)
        twitter.postTweet(1, 22)
        twitter.postTweet(1, 23)
        twitter.postTweet(1, 24)
        twitter.postTweet(1, 25)
        twitter.postTweet(1, 26)
        twitter.postTweet(1, 27)
        twitter.postTweet(1, 28)
        twitter.postTweet(1, 29)
        twitter.postTweet(1, 30)
        twitter.postTweet(1, 31)
        twitter.postTweet(1, 32)
        twitter.postTweet(1, 33)
        twitter.postTweet(1, 34)
        twitter.postTweet(1, 35)
        twitter.postTweet(1, 36)
        twitter.postTweet(1, 37)
        twitter.postTweet(1, 38)
        twitter.postTweet(1, 39)
        twitter.postTweet(1, 40)
        twitter.postTweet(1, 41)
        twitter.postTweet(1, 42)
        twitter.postTweet(1, 43)
        twitter.postTweet(1, 44)
        twitter.postTweet(1, 45)
        twitter.postTweet(1, 46)
        twitter.postTweet
        assert twitter.getNewsFeed(1) == [46, 45, 44, 43, 42, 41, 40, 39, 38, 37]
