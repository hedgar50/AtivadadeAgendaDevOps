nome = str(input("Nome: "))
endereco = str(input("Endereço: "))
rua = str(input("Rua: "))
cep = str(input("CEP: "))
tel = str(input("Telefone: "))
print(nome, endereco, rua, cep, tel)

arq = open("agenda.txt", "w")
arq.writelines(nome + "\n" + endereco + "\n" + rua + "\n" + cep + "\n" + tel)
arq.close()

arq = open('agenda.txt', 'r')
arq.readlines = arq.read()
print()
arq.close()
