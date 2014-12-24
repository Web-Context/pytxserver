import bottle
from bottle import TEMPLATES, route, view, request, response, run, abort, static_file, redirect
from databaseutils import DatabaseUtils
from gravatarutils import GravatarUtils

class UserUtils :
	def __init__(self):
		"""
		Initialize utilities.
		"""
		self.db = DatabaseUtils()
		self.gravatar = GravatarUtils()

	def login(self,request):
		"""
		Log in  user based on username and password in the request.
		"""
		username = request.forms.get("username") 
		password = request.forms.get("password")
		user =  self.db.authenticate(username, password)
		if user :
			session = bottle.request.environ.get('beaker.session')
			user['avatar']  = self.gravatar.get(''+user['email'])
			session['user'] = user
			return user
		else: 
			return None

