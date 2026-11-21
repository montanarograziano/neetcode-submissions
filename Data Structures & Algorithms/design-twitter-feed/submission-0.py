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
        # Include the user themselves alongside everyone they follow
        users = self.following[userId] | {userId}

        for u in users:
            # Only the last 10 tweets of any user could ever make the top 10
            candidates.extend(self.tweets[u][-10:])

        # Sort newest first (highest self.time) and return top 10 tweetIds
        candidates.sort(reverse=True)
        return [tweetId for _, tweetId in candidates[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)