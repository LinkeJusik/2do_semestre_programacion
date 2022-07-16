#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
#include <string.h>
#include<iostream>
using namespace std;

class Persona{
	private: //atributos
		int edad;
		string nombre;
	public: //metodos
		Persona(int,string); //constructor
		void leer();
		void correr();
};

//constructor (inicializa los atributos)
Persona::Persona(int _edad, string _nombre){
	edad= _edad;
	nombre= _nombre;
}

void Persona::leer(){
	cout<<"Soy "<<nombre<<", tengo "<<edad<<" anios y estoy leyendo un libro"<<endl;
	//printf("Soy %c, tengo %d anios y estoy leyendo un libro\n",nombre,edad);
}
void Persona::correr(){
	cout<<"Soy "<<nombre<<", tengo "<<edad<<" anios y estoy corriendo de un banco"<<endl;
	//printf("Soy %c y estoy corriendo del banco\n",nombre);
}

int main(){
	Persona p1 = Persona(19,"Gabriel");
	Persona p2(19,"Maria");
	p1.leer();
	p2.correr();
	printf("Quiero pan xd\n\n");
	
	system("pause");
	return 0;
}
