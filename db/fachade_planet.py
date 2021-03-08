import banco
print("inserir, ler, deletar, alterar")
frase = input("Digite a função que deseja:")

if frase == "inserir":
	ESI = input("Digite o ESI: ")
	SPH = input("Digite o SPH: ")
	HZD = input("Digite o HZD: ")
	HZC = input("Digite o HZC: ")
	HZA = input("Digite o HZA: ")
	pClass = input("Digite o pClass: ")
	habitalidade = input("Digite a habitalidade: ")
	print(banco.data_insert(ESI, SPH, HZD, HZC, HZA, pClass,habitalidade))

elif frase == "ler":
	id = input("Digite o id desejado: ")
	print("ESI, SPH, HZD, HZC, HZA, pClass, habitalidade")
	print(banco.data_read())

elif frase =="deletar":
	id = input("Digite o id desejado: ")
	banco.deletar("id", id)

elif frase =="alterar":
	ESI = input("Digite o ESI: ")
	SPH = input("Digite o SPH: ")
	HZD = input("Digite o HZD: ")
	HZC = input("Digite o HZC: ")
	HZA = input("Digite o HZA: ")
	pClass = input("Digite o pClass: ")
	habitalidade = input("Digite a habitalidade: ")
	id = input("Digite o id desejado: ")
	banco.data_update(ESI, SPH, HZD, HZC, HZA, pClass,habitalidade, id)
