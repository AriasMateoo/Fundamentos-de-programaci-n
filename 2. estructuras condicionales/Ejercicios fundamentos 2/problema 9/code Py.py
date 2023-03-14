# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# declaracion de variables
	num1 = int()
	num2 = int()
	num3 = int()
	# area de entrada
	print("num1")
	num1 = int(input())
	print("num2")
	num2 = int(input())
	print("num3")
	num3 = int(input())
	# area de procesos
	if num1>num2 and num1>num3:
		mayor = num1
	if num2>num1 and num2>num3:
		mayor = num2
	if num3>num2 and num2>num1:
		mayor = num3
	print("el numero mayor es:",mayor)

