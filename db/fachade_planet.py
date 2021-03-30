import sys
sys.path.append('../src/')
import insere_caso
import banco


print("inserir, ler, deletar, alterar")
frase = input("Digite a funcao que deseja:")

if frase == "inserir":
	nome = input("Digite o nome: ")
	ESI = input("Digite o ESI: ")
	SPH = input("Digite o SPH: ")
	HZD = input("Digite o HZD: ")
	HZC = input("Digite o HZC: ")
	HZA = input("Digite o HZA: ")
	pClass = input("Digite o pClass: ")
	habitalidade = input("Digite a habitalidade: ")
	print(banco.data_insert(nome,ESI, SPH, HZD, HZC, HZA, pClass,habitalidade))

elif frase == "ler":
	print("ESI, SPH, HZD, HZC, HZA, pClass, habitalidade")
	print(banco.data_read())

elif frase =="deletar":
	id = input("Digite o id desejado: ")
	banco.delete_data("id", id)

elif frase =="alterar":
	nome = raw_input("Digite o nome: ")
	ESI = input("Digite o ESI: ")
	SPH = input("Digite o SPH: ")
	HZD = input("Digite o HZD: ")
	HZC = input("Digite o HZC: ")
	HZA = input("Digite o HZA: ")
	pClass = input("Digite o pClass: ")
	habitalidade = input("Digite a habitalidade: ")
	id = input("Digite o id desejado: ")
	banco.data_update(nome, ESI, SPH, HZD, HZC, HZA, pClass,habitalidade, id)
