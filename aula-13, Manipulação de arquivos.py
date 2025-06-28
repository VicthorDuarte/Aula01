import csv
#Abrindo primeiro arquivo
with open ('primeiroarquivo.txt', 'w') as arquivo:
    arquivo.write('Linha1\n')
    arquivo.write('Linha\n')
#Lendo primeiro arquivo
with open('primeiroarquivo.txt', 'r') as arquivo:
    reader = arquivo.readlines()
    for linha in reader:
        print(linha.strip())

#Escrevendo arquivo .csv
with open('dados.csv', 'w', newline = '') as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(['Nome', 'Genero'])
    writer.writerow(['Alice','Feminino' ])
    writer.writerow(['Bob','Masculino'])
    writer.writerow(['Bruno','Masculino'])
    writer.writerow(['Roberta','Feminino'])

#Abrindo leitura de dados do arquivo .csv
with open('dados.csv', 'r') as arquivo:
    reader = csv.reader(arquivo)
    for linha in reader:
        print(linha)