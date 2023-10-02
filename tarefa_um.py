numeros = int (input("Quantos numeros deseja digitar?: "))

with open ('numeros.txt', 'w') as arquivo:
    for n in range(numeros):
        num = (input("Digite o numero: "))
        arquivo.write (f"{num}\n")

with open ('numeros.txt', 'r') as arquivo:
    soma = 0
    quantidade = 0
    for linha in arquivo:
        num = int (linha)
        soma = soma + num
        quantidade += 1
    media = soma / quantidade    
    print(media)
