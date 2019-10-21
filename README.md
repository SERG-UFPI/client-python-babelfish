#Client-python-babelfish
implementação em python de parse de linguagens de programação utilizando Babelfish. 


# Executando o scripty main
Para executar o script execute no terminal o cmd <i>python3 scripty.py</i>

No arquivo scripty.py é criada uma instância do servidor local através do código <i>self.client = bblfsh.BblfshClient(self.server_endpoint)</i>


# Funcionamento dos arquivos
## scripty.py
arquivo que irá executar os scripts 

## my_file.py
Representa a classe responsável por aplicar os filtros na AST retornada do parse realizado pelo servidor do Babelfish e interar cada nó da árvore

## my_file_js.py, my_file_java.py, my_file_py.py, my_file_php.py, my_file_rb.py
São as classes responsáveis por possuir a string que será aplicada no filter do parse através dos atributos <i>query_imports</i> e <i>query_imports</i> e interar cada nó da árvore específica para a linguagem

## my_file_js.py
Representa classe para tratar a iteração da AST de arquivos Javascript

## my_file_java.py
Representa classe para tratar a iteração da AST de arquivos Java

## my_file_py.py
Representa classe para tratar a iteração da AST de arquivos Phyton

## my_file_php.py
Representa classe para tratar a iteração da AST de arquivos PHP

## my_file_rb.py
Representa classe para tratar a iteração da AST de arquivos Ruby
