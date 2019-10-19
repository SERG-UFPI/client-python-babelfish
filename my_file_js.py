from my_file import MyFile

class MyFileJS(MyFile):

	def __init__(self):  
    	 self.query_imports = "//javascript:CallExpression"  
    	 self.query_calls = "//*[@role='Call' and @role='Callee']"

	def get_json_imports(self, node_json_decode):
		#print("{node}\n".format(node=node_json_decode["arguments"].keys()))
		for item in node_json_decode["arguments"]:
			#print("{node}\n".format(node=item.keys()))
			if "Value" in item.keys():
		    	 print("{node}".format(node=item["Value"]))
	

	def get_json_calls(self, node_json_decode):
		#print("{node}".format(node=node_json_decode.keys()))
		if "Name" in node_json_decode.keys():
			print("{node}".format(node=node_json_decode["Name"]))

