import json 

class MyFile:
	tratar_imports = "imports"
	tratar_calls = "calls"
	query_imports = ""
	query_calls = ""

	def my_execute(self, ctx):
		imports = ctx.filter(self.query_imports) #filter for get imports
		calls = ctx.filter(self.query_calls) #filter for get functions

		self.my_iterator(self.tratar_imports,imports)
		self.my_iterator(self.tratar_calls,calls)

	def save_log(self, conteudo):
		f= open("/home/lost/charles/scripty.log","w+")
		f.write("{conteudo}\r\n".format(conteudo=conteudo))
		f.close() 


	def my_iterator(self, title, it):
		print("\n{title}".format(title=title.upper()))
		for node in it:
		    # print internal node:
		    self.get_json_info(title, node)


		print("----------------------------------------------------------------\n")

	def get_json_info(self, title, node):
		node_json_encode = json.dumps(node.get()) #parse for string
		node_json_decode = json.loads(node_json_encode) #parse for json

		if (title == self.tratar_imports):
			return self.get_json_imports(node_json_decode)
		else:
			return self.get_json_calls(node_json_decode)
