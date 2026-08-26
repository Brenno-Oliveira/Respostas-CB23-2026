#1. 	
	As classes bases são: Pessoa e a classe adicionada estabelecimento.
	
	As subclasses de funcionario são: 
	
garçom; herda todos os métodos e tem como função anotar_pedido().

chefe de cozinha; herda todos os métodos e tem como função preparar().

gerente; herda todos os métodos e tem como função demitir().
	
	Há uma relação direta entre estabelecimento-restaurante-pizzaria, onde cada uma herda todos os métodos da anterior e tem seu método específico, como cardapio e rodizio. A classe iguaria é independente das demais e possui uma relação de composição com restaurante e pizzaria.
	
	As subclasses de iguaria são:
	
pizza; herda todos os métodos e tem seu próprio método pizza_recheada.

bolo; herda todos os métodos e tem seu próprio método formato.


#2. 

	Possui uma relação de composição, onde as subclasses de iguaria são interligadas com as outras. Por exemplo, pizza não é subordinado à pizzaria, mas sim a iguaria, pois apesar de parecer lógico existir pizza na pizzaria, os métodos que pizz deve ter são herdados de iguaria e nada tem haver com pizzaria. 
	
#3. 

	Argumento1: Um dicionário cuja chave é o item a ser pedido (string) e o valor a quantidade (int) ou uma instacia de iguaria ou de suas subclasses.
	
	Argumento2: Um dicionário cuja chave é o prato a ser preparado (string) e o valor a quantidade (int) ou uma instacia de iguaria ou de suas subclasses.
	
	Argumento3: Uma string com o nome do funcionário ou uma instancia da classe funcionario.
