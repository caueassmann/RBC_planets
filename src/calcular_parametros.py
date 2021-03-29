import math

#HZC funcoes
def rx_m(r1,k,m,m1,pos):##funcao que calcula as varivaveis rm de HZC
	p = k[0][pos]+(1/3.0)*math.log((m/m1[pos]),10)-k[1][pos]*(m/m1[pos])**k[2][pos]
	rx = r1[pos]*10**p
	return rx

def CalculaHZC(r, raio):#HZC = Habitable Zone Composition
	a = 2*raio -r[1] - r[0]
	b = r[1] - r[0]
	return a/b

#HZA funcoes
def ve_x(teq,mw,pos):#calcula as variaveis ve_x do HZA
	z = 2*10**-2
	return (z*teq)/mw[pos]

def CalculaHZA(v,raio,m):#HZA = Habitable Zone Atphomosfere
	a = 2*math.sqrt(m/raio)-v[1]-v[0]
	b = v[1] - v[0]
	return a/b

#HZD funcoes
def CalculaHZD(variaveis_HZD,au):# HZD = Habitable Zone Distance
	a = 2*au -variaveis_HZD[1] - variaveis_HZD[0]
	b = variaveis_HZD[1] - variaveis_HZD[0]
	return a/b

def lum_stellar(temp_estelar,raio_stellar):# calcula a luminosidade estelar
	area = 4*math.pi*raio_stellar**2* 5.67*10**-8
	temp_estelar = temp_estelar**4
	Sol =752129019.7746662
	return (temp_estelar*area)/Sol

def rx_s(ro,a,b,luminosidade,pos,e_stelar_t):#calcula a variavel rs de HZD
	Ts= e_stelar_t- 5700
	return (ro[pos]-a[pos]*Ts - b[pos]*(Ts)**2)*math.sqrt(luminosidade)

######FUNCAO PRINCIPAL########################
def calcular_parametros(m,raio,teq,raio_estelar,temp_estelar,au):
	#constantes HZC	
	variaveis_HZC = []
	k = [(-0.209490,-0.209396),(0.0804,0.0807),(0.394,0.375)] 
	r1 = [2.52,4.43]
	m1 = [5.8,5.52]

	#constante HZA
	mw = [14.0067,1.00784]
	variaveis_HZA = []

	#constantes HZD
	a = [2.7619*10**-5,1.3786*10**-4]
	b =[3.8095*10**-9, 1.4286*10**-9]
	ro = [0.72,1.77]
	AU = 206265
	variaveis_HZD = []

	luminosidade = lum_stellar(temp_estelar,raio_estelar)

	for x in range(0,2):
		rx = rx_m(r1,k,m,m1,x)
		variaveis_HZC.append(rx)
		veh = ve_x(teq,mw,x)
		variaveis_HZA.append(veh)
		rs = rx_s(ro,a,b,luminosidade,x,temp_estelar)
		variaveis_HZD.append(rs)

	################ HZC	
	HZC = CalculaHZC(variaveis_HZC, raio)

	################ HZA
	HZA = CalculaHZA(variaveis_HZA,raio,m)

	################# HZD
	HZD = CalculaHZD(variaveis_HZD,au)
	if HZD >-1 and HZD < 1:
		HZD = 1
	else:
		HZD = 0
	return [("HZC",HZC),("HZA",HZA),("HZD",HZD)]

