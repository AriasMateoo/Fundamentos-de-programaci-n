# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Declaraci�n de variables
	numero = float()
	suma = float()
	contador = int()
	# Inicializaci�n de variables
	suma = 0
	contador = 0
	# Entrada de datos
	print("Ingrese una serie de n�meros positivos. Ingrese 0 para terminar.")
	numero = float(input())
	# Procesamiento de datos
	while numero!=0:
		if numero>0:
			suma = suma+numero
			contador = contador+1
		numero = float(input())
	# C�lculo de la media
	if contador>0:
		media = suma/contador
		print("La media de la serie de n�meros positivos es: ",media)
	else:
		print("No se ingresaron n�meros positivos.")

