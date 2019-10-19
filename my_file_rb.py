from my_file import MyFile 

class MyFileRB(MyFile):

	def __init__(self):  
         self.query_imports = "//ruby:send_require"  
         self.query_calls = "//uast:Function"

	def get_json_imports(self, node_json_decode):
		#self.save_log(node_json_decode)
		#print("{node}\n".format(node=node_json_decode.keys()))
		for item in node_json_decode["Names"]:
			#print("{node}\n".format(node=item.keys()))
		    if "Path" in item.keys():
			    if "Value" in item["Path"].keys():
		             print("{node}".format(node=item["Path"]["Value"]))
	

	def get_json_calls(self, node_json_decode):
		#self.save_log(node_json_decode);
		#print("\n{node}".format(node=node_json_decode))
		if "Name" in node_json_decode.keys():
			print("{node}".format(node=node_json_decode["Name"]))
