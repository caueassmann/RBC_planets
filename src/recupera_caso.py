import sys
sys.path.append('db/')
import banco
# Constantes
NAO = 0
SIM = 1
SEMREGISTRO = "Não registrado"

#######################
#def validar(planetas, valor):
#	if type(planetas) != list:
#		return
#	else:
#		return planetas 

#########################################
def recuperaHZD(HZD,planetas):# apenas verifica se esta dentro da zona
	if HZD != 1:
		return NAO
	else:
		for caso in planetas:
			if caso[4] != 1:
				planetas.remove(caso)
		return planetas

########################################
def recuperaPClass(pClass, planetas):#apenas verifica a classe de massa dos planetas e remove os que sao muito grandes ou pequenos
	if pClass >3 or pClass <1:
		return  NAO
	else:
		for caso in planetas:
			if caso[7] >3 or caso[7]<1:
				planetas.remove(caso)

		return planetas

#######################################
def recupera_HZA(HZA, planetas, pos):# filtra os planetas que possuem uma diferenca de HZA  proxima e nao sao muito densos ou rarefeitos
	planetas_HZA = []
	for caso in planetas:
		if abs(HZA - caso[pos]) <= 0.4 and (caso[pos] > -1 or caso[pos] <1):
			planetas_HZA.append(caso)
	if not planetas_HZA:
		for caso in planetas:
			if abs(HZA - caso[pos]) <= 0.6 and (caso[pos] > -1 or caso[pos] <1):
				planetas_HZA.append(caso)
		if not planetas_HZA:
			return NAO
	return planetas_HZA

########################################
def recupera_HZC(HZC, planetas):#processo similar ao anterior, porém ocorre uma filtragem dependendo do tamanho da lista
	planetas = recupera_HZA(HZC, planetas, 5) #eh o mesmo processo inicial portanto pode-se usar a funcao
	if type(planetas) != list:
		return (planetas,SEMREGISTRO)
	for x in range(0,len(planetas)):
		planetas[x] += (abs(HZC-planetas[x][5]),)
	planetas = sorted(planetas, key= lambda planeta: planeta[-1])
	tamanho = len(planetas)
	if tamanho>10:
		filtro = len(planetas)%2
	elif tamanho>3:
		filtro = 1
	else:
		filtro = 0
	for x in range(0,filtro):
		planetas.remove(planetas[-1])
	return planetas
###########################################
def recupera_ESI(ESI,planetas):#verifica uma similaridade minima de 0.4 e prioriza ESI mais altos
	if ESI<0.4:
		return NAO
	planetas = sorted(planetas, key = lambda planeta: planeta[2])
	tamanho = len(planetas)
	if tamanho>10:
		filtro = len(planetas)%2
	elif tamanho>5:
		filtro = 3
	else:
		filtro = 0
	for x in range(0,filtro):
		planetas.remove(planetas[-1])
	return planetas
##########################################
def recupera_caso(array):
	planetas = banco.data_read()#id,nome,ESI,SPH(vai ser tirado),HZD,HZC,HZA,pClass, habitalidade(int)
	#filtragem
	planetas =recuperaHZD(array["HZD"], planetas)
	if type(planetas) != list:
		return (planetas,SEMREGISTRO)

	planetas = recuperaPClass(array["pClass"],planetas)
	if type(planetas) != list:
		return (planetas,SEMREGISTRO)

	planetas = recupera_HZA(array["HZA"], planetas, 6)
	if type(planetas) != list:
		return (planetas,SEMREGISTRO)

	planetas = recupera_HZC(array["HZC"], planetas)
	if type(planetas) != list:
		return (planetas,SEMREGISTRO)

	planetas = recupera_ESI(array["ESI"], planetas)
	if type(planetas) != list:
		return (planetas,SEMREGISTRO)

	#vizinho mais proximo
	if len(planetas)>1:#caso seja uma lista
		resultados = []
		for planeta in planetas: #determina distancia
			ESI = abs(planeta[2]-array["ESI"])*4
			HZC = abs(planeta[5]-array["HZC"])*2
			HZA = abs(planeta[6]-array["HZA"])*2
			pClass = abs(planeta[7]-array["pClass"])
			total = ESI + HZC + HZA + pClass
			planeta = (total,planeta[1],planeta[8])
			resultados.append(planeta)

		resultados = sorted(resultados)
		rejeitados = []
		aprovados = []
		distancia_apv = 0
		distancia_rej = 0

		for distancia in resultados:#separar habitaveis e nao habitaveis
			if distancia[2] == 0:
				distancia_rej +=distancia[0]
				rejeitados.append(distancia)
			else:
				distancia_apv +=distancia[0]
				aprovados.append(distancia)
		#determinacao
		if len(aprovados)>=len(rejeitados) and resultados[0][2] == 1:
			resposta_absoluta = SIM
		elif len(aprovados) == 0:
			resposta_absoluta = NAO
		elif resultados[0][2] == 0:
			if resultados[0][0] < (distancia_apv/len(aprovados)):
				resposta_absoluta = NAO
			else:
				resposta_absoluta = SIM
		else:
			if resultados[0][2] < (distancia_rej/len(rejeitados)):
				resposta_absoluta = SIM
			else:
				resposta_absoluta = NAO
	else:
		if planetas[0][8] ==1:
			resposta_absoluta = SIM
		else:
			resposta_absoluta = NAO
			
	#verifica planeta mais proximo
	if resultados:
		planeta_prox = resultados[0][1]
	elif planetas:
		planeta_prox = planeta[0][1]
	else:
		planeta_prox = SEMREGISTRO


	return (resposta_absoluta,planeta_prox)


