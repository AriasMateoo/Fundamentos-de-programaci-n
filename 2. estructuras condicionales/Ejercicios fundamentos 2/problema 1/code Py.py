# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Declaración de variables
	nombre = str()
	horastrabajadas = int()
	impuesto = float()
	salarioneto = float()
	salariobruto = float()
	# Entrada de datos
	print("Ingrese el nombre del trabajador: ")
	nombre = input()
	print("Ingrese el número de horas trabajadas: ")
	horastrabajadas = int(input())
	# Cálculo del salario bruto
	salariobruto = horastrabajadas*10000
	# Cálculo del impuesto a pagar
	impuesto = salariobruto*0.25
	# Cálculo del salario neto
	salarioneto = salariobruto-impuesto
	# Salida de datos
	print("El salario bruto de ",nombre," es: ",salariobruto)
	print("El impuesto a pagar es: ",impuesto)
	print("El salario neto de ",nombre," es: ",salarioneto)

