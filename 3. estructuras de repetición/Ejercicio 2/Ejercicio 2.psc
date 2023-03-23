Algoritmo sin_titulo
	//DESCRIPCION
	//enunciado: calcula de la nomina de un empleado
	//desarrollado por: Mateo Arias
	//version: 1.0
	//fecha:06/03/23
	
	//AREA DE DECLARACION DE VARIABLES
	definir v_nomEmp Como Caracter;
	definir v_horSemTra Como Entero;
	definir v_valHor como entero;
	Definir v_valHorExt como entero;
	Definir v_valImp como real;
	definir v_sueBase Como Real;
	definir v_suePag como real;
	definir v_valHorNor como entero;
	//AREA DE INICIALIZACION DE VARIABLES
	v_nomEmp="";
	v_horSemTra=0;
	v_valHorExt=0;
	v_valImp=0.0;
	v_sueBase=0.0;
	v_suePag=0.0;
	v_valHorNor=0;
	//AREA DE LECTURAS
	Escribir "digite nombre del empleado:";
	Leer v_nomEmp
	Escribir "Digite las horas trabajadas semanales:";
	leer v_horSemTra
	Escribir "digite el valor de la hora trabajada:";
	leer v_valHor
	//AREA DE PROCESOS
	si v_horSemTra < 35 Entonces
		v_sueBase=v_horSemTra*v_valHor;
	sino 
		v_sueBase=35*v_valHor+(v_horSemTra-35)*v_valHor*1.5
	FinSi
	si v_sueBase >= 300000  y v_sueBase <= 400000 Entonces
		v_valImp=v_sueBase*0.20
	sino 
		si v_sueBase> 400000 Entonces
			v_valImp=v_sueBase*0.30
		FinSi
	FinSi
	
	
	
	
	
FinAlgoritmo
