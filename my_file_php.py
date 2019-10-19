from my_file import MyFile

class MyFilePHP(MyFile):

	def __init__(self):  
         self.query_imports = "//php:Stmt_Class"  
         self.query_calls = "//php:Expr_MethodCall"

	def get_json_imports(self, node_json_decode):
		#print("{node}\n".format(node=node_json_decode.keys()))
		#self.save_log(node_json_decode);
		if "Name" in node_json_decode["extends"]:
			print("{node}".format(node=node_json_decode["extends"]["Name"]))
	

	def get_json_calls(self, node_json_decode):
		#self.save_log(node_json_decode);
		#print("{node}".format(node=node_json_decode["name"]["Name"]))
		if "name" in node_json_decode.keys():
				if "Name" in node_json_decode["name"].keys():
		        	 print("{node}".format(node=node_json_decode["name"]["Name"]))

