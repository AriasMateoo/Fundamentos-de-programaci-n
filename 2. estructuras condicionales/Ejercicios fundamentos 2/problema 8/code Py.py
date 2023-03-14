# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Pedimos los valores de los coeficientes
	print("Ingresa el valor de A:")
	a = float(input())
	print("Ingresa el valor de B:")
	b = float(input())
	print("Ingresa el valor de C:")
	c = float(input())
	# Calculamos el discriminante
	disc = b**2-4*a*c
	# Verificamos si la ecuación tiene solución
	if disc<0:
		print("La ecuación no tiene solución.")
	else:
		# Calculamos las raíces
		raizdisc = raiz_cuadradadisc
		x1 = (-b+raizdisc)/(2*a)
		x2 = (-b-raizdisc)/(2*a)
		# Mostramos las raíces
		print("Las raíces son:")
		print("x1 =",x1)
		print("x2 =",x2)

