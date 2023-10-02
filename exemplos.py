with open ('arquivo.txt', 'r') as arquivo:
    for linha in arquivo:
        print("-->" + linha)
#criando um arquivo novo
with open ('arquivo2.txt', 'w') as arquivo:
    arquivo.write('Milena, tem a mesma idade que Jose e Renan!\n')
    arquivo.write('Sera possivel?\n')

with open ('arquivo2.txt', 'r') as arquivo:
    for linha in arquivo:
        print("-->" + linha)
#adicionando linhas em um arquivo que existe
with open ('arquivo2.txt', 'a' ):
    arquivo.write('adicionando linha 3\n')
    arquivo.write('adicionando linha 4\n')


