import math
import sys
sys.path.append('db/')
import banco
def inserir_caso_novo(nome, ESI,HZD, HZC,HZA,pClass, habitalidade):
	banco.data_insert(nome, ESI, 0.0, HZD, HZC, HZA, pClass, habitalidade)
	print("Nome do planeta: %s"%(nome))
	print("ESI do planeta: %f"%(ESI))
	print ("Dentro da zona habitavel" if HZD == 1 else "Fora da zona habitavel")
	print("HZC do planeta: %f"%(HZC))
	print("HZA do planeta: %f"%(HZA))
	print("pClass do planeta: %i"%(pClass))
	print ("Habitavel" if habitalidade == 1 else "Nao habitavel")