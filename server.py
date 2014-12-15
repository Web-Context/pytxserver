from bottle import TEMPLATES, route, view, request, response, run, abort, static_file
import textile
import json
from collections import namedtuple

language = 'en'

def convertRate(rate):
	rate = rate/4
	return ("-"*4)

def presetHeader(request,response):
	response.set_header('Content-Language', language)
	if(request.get_cookie("gk2-visited")):
		return True
	else:
		response.set_cookie("gk2-visited","yes")
		return False

# Convert JSON object to python object
def _json_object_hook(d): 
	return namedtuple('X', d.keys())(*d.values())

# Convert JSON to object
def json2obj(data): 
	return json.loads(data, object_hook=_json_object_hook)

# Smart function to read a file content.
def readFile(filename):
	f = open(filename, "r")
	# Read the entire contents of a file at once.
	fcontent = f.read()
	f.close()
	return fcontent


@route("/clear/cache")
def clearCache():
	TEMPLATES.clear();

# Show a specific public 
# resource like css, js, jpg, png.
@route('/public/<filepath:path>')
def server_static(filepath):
	presetHeader(request,response)

	return static_file(filepath, root='public/')

# Show a textile page
@route('/')
@route('/page/<page:path>')
@view('page')
def index(page='index'):
	presetHeader(request,response)
	gamesjson = readFile('data/games.json')
	games        = json2obj(gamesjson)	
	platformjson = readFile('data/platforms.json')	
	platforms    = json2obj(platformjson)

	if(page != 'favicon.ico'):
		mypage = readFile('pages/' + page + '.textile')
		txpage = textile.textile(mypage)
		return  dict(
			language   = language,
			page       = ''+txpage,
			games      = games,
			platforms  = platforms,
			page_title = page)
	else:
		abort(404, "Requested page does not exist !")

# Show a game test.
@route('/game/<gameid:int>')
@view('game')
def game(gameid):
	presetHeader(request,response)
	gamesjson = readFile('data/games.json')
	games        = json2obj(gamesjson)	
	platformjson = readFile('data/platforms.json')	
	platforms    = json2obj(platformjson)

	if(games and platforms):
		game = games[gameid]
		if(games[gameid]):
			return dict(
				language   = language,
				game       = game,
				games      = games,
				platforms  = platforms,
				page_title = "Game "+game.title)
		else:
			abort(403,"Game for id="+gameid+" not found")
	else:
		abort(404,"The Requested Game id="+gameid)

# Show games for a platform.
@route('/games/<platformid:path>')
@view('games')
def games(platformid):
	presetHeader(request,response)
	gamesjson = readFile('data/games.json')
	games        = json2obj(gamesjson)	
	platformjson = readFile('data/platforms.json')	
	platforms    = json2obj(platformjson)

	if(games and platforms):
		return dict(
			language   = language,
			games      = games,
			platforms  = platforms,
			page_title = "Games for "+platformid)
	else:
		abort(404,"The Requested Game id="+platformid)

# Start server and delegate to cherrypy
# multi-threading http server.
run( server='cherrypy', 
	 host='localhost', 
	 port=8000, 
	 debug=True, 
	 reloader=True)
