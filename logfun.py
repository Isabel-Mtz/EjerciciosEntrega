"""
#INTEGRANTES:
#Luna González Rocío 16590485 y Martinez Garcia Isabel 16590490
#Resolución del ejercicio numero 1 de mmp:
	https://www.computrabajo.com.mx/ofertas-de-trabajo/oferta-de-trabajo-de-desarrollador-batch-exp-sistemas-abiertos-en-queretaro-601BC72F6CEBB0F761373E686DCF3405
	En una empresa solicitan Lic./Ing. en Sistemas, Computación o afín.
	con los siguientes requisitos:
	• Oracle BBDD
	• SQL y PL/SQL
	• Linux
	• Unix
	• Shell (Linux - Unix)
	• C++, Proc*C y Tuxedo V12 o anteriores
	• Visual Basic 6.0
	• Java (Frameworks) , Web Services y Micro Servicios APIs
Realizar un programa que realice preguntas al usuario y que apartir de sus respuestas evalue si es cadidato o no
	(usen conjuntos)
"""
Requisitos = {
	"Oracle","SQL/PL","Linux","Unix","Shell","C++",
	"Proc*C","TuxedoV12", "VB6", "Java","WebServices","MicroServicios"
} 

print(Requisitos)
print("Para saber si usted es candidato al trabajo, escriba si o no segun su experienciaen el lenguaje")
def Candidato():
	1 = input("\n Oracle BBDD   : ").upper()
	2 = input(" SQL y PL/SQL  : ").upper()
	3 = input(" Linux         : ").upper()
	4 = input(" Unix          : ").upper()
	5 = input(" Shell (Linux - Unix) : ").upper()
	6 = input(" C++           : ").upper()
	7 = input(" Proc*C        : ").upper()
	8 = input(" TuxedoV12     : ").upper()
	9 = input(" VB6           : ").upper()
	10 = input(" Java          : ").upper()
	11 = input(" WebServices   : ").upper()
	12 = input(" MicroServicios: ").upper()
	Exp = set()
	if 1 == "SI":
		Exp.add("Oracle")
	if 2 == "SI":
		Exp.add("SQL/PL")
	if 3 == "SI":
		Exp.add("Linux")
	if 4 == "SI":
		Exp.add("Unix")
	if 5 == "SI":
		Exp.add("Shell")
	if 6 == "SI":
		Exp.add("C++")
	if 7 == "SI":
		Exp.add("Proc*C")
	if 8 == "SI":
		Exp.add("TuxedoV12")
	if 9 == "SI":
		Exp.add("VB6")
	if 10 == "SI":
		Exp.add("Java")
	if 11 == "SI":
		Exp.add("WebServices")
	if 12 == "SI":
		Exp.add("MicroServicios")
	Difes = Requisitos - Exp
	interseccion = Requisitos & Exp
	print("\nExperiencia del candidato  es: ",Exp)
	print("\nHabilidades que  faltan reforsar son: ",Difes)
	Req = len(Requisitos)
	ExpU = len(interseccion)
	ReqMinimos = Req - 3
	if ExpU >= ReqMinimos:
		return "\nFelicidades es candidato"
	else:
		return "\nLo siento mucho NO es candidato"

print(Candidato())
