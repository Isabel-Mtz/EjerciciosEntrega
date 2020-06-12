#Programación  Lógica
#INTEGRANTES:
#Luna González Rocío 16590485
#Martinez Garcia Isabel 16590490
#Resolución del ejercicio numero 1 de mmp:
Base = [
	["Laura","Queretaro"],
	["Elena","Paris"],
	["Claudia","San Francisco"],
	["Queretaro","Mexico"],
	["Paris","Francia"],
	["San Francisco","EUA"],
	["Mexico","America"],
	["Francia","Europa"],
	["EUA","America"]
]
def buscar(F1,E1):
	if not F1:
		return []
	if len(F1):
		if E1 == F1[0][0]:
			return F1[0][1]
		else:
			return buscar(F1[1:],E1)

def esta (E1,E2):
	R = buscar(Base,E1)
	L = buscar(Base, R)
	if L == E2 or R == E2:
		return True
	S = buscar(Base, L)
	if S == E2:
		return True
	else:
		return False
print(esta("Elena","Europa"))
# true
# Alena no existe en los datos
print(esta("Laura","America"))
# true
print(esta("Laura","Europa"))
# false
print(esta("Queretaro","Mexico"))
# True
print(esta("Francia","America"))
# False