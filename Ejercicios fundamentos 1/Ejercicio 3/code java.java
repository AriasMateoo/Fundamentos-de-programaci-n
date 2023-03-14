/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "EJERCICIO_3.java."

import java.io.*;
import java.math.*;

public class ejercicio_3 {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		double aceleracion;
		double distancia;
		int tiempo;
		int v_final;
		int v_inicial;
		// area de documentacion
		// enunciado:leer velociad en metros sobre segundos y tiempo en segundos para hallar la aceleracion y el tiempo
		// version:1.0
		// desarrollado por:Mateo Arias
		// fecha:23/02/23
		// area definicion de variables 
		// area de entradas
		System.out.println("cual es la velocidad inicial");
		v_inicial = Integer.parseInt(bufEntrada.readLine());
		System.out.println("cual es la velocidad final");
		v_final = Integer.parseInt(bufEntrada.readLine());
		System.out.println("tiempo");
		tiempo = Integer.parseInt(bufEntrada.readLine());
		// area de procesos
		aceleracion = v_inicial+v_final/tiempo;
		distancia = v_inicial*tiempo+0.5*aceleracion*Math.pow(tiempo,2);
		// area de salidas
		System.out.println("la aceleracion es de:"+aceleracion);
		System.out.println("la distancia es:"+distancia);
	}


}

