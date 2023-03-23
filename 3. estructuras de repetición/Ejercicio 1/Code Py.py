# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# descripcion:programa que lee una ecuacion lineal y la resuleve
	# version:1.0
	# desarrollado por:Mateo Arias
	# fecha:28/02/23
	# area de definicion de variables
	a = float()
	b = float()
	# area de entrada
	print("digite el valor de a")
	a = float(input())
	print("digite el valor de b")
	b = float(input())
	# area de Proceso 
	if a!=0:
		x = -1*b/a
		print("la solucion de la ecuacion es:",x)
		if b==0:
			# area de salidas
			print("la ecuacion no tiene solucion")
	else:
		print("solucion indeterminada")

