#include<stdio.h>
#include<stdlib.h>
#include<iostream>
using namespace std;

class Profesor{
	private:
		string nombre, materia;
		int semestre;
	public:
		Profesor(string,string,int);
		void presentacion();
};

Profesor::Profesor(string _nombre,string _materia,int _semestre){
	nombre= _nombre;
	materia= _materia;
	semestre= _semestre;
}

void Profesor::presentacion(){
	cout<<"El profesor "<<nombre<<" imparte la materia de "<<materia<<" en el semestre n\243mero "<<semestre<<" de la Ingenieria Matematica de ESFM"<<endl;
}

int main(){
	
	Profesor mor("Moreno","Calculo",2);
	Profesor cis("Cisneros","Introducci\242n a la ingenier\241a",2);
	Profesor zam("Felidios","Algebra",2);
	Profesor esc("Escamilla","Matematicas discretas",2);
	Profesor crz("Rogelio","Programaci\242n",2);
	Profesor pac("Paco","Depresi\242n",1000);
	
	mor.presentacion();
	cis.presentacion();
	zam.presentacion();
	esc.presentacion();
	crz.presentacion();
	pac.presentacion();
	
	system("Pause");
	return 0;	
}
