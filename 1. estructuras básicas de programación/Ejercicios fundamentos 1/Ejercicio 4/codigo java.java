/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "EJERCICIO_4.java."

import java.io.*;

public class ejercicio_4 {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		int aceleracion;
		double tiempo;
		int v_final;
		int v_inicial;
		System.out.println("v_final en m/s");
		v_final = Integer.parseInt(bufEntrada.readLine());
		System.out.println("v_inicial");
		v_inicial = Integer.parseInt(bufEntrada.readLine());
		System.out.println("aceleracion");
		aceleracion = Integer.parseInt(bufEntrada.readLine());
		tiempo = v_final-v_inicial;
		tiempo = tiempo/aceleracion;
		System.out.println("el tiempo es : "+tiempo);
	}


}

