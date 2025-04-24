class User:
    def __init__(self, userId):
        self.userId = userId
        self.tweets = set()
        self.following = set()
    
    def __str__(self):
        print(f"{self.userId} - {self.tweets} - {self.following}")

class Twitter:

    def __init__(self):
        self.users = dict()
        self.tweetPosition = 1
            
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            newUser = User(userId)
            self.users[userId] = newUser
        
        self.users[userId].tweets.add((self.tweetPosition, tweetId))
        self.tweetPosition += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        obtainedFeeds = [] # Id of people whose feed already considered
        if userId not in self.users:
            self.users[userId] = User(userId)
        listOfPeople = self.users[userId].following; listOfPeople.add(userId)
        feeds = set()
        for personId in listOfPeople:
            personFeed = self.users[personId].tweets
            feeds = feeds.union(personFeed)
        
        return [feed[1] for feed in sorted(list(feeds), reverse=True)][:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.users:
            self.users[followeeId] = User(followeeId)

        if followerId not in self.users:
            self.users[followerId] = User(followerId)

        if followeeId not in self.users[followerId].following:
            self.users[followerId].following.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users and followeeId in self.users[followerId].following:
            self.users[followerId].following.remove(followeeId)
