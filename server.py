from bottle import Bottle, route, run, template
import textile

app=Bottle()

def readFile(file):
	f = open(file, "r")
	# Read the entire contents of a file at once.
	fcontent = f.read()
	f.close()
	return fcontent


@app.route('/')
@app.route('/<page>')
def index(page='index'):
	mytemplate = readFile('template/index.html')
	if(page!='favicon.ico'):
		mypage = readFile('pages/'+page+'.textile')
		txpage = textile.textile(mypage)
		print txpage
	return template(mytemplate,page=txpage, page_title=page)

run(app, host='localhost', port=8080, reloader=True)
