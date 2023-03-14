Algoritmo ejercicio_5
	//area de documentacion
	//enunciado:leer el salario de un empleado con sus respectivos descuentos
	//version:1.0
	//desarrollado por:Mateo Arias
	//fecha:23/02/23
	
	//area declaracion de variables
	Definir s_diurno,s_nocturno Como Real//variable de entrada que almacena el salario diurno, el salario nocturno y cada descuento
	//area de entrada
	Escribir 'cuales son sus ingresos totales diurnos'
	Leer s_diurno
	Escribir 'cuales son sus ingresos totales nocturnos sin el 40%'
	Leer s_nocturno
	//area de Proceso 
	s_diurno <- s_diurno-10*s_diurno/100-3*s_diurno/100-2*s_diurno/100-4*s_diurno/100
	s_nocturno <- s_nocturno-10*s_nocturno/100-3*s_nocturno/100-2*s_nocturno/100-4*s_nocturno/100+40*s_nocturno/100
	//area de salidas
	Escribir 'el salario diurno es : ',s_diurno
	Escribir 'el salario nocturno es : ',s_nocturno
FinAlgoritmo
