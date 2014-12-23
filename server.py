import bottle
import json
import textile
from bottle import TEMPLATES, route, view, request, response, run, abort, static_file, redirect
from beaker.middleware import SessionMiddleware
from databaseutils import DatabaseUtils
from htmlutils import HTMLUtils
from jsonutils import FileUtils
from textutils import TextUtils
from userutils import UserUtils

LANG = 1
VERSION = 1.2

fileUtils = FileUtils()
textUtils = TextUtils()
htmlUtils = HTMLUtils()
userutils = UserUtils()

db = DatabaseUtils()

session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.data_dir': './sessions',
    'session.auto': True
}
app = SessionMiddleware(bottle.app(), session_opts)


def getUserFromSession():
	session = bottle.request.environ.get('beaker.session')
	if('user' in session ):
		user = session['user']
	else:
		user = None
	return user


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
	htmlUtils.presetHeader(request,response, LANG)
	games     = db.findGames()
	platforms = db.findPlatforms()
	csspage   = "home"
	user = getUserFromSession()

	if(page != 'favicon.ico'):
		mypage = fileUtils.readFile('pages/' + page + '.textile')
		txpage = textile.textile(mypage)
		return  dict(
			user 		= getUserFromSession(),
			version    	= VERSION,
			language    = LANG,
			csspage    	= csspage,
			page       	= ''+txpage,
			games      	= games,
			platforms  	= platforms,
			platform 	= {},
			game 		= {},
			page_title 	= page)
	else:
		abort(404, "Requested page does not exist !")

# Show a game test.
@route('/game/<gameId:path>')
@view('game')
def game(gameId):
	htmlUtils.presetHeader(request,response, LANG)
	games     = db.findGames()
	platforms = db.findPlatforms()
	game      = db.findGameById(gameId)
	platform  = db.findPlatformByCode(game['platform'])
	csspage      = "game"

	if(games and platforms):
		if(game):
			game['rates'][0]=textUtils.convertRate(game['rates'][0])
			game['rates'][1]=textUtils.convertRate(game['rates'][1])
			game['rates'][2]=textUtils.convertRate(game['rates'][2])
			game['rates'][3]=textUtils.convertRate(game['rates'][3])
			return dict(
				version    	= VERSION,
				language    = LANG,
				user 		= getUserFromSession(),
				csspage    	= csspage,
				game       	= game,
				games      	= games,
				platforms  	= platforms,
				platform   	= platform,
				page_title 	= game['title'])
		else:
			abort(404,"Game for _id="+gameId+" not found")
	else:
		abort(404,"The Requested Game _id="+gameId)

# Search for a game.
@route('/games/search/<title:path>')
@view('search')
def search(title):
	htmlUtils.presetHeader(request,response, LANG)

	games = db.searchGameByTitle(title)		

	if(games):
		page_title = "Search result"+(len(games))+" for '"+title+"'"
		return dict(
			version    	= VERSION,
			language    = LANG,
			user 		= getUserFromSession(),
			games      = games,
			page_title = page_title)
	else:
		abort(404,"search for '"+title+"' has no result.")

# Show games for a platform.
@route('/games/<platformCode:path>')
@view('games')
def games(platformCode):
	htmlUtils.presetHeader(request,response, LANG)
	games = db.findGamesForPlatform(platformCode)		
	platforms = db.findPlatforms()
	platform  = db.findPlatformByCode(platformCode)
	csspage   = "game" 
	
	if(games and platforms):
		return dict(
			version    	= VERSION,
			language    = LANG,
			user 		= getUserFromSession(),
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
	htmlUtils.presetHeader(request,response, LANG)
	data = request.body.read()
	if not data:
		abort(400,"No data received")
	game = json.loads(data)
	if not game.has_key('_id'):
		abort(400,"no _id specified to store game data")
	db.createGame(game)
	return dict( game = game)

# User login in JSON format.
@route("/login", method="POST") 
@view('index')
def login(): 
	user = userutils.login(request)
	redirect('/')

# User login in JSON format.
@route("/logout", method="GET") 
def logout(): 
	session = bottle.request.environ.get('beaker.session')
	session['user'] = None
	session.save()
	redirect('/')


# Start server and delegate to cherrypy
# multi-threading http server.
bottle.run( 
	 app=app,
	 server='cherrypy', 
	 host='localhost', 
	 port=8000, 
	 debug=True, 
	 reloader=True)
