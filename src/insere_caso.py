import math
import sys
sys.path.append('db/')
import banco
def inserir_caso_novo(nome, ESI,HZD, HZC,HZA,pClass, habitalidade):
	banco.data_insert(nome, ESI, 0.0, HZD, HZC, HZA, pClass, habitalidade)