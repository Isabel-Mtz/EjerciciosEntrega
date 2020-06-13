#INTEGRANTES:
#Luna González Rocío 16590485 y Martinez Garcia Isabel 16590490
Requisitos = {
	"Oracle","SQL/PL","Linux","Unix","Shell","C++",
	"Proc*C","TuxedoV12", "VB6", "Java","WebServices","MicroServicios"
} 

print(Requisitos)
print("Para saber si usted es candidato al trabajo, escriba si o no segun su experiencia")
def Candidato():
	LEG1 = input("\n Oracle BBDD   : ").upper()
	LEG2 = input(" SQL y PL/SQL  : ").upper()
	LEG3 = input(" Linux         : ").upper()
	LEG4 = input(" Unix          : ").upper()
	LEG5 = input(" Shell (Linux - Unix) : ").upper()
	LEG6 = input(" C++           : ").upper()
	LEG7 = input(" Proc*C        : ").upper()
	LEG8 = input(" TuxedoV12     : ").upper()
	LEG9 = input(" VB6           : ").upper()
	LEG10 = input(" Java          : ").upper()
	LEG11 = input(" WebServices   : ").upper()
	LEG12 = input(" MicroServicios: ").upper()
	Exp = set()
	if LEG1 == "SI":
		Exp.add("Oracle")
	if LEG2 == "SI":
		Exp.add("SQL/PL")
	if LEG3 == "SI":
		Exp.add("Linux")
	if LEG4 == "SI":
		Exp.add("Unix")
	if LEG5 == "SI":
		Exp.add("Shell")
	if LEG6 == "SI":
		Exp.add("C++")
	if LEG7 == "SI":
		Exp.add("Proc*C")
	if LEG8 == "SI":
		Exp.add("TuxedoV12")
	if LEG9 == "SI":
		Exp.add("VB6")
	if LEG10 == "SI":
		Exp.add("Java")
	if LEG11 == "SI":
		Exp.add("WebServices")
	if LEG12 == "SI":
		Exp.add("MicroServicios")
	Difes = Requisitos - Exp
	interseccion = Requisitos & Exp
	print("\nExperiencia del candidato  es: ",Exp)
	print("\nHabilidades que  faltan reforsar son: ",Difes)
	Req = len(Requisitos)
	ExpU = len(interseccion)
	ReqMinimos = Req - 4
	if ExpU >= ReqMinimos:
		return "\nFelicidades es candidato"
	else:
		return "\nLo siento mucho NO es candidato"

print(Candidato())