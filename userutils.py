import bottle
from bottle import TEMPLATES, route, view, request, response, run, abort, static_file, redirect
from databaseutils import DatabaseUtils

class UserUtils :
	def __init__(self):
		self.db = DatabaseUtils()

	def login(self,request):
		username = request.forms.get("username") 
		password = request.forms.get("password")
		user =  self.db.authenticate(username, password)
		if user :
			session = bottle.request.environ.get('beaker.session')
			session['user']=user
			return user
		else: 
			return None

