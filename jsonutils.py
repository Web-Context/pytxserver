import json
from collections import namedtuple


class FileUtils:
        # Smart function to read a file content.
    def readFile(self,filename):
        f = open(filename, "r")
        # Read the entire contents of a file at once.
        fcontent = f.read()
        f.close()
        return fcontent
    
class JSONUtils:
    # Convert JSON object to python object
    def _json_object_hook(self,d): 
        return namedtuple('X', d.keys())(*d.values())
    
    # Convert JSON to object
    def json2obj(self,data): 
        return json.loads(data, object_hook=self._json_object_hook)
        
    def readFromJson(self,file):
        fileUtils = FileUtils()
        data = fileUtils.readFile(file)
        return self.json2obj(data)

