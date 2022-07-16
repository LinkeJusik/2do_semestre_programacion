#include<stdio.h>
#include<iostream>
#include<stdlib.h>
using namespace std;

class Rectangulo{
	private:
		int lado, ancho;
	public:
		Rectangulo(int,int);
		void area();
		void perimetro();
};

Rectangulo::Rectangulo(int _lado,int _ancho){
	lado= _lado;
	ancho= _ancho;
}

void Rectangulo::area(){
	cout<<"El area de tu rectangulo es "<<lado*ancho<<endl;
}

void Rectangulo::perimetro(){
	cout<<"El perimetro de tu rectangulo es "<<(2*lado)+(2*ancho)<<endl;
}

int main(){
	int a,b;
	printf("Introduce el lado de un rectangulo ");
	scanf("%d",&a);
	printf("Introduce el ancho de un rectangulo ");
	scanf("%d", &b);
	
	Rectangulo r1(a,b);
	r1.area();
	r1.perimetro();

	printf("\n\n");
	system("pause");
	return 0;
}
