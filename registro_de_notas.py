# Função principal para registrar as notas e calcular a média
def registrar_notas():
    notas = []  # Lista para armazenar as notas válidas
    while True:
        try:
            # Solicita a nota ou a palavra "fim" para encerrar
            entrada = input("Digite uma nota (ou 'fim' para encerrar): ").strip().lower()
            
            if entrada == "fim":
                break  # Sai do loop quando o usuário digitar "fim"
            
            # Converte a entrada para float e verifica se a nota está no intervalo válido
            nota = float(entrada)
            
            if 0 <= nota <= 10:
                notas.append(nota)  # Adiciona a nota à lista
            else:
                print("Erro: A nota deve estar entre 0 e 10!")
        
        except ValueError:
            print("Erro: Entrada inválida! Por favor, insira uma nota válida ou 'fim' para encerrar.")
    
    if notas:  # Verifica se há notas registradas
        media = sum(notas) / len(notas)
        print(f"\nMédia da turma: {media:.2f}")
        print(f"Total de notas válidas registradas: {len(notas)}")
    else:
        print("\nNenhuma nota válida foi registrada.")

# Chama a função para rodar o programa
registrar_notas()
