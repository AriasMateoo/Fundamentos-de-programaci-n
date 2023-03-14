# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	v_inicial = int()
	v_final = int()
	tiempo = int()
	aceleracion = int()
	print("v_final")
	v_final = int(input())
	print("v_inicial")
	v_inicial = int(input())
	print("tiempo")
	tiempo = int(input())
	aceleracion = v_final-v_inicial
	aceleracion = aceleracion/tiempo
	print("la aceleracion es : ",aceleracion)

