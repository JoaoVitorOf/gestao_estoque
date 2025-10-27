from database import initialize_db # Aqui importamos a função initialize_db() que está no arquivo database.py, esse código vai usar a função que cria o banco e a tabela produtos.
from controle_estoque import cadastrar_produto, listar_produtos, atualizar_produto, excluir_produto # Aqui estamos importando 4 funções do controle_estoque

# Inicializa o banco de dados
initialize_db()

# Função do menu principal e todas opções visiveis para o usuário 
def menu():
    while True:
        print("\n--- Sistema de Gestão de Estoque ---")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Atualizar produto")
        print("4 - Excluir produto")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            atualizar_produto()
        elif opcao == "4":
            excluir_produto()
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Executa o menu e garante que o código dentro só execute quando o arquivo for o principal
if __name__ == "__main__":
    menu()