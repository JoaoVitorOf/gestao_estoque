from database import get_connection #Aqui importamos do database.py a função get_connection (Que serve para concecta com banco de dados)
from produto import Produto #Aqui importamos do produto.py a class Produto

# Função para cadastrar produto
def cadastrar_produto():
    nome = input("Nome do produto: ")
    categoria = input("Categoria: ")
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: ").replace(",", "."))

    conn = get_connection()
    cursor = conn.cursor()

    # Verifica se já existe um produto com o mesmo nome (Afim de evitar duplicatas)
    cursor.execute("SELECT * FROM produtos WHERE nome = ?", (nome,))
    produto_existente = cursor.fetchone()

    if produto_existente:
        print("Produto já cadastrado no estoque. Operação cancelada.")
    else:
        cursor.execute(
            "INSERT INTO produtos (nome, categoria, quantidade, preco) VALUES (?, ?, ?, ?)",
            (nome, categoria, quantidade, preco)
        )
        conn.commit()
        print("Produto cadastrado com sucesso!")

    conn.close()

# Função para listar produtos 
def listar_produtos():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    conn.close()

    if produtos:
        print("\n--- Lista de Produtos ---")
        for p in produtos:
            print(f"ID: {p[0]}")
            print(f"Nome: {p[1]}")
            print(f"Categoria: {p[2]}")
            print(f"Quantidade: {p[3]}")
            print(f"Preço: R$ {p[4]:.2f}")
            print("-" * 30)
    else:
        print("Nenhum produto cadastrado.")

# Função para atualizar produto
def atualizar_produto():
    listar_produtos()
    id_produto = int(input("Digite o ID do produto que deseja atualizar: "))

    nome = input("Novo nome: ")
    categoria = input("Nova categoria: ")
    quantidade = int(input("Nova quantidade: "))
    preco = float(input("Novo preço: ").replace(",", "."))

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE produtos SET nome = ?, categoria = ?, quantidade = ?, preco = ? WHERE id = ?",
        (nome, categoria, quantidade, preco, id_produto)
    )
    conn.commit()
    conn.close()
    print("Produto atualizado com sucesso!")

# Função para excluir produto
def excluir_produto():
    listar_produtos()
    id_produto = int(input("Digite o ID do produto que deseja excluir: "))

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM produtos WHERE id = ?", (id_produto,))
    conn.commit()
    conn.close()
    print("Produto excluído com sucesso!")