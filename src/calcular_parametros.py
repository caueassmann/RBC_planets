import math
def rx_m(r1,k,m,m1,pos):
	p = k[0][pos]+(1/3.0)*math.log((m/m1[pos]),10)-k[1][pos]*(m/m1[pos])**k[2][pos]
	rx = r1[pos]*10**p
	return rx

def ve_x(teq,mw,pos):
	z = 2*10**-2
	return (z*teq)/mw[pos]

def HZC(r, raio):
	a = 2*raio -r[0] - r[1]
	b = r[0] - r[1]
	return a/b

def HZA(v,raio,m):
	a = 2*math.sqrt(m/raio)-v[1]-v[0]
	b = v[1] - v[0]
	return a/b

r = []
x =0
k = [(-0.209490,-0.209396),(0.0804,0.0807),(0.394,0.375)] 
r1 = [2.52,4.43]
m1 = [5.8,5.52]
mw = [14,1]

m  = input("m: ")
raio = input("raio: ")
teq =  input("teq: ")

rx = rx_m(r1,k,m,m1,0)
print(rx)
r.append(rx)
rx = rx_m(r1,k,m,m1,1)
print(rx)
r.append(rx)

HZC = HZC(r, raio)
print(HZC)

################
veh = ve_x(teq,mw,0)
vex = ve_x(teq,mw,1)
v = [veh, vex]
HZA = HZA(v,raio,m)
print(HZA)
