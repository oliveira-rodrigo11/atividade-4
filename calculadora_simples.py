# Função para realizar a operação
def realizar_operacao(num1, num2, operacao):
    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2
    elif operacao == "*":
        return num1 * num2
    elif operacao == "/":
        if num2 == 0:
            return "Erro: Divisão por zero!"
        else:
            return num1 / num2
    else:
        return "Operação inválida!"

# Laço para garantir que o programa continue pedindo até uma operação válida
while True:
    try:
        # Solicita os números ao usuário
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        # Solicita a operação desejada
        operacao = input("Digite a operação desejada (+, -, *, /): ")

        # Realiza a operação e exibe o resultado
        resultado = realizar_operacao(num1, num2, operacao)
        
        # Verifica se a operação foi válida e exibe o resultado
        if resultado == "Operação inválida!" or resultado == "Erro: Divisão por zero!":
            print(resultado)  # Exibe a mensagem de erro
        else:
            print(f"O resultado de {num1} {operacao} {num2} é: {resultado}")
            break  # Encerra o loop após uma operação válida
    except ValueError:
        print("Erro: Entrada inválida! Por favor, insira números válidos.")
