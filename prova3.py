#PROVA 3 DE LOGICA DE PROGRAMAÇÃO ALUNO: PEDRO NEGREIROS 

# Solicita ao usuário o número para o qual deseja ver a tabuada

numero = int(input("Digite um número inteiro de 1 a 10 para gerar a tabuada: "))



# Verifica se o número está dentro do intervalo  (1 a 10)

if 1 <= numero <= 10:

    print(f"Tabuada de {numero}:")



    # Loop de 1 a 10 para gerar a tabuada

    for i in range(1, 11):

        resultado = numero * i

        print(f"{numero} X {i} = {resultado}")

else:

    print("Número fora do intervalo permitido. Por favor, escolha um número")

