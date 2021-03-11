#aqui vai ser posto o código para recuperação dos casos
import sys
sys.path.append('../db/')
import banco
NAO = "não é habitável"
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

def recuperaHZA(HZA, planetas):
	planetas_HZA = []
	for caso in planetas:
		if abs(HZA - caso[6]) <= 0.2 and (caso[6] > -1 or caso[6] <1):
			planetas_HZA.append(caso)
	if not planetas_HZA:
		for caso in planetas:
			if abs(HZA - caso[6]) <= 0.6 and (caso[6] > -1 or caso[6] <1):
				planetas_HZA.append(caso)
		if not planetas_HZA:
			return NAO
			
	planetas_HZA = sorted(planetas_HZA, key= 7)
	return planetas_HZA

def recupera_caso(array):
	planetas = banco.data_read()
	planetas =recuperaHZD(array[3], planetas)
	if type(planetas) != list:
		print(planetas)
		print("FIM DO PROCESSO")
		sys.exit()
	else:
		planetas = recuperaPClass(array[6],planetas)

	if type(planetas) != list:
		print(planetas)
		print("FIM DO PROCESSO-2")
	else:
		planetas = recuperaHZA(array[5], planetas)
		print(planetas)


array = ["KOI-3010.01", 0.84, 0.63, 1,-0.16,-0.06,2]
recupera_caso(array)




