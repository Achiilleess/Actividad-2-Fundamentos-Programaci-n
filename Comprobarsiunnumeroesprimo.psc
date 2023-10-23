
//iniciamos un Proceso 
Proceso Comprobarsiunnumeroesprimo
	//definimos variables
	Definir n, iteracion, limite Como Entero;
	Definir resultado, R Como Real;
	Definir primo Como Logico;
	//solicitamos variables
	Escribir "Ingrese numero: ";
	Leer n;
	//asignamos valor a las variables
	iteracion <- 3;
	Si n > 1 Entonces
		Si n mod 2 = 0 Entonces
			Escribir n, " no es primo";
		SiNo
			Si n > 100000000 Entonces
				R <- RC(n)
			FinSi
			primo <- Verdadero;
			Para iteracion <- 3 Hasta RC(R) Con Paso 2 Hacer
				resultado <- n mod iteracion;
				Si resultado = 0 Entonces
					primo <- Falso;
				FinSi
			Fin Para
			Si primo = Verdadero Entonces
				Escribir n, " es primo";
			SiNo
				Escribir n, " no es primo";
			FinSi
		FinSi
	SiNo
		Escribir n, " no es un numero primo porque ningun numero menor a 1 lo es";
	FinSi
	
FinProceso
	
