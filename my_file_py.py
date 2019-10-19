from my_file import MyFile

class MyFilePY(MyFile):

	def __init__(self):  
         self.query_imports = "//python:Module"  
         self.query_calls = "//python:BoxedAttribute"


	def get_json_imports(self, node_json_decode):
		for item in node_json_decode["body"]:
			#print("{node}\n".format(node=item.keys()))
			if "Path" in item.keys():
				if "Name" in item["Path"].keys():
		        	 print("{node}".format(node=item["Path"]["Name"]))
	

	def get_json_calls(self, node_json_decode):
		if "boxed_value" in node_json_decode.keys():
				if "Name" in node_json_decode["boxed_value"].keys():
		        	 print("{node}".format(node=node_json_decode["boxed_value"]["Name"]))

