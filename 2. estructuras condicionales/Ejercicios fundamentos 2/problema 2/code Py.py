# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Declaración de variables
	numero = float()
	suma = float()
	contador = int()
	# Inicialización de variables
	suma = 0
	contador = 0
	# Entrada de datos
	print("Ingrese una serie de números positivos. Ingrese 0 para terminar.")
	numero = float(input())
	# Procesamiento de datos
	while numero!=0:
		if numero>0:
			suma = suma+numero
			contador = contador+1
		numero = float(input())
	# Cálculo de la media
	if contador>0:
		media = suma/contador
		print("La media de la serie de números positivos es: ",media)
	else:
		print("No se ingresaron números positivos.")

