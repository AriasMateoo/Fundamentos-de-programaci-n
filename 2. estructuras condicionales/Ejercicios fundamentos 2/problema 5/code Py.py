# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	duracion = float()
	costo = float()
	print("CALCULO DE COSTO DE LLAMADA")
	print("Introduzca la duracion de la llamada en minutos:")
	duracion = float(input())
	if duracion<=3:
		costo = 0.10
	else:
		costo = 0.10+((duracion-3)*0.05)
	print("El costo de la llamada es de: ",costo," euros.")

