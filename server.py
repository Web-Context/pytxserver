from bottle import TEMPLATES, route, view, request, response, run, abort, static_file
import textile
import json
from jsonutils import FileUtils
from textutils import TextUtils
from htmlutils import HTMLUtils
from databaseutils import DatabaseUtils

language = 1
__version__ = 1.1

fileUtils = FileUtils()
textUtils = TextUtils()
htmlUtils = HTMLUtils()
database = DatabaseUtils()

@route("/clear/cache")
def clearCache():
	TEMPLATES.clear();

# Show a specific public 
# resource like css, js, jpg, png.
@route('/public/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root='public/')

# Show a textile page
@route('/')
@route('/page/<page:path>')
@view('page')
def index(page='index'):	
	htmlUtils.presetHeader(request,response, language)
	games     = database.findGames()
	platforms = database.findPlatforms()
	csspage   = "home"
	
	if(page != 'favicon.ico'):
		mypage = fileUtils.readFile('pages/' + page + '.textile')
		txpage = textile.textile(mypage)
		return  dict(
			version    = __version__,
			language   = language,
			csspage    = csspage,
			page       = ''+txpage,
			games      = games,
			platforms  = platforms,
			platform = {},
			game = {},
			page_title = page)
	else:
		abort(404, "Requested page does not exist !")

# Show a game test.
@route('/game/<gameId:path>')
@view('game')
def game(gameId):
	htmlUtils.presetHeader(request,response, language)
	games     = database.findGames()
	platforms = database.findPlatforms()
	game      = database.findGameById(gameId)
	platform  = database.findPlatformByCode(game['platform'])
	csspage      = "game"

	if(games and platforms):
		if(game):
			game['rates'][0]=textUtils.convertRate(game['rates'][0])
			game['rates'][1]=textUtils.convertRate(game['rates'][1])
			game['rates'][2]=textUtils.convertRate(game['rates'][2])
			game['rates'][3]=textUtils.convertRate(game['rates'][3])
			return dict(
				version    = __version__,
				language   = language,
				csspage    = csspage,
				game       = game,
				games      = games,
				platforms  = platforms,
				platform   = platform,
				page_title = game['title'])
		else:
			abort(404,"Game for _id="+gameId+" not found")
	else:
		abort(404,"The Requested Game _id="+gameId)

# Search for a game.
@route('/games/search/<title:path>')
@view('search')
def search(title):
	htmlUtils.presetHeader(request,response, language)

	games = database.searchGameByTitle(title)		

	if(games):
		page_title = "Search result"+(len(games))+" for '"+title+"'"
		return dict(
			version    = __version__,
			language   = language,
			games      = games,
			page_title = page_title)
	else:
		abort(404,"search for '"+title+"' has no result.")

# Show games for a platform.
@route('/games/<platformCode:path>')
@view('games')
def games(platformCode):
	htmlUtils.presetHeader(request,response, language)
	games = database.findGamesForPlatform(platformCode)		
	platforms = database.findPlatforms()
	platform  = database.findPlatformByCode(platformCode)
	csspage   = "game" 
	
	if(games and platforms):
		return dict(
			version    = __version__,
			language   = language,
			csspage    = csspage,
			games      = games,
			platforms  = platforms,
			platform   = platform,
			page_title = "Games for "+platformCode)
	else:
		abort(404,"The Requested Game id="+platformCode)

#create a game.
@route("/game", method='PUT')
def create():
	htmlUtils.presetHeader(request,response, language)
	data = request.body.read()
	if not data:
		abort(400,"No data received")
	game = json.loads(data)
	if not game.has_key('_id'):
		abort(400,"no _id specified to store game data")
	database.createGame(game)
	return dict( game = game)

# User login in JSON format.
@route("/login", method="POST") 
def authenticate(): 
	username = request.forms.get("username") 
	password = request.forms.get("password")
	user =  check_login(username, password)
	if user :
		userjson = jsonutils.json2obj(user)
		return "{'message':'User not authorized to login','user':"+userjson+"}"
	else: 
		return abort(403,"{'message':'User not authorized to login'}") 

# Start server and delegate to cherrypy
# multi-threading http server.
run( server='cherrypy', 
	 host='localhost', 
	 port=8000, 
	 debug=True, 
	 reloader=True)
