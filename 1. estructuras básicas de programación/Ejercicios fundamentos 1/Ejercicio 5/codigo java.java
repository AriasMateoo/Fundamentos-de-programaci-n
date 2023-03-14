/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "EJERCICIO_5.java."

import java.io.*;

public class ejercicio_5 {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		double bf;
		double fe;
		double i_total;
		double i_totales_diurno;
		double i_totales_nocturno;
		double rf;
		double sp;
		double s_diurno;
		double s_nocturno;
		System.out.println("s_diurno");
		s_diurno = Double.parseDouble(bufEntrada.readLine());
		System.out.println("s_nocturno");
		s_nocturno = Double.parseDouble(bufEntrada.readLine());
		System.out.println("SP");
		sp = Double.parseDouble(bufEntrada.readLine());
		System.out.println("BF");
		bf = Double.parseDouble(bufEntrada.readLine());
		System.out.println("RF");
		rf = Double.parseDouble(bufEntrada.readLine());
		System.out.println("FE");
		fe = Double.parseDouble(bufEntrada.readLine());
		System.out.println("I_totales_diurno");
		i_totales_diurno = Double.parseDouble(bufEntrada.readLine());
		System.out.println("I_totales_nocturno");
		i_totales_nocturno = Double.parseDouble(bufEntrada.readLine());
		s_diurno = i_totales_diurno-sp-bf-rf-fe;
		s_nocturno = i_totales_nocturno-sp-bf-rf-fe+40*14000000/100;
		System.out.println("el salario diurno es : "+s_diurno);
		System.out.println("el salario nocturno es : "+s_nocturno);
	}


}

