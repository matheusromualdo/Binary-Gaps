try:
    # Pede um número para o usuário
    N = int(input("Digite um numero: "))
    
    # Função que calcula o maior número de zeros consecutivos no binário de N
    def solution(N):
        # Converte o número para binário e remove o prefixo '0b'
        binario = bin(N)[2:] 
        
        # Variáveis para contagem de zeros consecutivos
        cont = 0 
        cont2 = 0 

        # Percorre cada dígito do número binário
        for i in binario:
            # Se o dígito for "0", incrementa o contador de zeros consecutivos
            if i == "0":
                cont += 1
            # Se o dígito for "1", compara o contador de zeros com o maior encontrado até o momento
            elif i == "1":
                cont2 = max(cont2, cont)
                cont = 0  # Reseta o contador de zeros

        # Imprime o maior número de zeros consecutivos encontrados
        print(cont2)

    # Chama a função para processar o número N
    solution(N)

except ValueError:
    # Caso o usuário não digite um número inteiro, exibe uma mensagem de erro
    print("Digite um numero inteiro!")
