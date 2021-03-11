import sys
sys.path.append('../db/')
import banco
NAO = "nao e habitavel"
def validar(planetas):
	if type(planetas) != list:
		print(planetas)
		print("FIM DO PROCESSO")
		sys.exit()
	else:
		return planetas 
def recuperaHZD(HZD,planetas):
	if HZD != 1:
		return NAO
	else:
		for caso in planetas:
			if caso[4] != 1:
				planetas.remove(caso)
		return planetas

def recuperaPClass(pClass, planetas):
	if pClass >3 or pClass <1:
		return  NAO
	else:
		for caso in planetas:
			if caso[7] >3 or caso[7]<1:
				print(caso)
				planetas.remove(caso)
		return planetas

def recupera_HZA(HZA, planetas, pos):
	planetas_HZA = []
	for caso in planetas:
		if abs(HZA - caso[pos]) <= 0.2 and (caso[pos] > -1 or caso[pos] <1):
			planetas_HZA.append(caso)
	if not planetas_HZA:
		for caso in planetas:
			if abs(HZA - caso[pos]) <= 0.6 and (caso[pos] > -1 or caso[pos] <1):
				planetas_HZA.append(caso)
		if not planetas_HZA:
			return NAO
	return planetas_HZA

def recupera_HZC(HZC, planetas):
	planetas = recupera_HZA(HZC, planetas, 5) #eh o mesmo processo inicial portanto pode-se usar a funcao
	planetas = validar(planetas)
	for x in range(0,len(planetas)):
		planetas[x] += (abs(HZC-planetas[x][5]),)
	planetas = sorted(planetas, key= lambda planeta: planeta[-1])
	return planetas


def recupera_caso(array):
	planetas = banco.data_read()

	planetas =recuperaHZD(array["HZD"], planetas)
	planetas = validar(planetas)

	planetas = recuperaPClass(array["pClass"],planetas)
	planetas = validar(planetas)

	planetas = recupera_HZA(array["HZA"], planetas, 6)
	planetas = validar(planetas)

	planetas = recupera_HZC(array["HZC"], planetas)
	planetas = validar(planetas)


	for planeta in planetas:
		print(planeta)
		print("=======================================")
	

array = [("nome","Kepler-62e"), ("ESI",0.83), ("SPH",0.96), 
("HZD",1),("HZC",-0.15),("HZA",0.28),("pClass",3)]
array = dict(array)
recupera_caso(array)





