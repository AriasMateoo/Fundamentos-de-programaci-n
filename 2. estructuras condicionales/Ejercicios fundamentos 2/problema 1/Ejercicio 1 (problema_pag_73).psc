Algoritmo problema_pag_73
	// Declaración de variables
	Definir nombre Como Caracter
	Definir horasTrabajadas Como Entero
	Definir impuesto Como Real
	Definir salarioNeto Como Real
	Definir salarioBruto Como Real
	// Entrada de datos
	Escribir 'Ingrese el nombre del trabajador: '
	Leer nombre
	Escribir 'Ingrese el número de horas trabajadas: '
	Leer horasTrabajadas
	// Cálculo del salario bruto
	salarioBruto <- horasTrabajadas*10000
	// Cálculo del impuesto a pagar
	impuesto <- salarioBruto*0.25
	// Cálculo del salario neto
	salarioNeto <- salarioBruto-impuesto
	// Salida de datos
	Escribir 'El salario bruto de ',nombre,' es: ',salarioBruto
	Escribir 'El impuesto a pagar es: ',impuesto
	Escribir 'El salario neto de ',nombre,' es: ',salarioNeto
FinAlgoritmo
