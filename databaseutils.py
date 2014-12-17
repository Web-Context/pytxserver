from pymongo import Connection
import pymongo
from jsonutils import JSONUtils

class DatabaseUtils:
    
    def loadData(self, collection, filename):
        
        """
        This loadData method load data from a jsonUtils file and load them into
        the collection.
        """
        jsonUtils = JSONUtils()
        if (collection.count() == 0):
            listItems = jsonUtils.readFromJson(filename)
            for item in listItems:
                collection.insert(item.__dict__)

    
    def __init__(self):
        self.connection = Connection("mongodb://localhost:27017/")
        self.client = self.connection.gamesdb
        self.client.games
        self.client.platforms
        self.client.users

        self.loadData(self.client.games, "data/games.json")
        self.loadData(self.client.platforms, "data/platforms.json")
        self.loadData(self.client.users, "data/users.json")

    def findGames(self,maxPage=10):
        games = self.client.games.find().sort('title', pymongo.ASCENDING).limit(maxPage)
        return games

    def findGamesForPlatform(self, platformCode,maxPage=10):
        games = self.client.games.find({'platform':platformCode}).sort('title', pymongo.ASCENDING).limit(maxPage)
        return games
    
    def createGame(self, game):
        self.client.games.insert(game)
 
    def searchGameByTitle(self, title,maxPage):
        games = self.client.games.find({'title':{'$search' : title}}, {'score':{'$meta':'textScore'}}).limit(maxPage)
        return games
 
    def findGameById(self, gameId):
        game = self.client.games.find_one({'id':gameId})
        return game
    

    def findPlatforms(self,maxPage=10):
        platforms = self.client.platforms.find().sort('code', pymongo.ASCENDING).limit(maxPage)
        return platforms

    def findPlatformByCode(self, platformCode):
        platform = self.client.platforms.find_one({'code':platformCode})
        return platform
    
    def createPlatform(self, platform):
        self.client.platforms.insert(platform)

    def findUsers(self,maxPage):
        users = self.client.users.find().limit(maxPage)
        return users
    
    def findUserByUsername(self, username):
        users = self.client.users.find({'username':username})
        return users
    
    def authenticate(self, username, password):
        user = self.findUserByUsername(username)
        if (user['password'] == password):
            return True
        else:
            return False
        
    def createUser(self, user):
        self.client.users.insert(user)
