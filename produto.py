class Produto: # Criamos uma classe chamada Produto, uma classe é molde ou "receita" para criar objetos com caracteristicas.
    def __init__(self, nome, categoria, quantidade, preco, id=None): # Este é o construtor da classe, que define os atributos do produto quando eu crio um novo objeto
        self.id = id # Guarda o identificador único do produto no banco (geralmente o banco gera sozinho).
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.preco = preco

# O resto de seft.... Guardam as informações básicas do produto, como nome, categoria, quantidade em estoque e preço.