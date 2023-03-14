# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	s_diurno = float()
	s_nocturno = float()
	sp = float()
	bf = float()
	rf = float()
	fe = float()
	i_total = float()
	print("s_diurno")
	s_diurno = float(input())
	print("s_nocturno")
	s_nocturno = float(input())
	print("SP")
	sp = float(input())
	print("BF")
	bf = float(input())
	print("RF")
	rf = float(input())
	print("FE")
	fe = float(input())
	print("I_totales_diurno")
	i_totales_diurno = float(input())
	print("I_totales_nocturno")
	i_totales_nocturno = float(input())
	s_diurno = i_totales_diurno-sp-bf-rf-fe
	s_nocturno = i_totales_nocturno-sp-bf-rf-fe+40*14000000/100
	print("el salario diurno es : ",s_diurno)
	print("el salario nocturno es : ",s_nocturno)

