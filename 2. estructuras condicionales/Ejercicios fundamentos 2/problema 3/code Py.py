# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# DECLARACION DE VARIABLES
	i = int()
	suma = int()
	# inicializacion de varaiables
	suma = 0
	for i in range(2,101,2):
		# area de procesos 
		suma = suma+i
	# area de salidas
	print("La suma de los numeros pares entre 2 y 100 es: ",suma)

