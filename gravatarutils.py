import urllib, hashlib

class GravatarUtils:
	"""
	Gravatar Utility to convert email to its corresponding gravatar.
	thanks to https://fr.gravatar.com/site/implement/images/python/ 
	"""
	def __init__(self):
		"""
		Initialize default root url.
		"""
		self.root = "http://www.gravatar.com/avatar/"

	# construct the url
	def get(self, email, default="http://www.gravatar.com/avatar/", size=32):
		"""
		Compute the corresponding gravatar url for email user. 
		"""
		return self.root + hashlib.md5(email.lower().encode('utf-8')).hexdigest() + "?s="+str(size) 
