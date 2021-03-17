import sys
sys.path.append('../db/')
import banco
# Constantes
NAO = "nao e habitavel"
SIM = "Habitavel"

#######################
def validar(planetas):
	if type(planetas) != list:
		print(planetas)
		print("FIM DO PROCESSO")
		sys.exit()
	else:
		return planetas 

#########################################
def recuperaHZD(HZD,planetas):
	if HZD != 1:
		return NAO
	else:
		for caso in planetas:
			if caso[4] != 1:
				planetas.remove(caso)
		return planetas

########################################
def recuperaPClass(pClass, planetas):
	if pClass >3 or pClass <1:
		return  NAO
	else:
		for caso in planetas:
			if caso[7] >3 or caso[7]<1:
				planetas.remove(caso)

		return planetas

#######################################
def recupera_HZA(HZA, planetas, pos):
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
def recupera_HZC(HZC, planetas):
	planetas = recupera_HZA(HZC, planetas, 5) #eh o mesmo processo inicial portanto pode-se usar a funcao
	planetas = validar(planetas)
	for x in range(0,len(planetas)):
		planetas[x] += (abs(HZC-planetas[x][5]),)
	planetas = sorted(planetas, key= lambda planeta: planeta[-1])
	tamanho = len(planetas)
	if tamanho>10:
		filtro = len(planetas)%2
	else:
		filtro = 1
	for x in range(0,filtro):
		planetas.remove(planetas[-1])
	return planetas
###########################################
def recupera_ESI(ESI,planetas):
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
	planetas = validar(planetas)

	planetas = recuperaPClass(array["pClass"],planetas)
	planetas = validar(planetas)

	planetas = recupera_HZA(array["HZA"], planetas, 6)
	planetas = validar(planetas)

	planetas = recupera_HZC(array["HZC"], planetas)
	planetas = validar(planetas)

	planetas = recupera_ESI(array["ESI"], planetas)
	planetas = validar(planetas)

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
			print(SIM)
			print(resultados)
		elif resultados[0][2] == 0:
			if resultados[0][0] < (distancia_apv/len(aprovados)):
				print(NAO)
				print(resultados)
			else:
				print(SIM)
				print(planetas)
		else:
			if resultados[0][2] < (distancia_rej/len(rejeitados)):
				print(SIM)
				print(planetas)
			else:
				print(NAO)
				print(resultados)
	else:
		if planetas[0][8] ==1:
			print(SIM)
			print(planetas)
		else:
			print(NAO)
			print(planetas)
	
array = [("nome","Kepler-62e"), ("ESI",0.8), ("SPH",0.96), 
("HZD",1),("HZC",-0.6),("HZA",0.2),("pClass",2)]
array = dict(array)
recupera_caso(array)





