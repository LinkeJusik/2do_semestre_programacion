#include <stdio.h>
#include <stdlib.h>
#include <math.h>
void vectores(float *v1,float *v2,int n){
	int x,y=0,z,sum;
	for(x=0;x<n;x++){
		if(*(v1+x) != *(v2+x)){
			y=1;
		}
	}
	if(y==0){
		printf("\nSon iguales\n");
	}else{
		printf("\nNo son iguales UnU\n");
	}
	y=0;
	if(*(v1) > *(v2)){
		z=(*(v1) / *(v2));
		for(x=0;x<n;x++){
			if(*(v1+x) != (*(v2+x) *z)){
				y=1;
			}
		}
	}else{
		z=(*(v2) / *(v1));
		for(x=0;x<n;x++){
			if(*(v2+x) != (*(v1+x) *z)){
				y=1;
			}
		}	
	}
	
	if(y!=1){
		printf("\nSon colineales\n");
	}else{
		printf("\nNo son colineales UnU\n");
	}
	
	for(x=0;x<n;x++){
		sum+=(*(v1+x) * *(v2+x));
	}
	if(sum==0){
		printf("\nSon ortogonales\n");
	}else{
		printf("\nNo son ortogonales UnU\n");
	}
	
	printf("\nComo s\242lo tenemos dos vectores, tienen que ser coplanares\n");
	
}

int main(){
	float *Apu,*Apu2,s1=0,s2=0;
	int n1,n2,x;
	printf("Ingrese el tamaño de su primer vector\n");
	scanf("%d",&n1);
	printf("Ingresa el tamaño de su segundo vector\n");
	scanf("%d",&n2);
	printf("\n");
	
	Apu=(float *) malloc(n1*sizeof(float));
	Apu2=(float *) malloc(n2*sizeof(float));
	
	for(x=0;x<n1;x++){
		printf("Ingrese su primer vector \n");
		scanf("%f",&*(Apu+x));
		s1+=(pow(*(Apu+x),2.0));
	}
	printf("\n");
	for(x=0;x<n2;x++){
		printf("Ingrese su segundo vector\n");
		scanf("%f",&*(Apu2+x));
		s2+=(pow(*(Apu2+x),2.0));
	}
	
	if(n1==n2){
		vectores(Apu,Apu2,n1);		
	}else{
		printf("\nNo son iguales\nY como no tienen la misma longitud, no podemos compararlos para determinar si son colineales, ortogonales ni coplanares\n");
	}
	
	if(s1==s2){
		printf("\nTienen la misma norma de %f\n\n",sqrt(s1));
	} else if(s1>s2){
		printf("\nTu primer vector tiene un norma mayor a la del segundo: %f > %f\n\n",sqrt(s1),sqrt(s2));
	} else {
		printf("\nTu segundo vector tiene un norma mayor a la del primero: %f > %f\n\n",sqrt(s2),sqrt(s1));
	}
	system ("pause");
	return 0;
}
