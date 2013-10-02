from bottle import Bottle, route, run, template, static_file
import textile
import string

app=Bottle()

def readFile(file):
	f = open(file, "r")
	# Read the entire contents of a file at once.
	fcontent = f.read()
	f.close()
	return fcontent


@app.route('/')
@app.route('/p/<page:path>')
def index(page='index'):
	mytemplate = readFile('template/main.html')
	if(page!='favicon.ico'):
		mypage = readFile('pages/'+page+'.textile')
		txpage = textile.textile(mypage)

	return  template(
			mytemplate,
			page=''+txpage, 
			page_title=page)


@app.route('/public/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='public/' )

run(app, host='localhost', port=8080, reloader=True)
