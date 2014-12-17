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

	if(page != 'favicon.ico'):
		mypage = fileUtils.readFile('pages/' + page + '.textile')
		txpage = textile.textile(mypage)
		return  dict(
			version = __version__,
			language   = language,
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

	if(games and platforms):
		if(game):
			game['rates'][0]=textUtils.convertRate(game['rates'][0])
			game['rates'][1]=textUtils.convertRate(game['rates'][1])
			game['rates'][2]=textUtils.convertRate(game['rates'][2])
			game['rates'][3]=textUtils.convertRate(game['rates'][3])
			return dict(
				version = __version__,
				language   = language,
				game       = game,
				games      = games,
				platforms  = platforms,
				platform = platform,
				page_title = game['title'])
		else:
			abort(404,"Game for _id="+gameId+" not found")
	else:
		abort(404,"The Requested Game _id="+gameId)

# Show games for a platform.
@route('/games/<platformCode:path>')
@view('games')
def games(platformCode):
	htmlUtils.presetHeader(request,response, language)

	games = database.findGamesForPlatform(platformCode)		
	platforms = database.findPlatforms()
	platform  = database.findPlatformByCode(platformCode)

	if(games and platforms):
		return dict(
			version = __version__,
			language   = language,
			games      = games,
			platforms  = platforms,
			platform = platform,
			page_title = "Games for "+platformCode)
	else:
		abort(404,"The Requested Game id="+platformCode)

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

# Start server and delegate to cherrypy
# multi-threading http server.
run( server='cherrypy', 
	 host='localhost', 
	 port=8000, 
	 debug=True, 
	 reloader=True)
