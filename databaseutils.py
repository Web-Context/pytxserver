from pymongo import Connection
import pymongo
from jsonutils import JSONUtils

#----- Data Access Utils -------------------------------

class DatabaseUtils:
    
    # Initialization for Database connection ------
    def __init__(self):
        self.connection = Connection("mongodb://localhost:27017/")
        self.client = self.connection.gamesdb
        self.client.games
        self.client.platforms
        self.client.users

        self.loadData(self.client.games, "data/games.json")
        self.loadData(self.client.platforms, "data/platforms.json")
        self.loadData(self.client.users, "data/users.json")

    # Load filename JSON content to the named collection.
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

    #----- Users --------------------------------------

    # Create a new Game
    def createGame(self, game):
        self.client.games.insert(game)
 
    # Retrieve all games
    def findGames(self, offset=0, maxPage=10):
        games = self.client.games.find().sort('title', pymongo.DESCENDING).skip(offset).limit(maxPage)
        return games

    # Retrieve a game on its id
    def findGameById(self, gameId):
        game = self.client.games.find_one({'id':gameId})
        return game

    # Search for games on title pattern
    def searchGameByTitle(self, title, offset=0, maxPage=10):
        games = self.client.games.find({'title':{'$search' : title}}, {'score':{'$meta':'textScore'}}).limit(maxPage)
        return games

    # Find games for a specific platform code.        
    def findGamesForPlatform(self, platformCode="all", offset=0, maxPage=10):
        if(platformCode=="all"):
            games = self.client.games.find().sort('title', pymongo.DESCENDING).limit(maxPage)
        else:
            games = self.client.games.find({'platform':platformCode}).sort('title', pymongo.DESCENDING).limit(maxPage)
        return games

    #----- Platform --------------------------------------
    
    # Create a new Platform        
    def createPlatform(self, platform):
        self.client.platforms.insert(platform)

    # Retrieve all platforms
    def findPlatforms(self, offset=0, maxPage=10):
        platforms = self.client.platforms.find().sort('code', pymongo.ASCENDING).limit(maxPage)
        return platforms

    # Retrieve a platform on its code.
    def findPlatformByCode(self, platformCode):
        platform = self.client.platforms.find_one({'code':platformCode})
        return platform

    #----- Users --------------------------------------

    # Create a new user
    def createUser(self, user):
        self.client.users.insert(user)

    # Retrieve all user
    def findUsers(self, offset = 0, maxPage = 10):
        users = self.client.users.find().limit(maxPage)
        return users

    # Retrieve User on its username.
    def findUserByUsername(self, username = "*"):
        users = self.client.users.find({'username':username})
        return users
    
    # Authenticate user on its username/password.
    def authenticate(self, username, password):
        user = self.findUserByUsername(username)
        if (user['password'] == password):
            return user
        else:
            return False
