#Cristina Borges 08-Mar-18

arquivo = open("Data\iris.csv","r")
for linha in arquivo:
    coluna = linha.split(",")
    print(coluna[0], " ", " ", coluna[1], " ", coluna[2]," ", coluna[3])
arquivo.close