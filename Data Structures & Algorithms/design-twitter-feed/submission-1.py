class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)     # userId -> list of (time, tweetId)
        self.following = defaultdict(set)   # userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        candidates = []
        users = self.following[userId] | {userId}
        for u in users:
            candidates += self.tweets[u][-10:]

        candidates.sort(reverse=True)
        return [tweetId for _, tweetId in candidates[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)