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
	if pClass >3 or pClass<1:
		return  NAO
	else:
		for caso in planetas:
			if caso[7] >3 or caso[7]<1:
				print(caso)
				planetas.remove(caso)
		return planetas


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
		print(planetas)
		print("continua...")


array = ["KOI-3010.01", 0.84, 0.63, 1,-0.16,-0.06,2]
recupera_caso(array)




