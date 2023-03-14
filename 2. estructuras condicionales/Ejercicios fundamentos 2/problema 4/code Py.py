# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# declaracion de varaiables
	nombre = str()
	horas = float()
	precio = float()
	salario = float()
	# area definicion de variables
	print("CALCULO DE SALARIOS")
	# area de entradas
	print("Introduzca el nombre del empleado:")
	nombre = input()
	print("Introduzca las horas trabajadas por semana:")
	horas = float(input())
	print("Introduzca el precio por hora:")
	precio = float(input())
	# area de procesos
	if horas<=40:
		salario = horas*precio
		print("El salario mensual de ",nombre," es de: ",salario)
	else:
		salario = (40*precio)+((horas-40)*precio*1.5)
		# area de salidas
		print("El salario mensual de ",nombre," es de: ",salario)
		print("----------------------")

