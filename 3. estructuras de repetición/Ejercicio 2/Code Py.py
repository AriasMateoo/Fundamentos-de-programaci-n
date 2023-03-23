# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# DESCRIPCION
	# enunciado: calcula de la nomina de un empleado
	# desarrollado por: Mateo Arias
	# version: 1.0
	# fecha:06/03/23
	# AREA DE DECLARACION DE VARIABLES
	v_nomemp = str()
	v_horsemtra = int()
	v_valhor = int()
	v_valhorext = int()
	v_valimp = float()
	v_suebase = float()
	v_suepag = float()
	v_valhornor = int()
	# AREA DE INICIALIZACION DE VARIABLES
	v_nomemp = ""
	v_horsemtra = 0
	v_valhorext = 0
	v_valimp = 0.0
	v_suebase = 0.0
	v_suepag = 0.0
	v_valhornor = 0
	# AREA DE LECTURAS
	print("digite nombre del empleado:")
	v_nomemp = input()
	print("Digite las horas trabajadas semanales:")
	v_horsemtra = int(input())
	print("digite el valor de la hora trabajada:")
	v_valhor = int(input())
	# AREA DE PROCESOS
	if v_horsemtra<35:
		v_suebase = v_horsemtra*v_valhor
	else:
		v_suebase = 35*v_valhor+(v_horsemtra-35)*v_valhor*1.5
	if v_suebase>=300000 and v_suebase<=400000:
		v_valimp = v_suebase*0.20
	else:
		if v_suebase>400000:
			v_valimp = v_suebase*0.30

