/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo deber�a llamarse "EJERCICIO_1.java."

import java.io.*;

public class ejercicio_1 {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		int aceleracion;
		int tiempo;
		int v_final;
		int v_inicial;
		System.out.println("v_final");
		v_final = Integer.parseInt(bufEntrada.readLine());
		System.out.println("v_inicial");
		v_inicial = Integer.parseInt(bufEntrada.readLine());
		System.out.println("tiempo");
		tiempo = Integer.parseInt(bufEntrada.readLine());
		aceleracion = v_final-v_inicial;
		aceleracion = aceleracion/tiempo;
		System.out.println("la aceleracion es : "+aceleracion);
	}


}

