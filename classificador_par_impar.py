# Função principal para classificar números pares e ímpares
def classificar_numeros():
    pares = 0  # Contador de números pares
    impares = 0  # Contador de números ímpares
    
    while True:
        entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ").strip()

        # Encerra o programa se o usuário digitar "fim"
        if entrada.lower() == "fim":
            break

        try:
            # Tenta converter a entrada para inteiro
            numero = int(entrada)
            
            # Verifica se o número é par ou ímpar
            if numero % 2 == 0:
                print(f"{numero} é par.")
                pares += 1
            else:
                print(f"{numero} é ímpar.")
                impares += 1
                
        except ValueError:
            print("Erro: Entrada inválida! Por favor, insira um número inteiro ou 'fim' para encerrar.")

    # Exibe a quantidade total de números pares e ímpares informados
    print(f"\nTotal de números pares informados: {pares}")
    print(f"Total de números ímpares informados: {impares}")

# Chama a função para classificar os números
classificar_numeros()
