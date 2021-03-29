import sys
sys.path.append('src/')
import insere_caso
import calcular_parametros
import recupera_caso

def habitalidade(m,raio,teq,raio_estelar,temp_estelar,au, nome, ESI):
	Hs = calcular_parametros.calcular_parametros(m,raio,teq,raio_estelar,temp_estelar,au)
	Hs = dict(Hs)

	#verificar classe planetaria
	if m > 10:
		pClass = 4
	elif m > 5:
		pClass = 3
	elif m > 0.5:
		pClass = 2
	elif m > 0.1:
		pClass = 1
	else:
		pClass = 0

	array = [("nome", nome),("ESI", ESI), ("SPH", 0.0),("HZD",round(Hs["HZD"],2)),("HZC",round(Hs["HZC"],2)),("HZA",round(Hs["HZA"],2)),("pClass",pClass)]
	array = dict(array)
	resposta = recupera_caso.recupera_caso(array)
	hab = resposta
	if type(resposta) != int:
		hab = resposta[0]
	insere_caso.inserir_caso_novo(array["nome"],array["ESI"],array["HZD"],array["HZC"],array["HZA"],array["pClass"],hab)
	return (array, resposta)

#######################



