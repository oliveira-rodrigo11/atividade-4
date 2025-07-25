import re  # Para usar expressões regulares

# Função para avaliar a força da senha
def avaliar_senha():
    while True:
        senha = input("Digite uma senha (ou 'sair' para encerrar): ").strip()

        # Encerra o programa se o usuário digitar "sair"
        if senha.lower() == "sair":
            print("Programa encerrado.")
            break

        # Verifica se a senha tem pelo menos 8 caracteres
        if len(senha) < 8:
            print("A senha é fraca. Ela deve ter pelo menos 8 caracteres.")
            continue

        # Verifica se a senha contém pelo menos um número
        if not re.search(r'\d', senha):
            print("A senha é fraca. Ela deve conter pelo menos um número.")
            continue

        # Se passou nas verificações, a senha é forte
        print("A senha é forte!")
        break

# Chama a função para avaliar a senha
avaliar_senha()
