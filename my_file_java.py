from my_file import MyFile

class MyFileJava(MyFile):

	def __init__(self):  
         self.query_imports = "//uast:Import"  
         self.query_calls = "//*[@role='Call' and @role='Callee']" 

	def get_json_imports(self, node_json_decode):
		#self.save_log(node_json_decode)
		#print("{node}\n".format(node=node_json_decode.keys()))
		self.my_iterator_imports_java(node_json_decode["Path"]["Names"])
		self.my_iterator_imports_java(node_json_decode["Names"])

	def my_iterator_imports_java(self, lista):
		for item in lista:
			#print("{node}\n".format(node=item.keys()))
			if "Name" in item.keys():
		    	 print("{node}".format(node=item["Name"]))
	

	def get_json_calls(self, node_json_decode):
		if "Name" in node_json_decode.keys():
			print("{node}".format(node=node_json_decode["Name"]))

