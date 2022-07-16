#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void(polinomio(float * poli,float a,float b,float i, int g)){
	float x, suma=0;
	int y;
	for(y=g;y>=0;y--){
		if(*(poli+y)>0){
			printf("+%.2f x^%d ",*(poli+y),y);
		}else{
			printf("%.2f x^%d ",*(poli+y),y);
		}
	}
	for(x=a;x<=b;x+=i){
		for(y=0;y<=g;y++){
			suma+=*(poli+y)*pow(x,y);
		}
		printf("\nf(%.2f)=%.2f",x,suma);
		suma=0;
	}
}
int main(){
	int grado,x;
	float *Ptr,a,b,i,z;
	printf("\nIngresa a: ");
	scanf("%f",&a);
	printf("\nIngresa b: ");
	scanf("%f",&b);
	if(a>b){
		z=b;
		b=a;
		a=z;
	}
	printf("\nIngresa el grado de tu polinomio: ");
	scanf("%d",&grado);
	printf("\nIngresa el incremento: ");
	scanf("%f",&i);
	
	Ptr=(float *) malloc(grado+1 * sizeof(float));
	
	for(x=0;x<=grado;x++){
		printf("\nCoeficiente %d: ",x);
		scanf("%f",&*(Ptr+x));
	}
	
	polinomio(Ptr,a,b,i,grado);
	system("pause");
	return 0;
}
