import bblfsh
import os
from my_file import MyFile
from my_file_js import MyFileJS
from my_file_java import MyFileJava
from my_file_py import MyFilePY
from my_file_php import MyFilePHP
from my_file_rb import MyFileRB

class MyController:
	server_endpoint = "localhost:9432"
	allowed_file_extensions = ["js","java","py","php","rb"]

	def __init__(self, path):
		self.path = path
		self.client = bblfsh.BblfshClient(self.server_endpoint)

	'''def files_path04(self):
	    for caminho, _, arquivos in os.walk(self.path):
	    	for arquivo in arquivos:
	    		extension = arquivo.rpartition(".")[-1]
	    		if extension in self.allowed_file_extensions:
	    			print(caminho, arquivo, extension)'''

	def parse(self, path, filename):
		extension = filename.rpartition(".")[-1]

		if extension in self.allowed_file_extensions:
			print("\nEXTENSION: {title}\n".format(title=extension))
			ctx = self.client.parse(path+"/"+filename, mode=bblfsh.Modes.SEMANTIC)

			self.my_file = self.init_my_file(extension)

			self.my_file.my_execute(ctx)


	def init_my_file(self, extension):
		res_file= None

		if extension == self.allowed_file_extensions[0]:
			res_file = MyFileJS()
		if extension == self.allowed_file_extensions[1]:
			res_file = MyFileJava()
		if extension == self.allowed_file_extensions[2]:
			res_file = MyFilePY()
		if extension == self.allowed_file_extensions[3]:
			res_file = MyFilePHP()
		if extension == self.allowed_file_extensions[4]:
			res_file = MyFileRB()

		return res_file;

	def simple_test(self, path, filename):
		print("\nSIMPLE_TEST\n")
		self.parse(path, filename)

	def medium_test(self, path, list):
		print("\nMEDIUM_TEST\n")
		for filename in list:
			self.parse(path, filename)


my_domain_path = "/home/lost/charles/teste_folder";
obj = MyController(my_domain_path)
#obj.files_path04()

file_tests1= ["ApiSpecs.js","JobExecutionExitCodeGeneratorTests.java","test_model_saving.py","Setup_test.php","spec_helper.rb"]

#obj.simple_test(my_domain_path, file_tests1[4])

obj.medium_test(my_domain_path, file_tests1)