class HTMLUtils:
	def presetHeader(self, request,response, language):
		response.set_header('Content-Language', language)
		if(request.get_cookie("gk2-visited")):
			return True
		else:
			response.set_cookie("gk2-visited","yes")
			return False
	
