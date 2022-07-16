#include <stdio.h>
#include <stdlib.h>
#include <math.h>
void vectores(float *v1,float *v2,int n){
	int x,y=0;
	for(x=0;x<n;x++){
		if(*(v1+x) != *(v2+x)){
			y=1;
		}
	}
	if(y==0){
		printf("Son iguales\n");
	}else{
		printf("Tienen la misma longitud, pero no son iguales UnU\n");
	}
}

int main(){
	float *ptr1,*ptr2,s=0,s1=0;
	int n,n2,x;
	printf("Ingrese el tamaño de su primer vector\n");
	scanf("%d",&n);
	printf("Ingresa el tamaño de su segundo vector\n");
	scanf("%d",&n2);
	printf("\n");
	
	ptr1=(float *) malloc(n*sizeof(float));
	ptr2=(float *) malloc(n2*sizeof(float));
	
	for(x=0;x<n;x++){
		printf("Ingrese su primer vector \n");
		scanf("%f",&*(ptr1+x));
		s+=(pow(*(ptr1+x),2.0));
	}
	printf("\n");
	for(x=0;x<n2;x++){
		printf("Ingrese su segundo vector\n");
		scanf("%f",&*(ptr2+x));
		s1+=(pow(*(ptr2+x),2.0));
	}
	
	if(n==n2){
		vectores(ptr1,ptr2,n);
	} else if(s==s1){
		printf("No son iguales, pero tienen la misma norma de %f\n",sqrt(s));
	} else if(s>s1){
		printf("Tu primer vector tiene un norma mayor a la del segundo: %f\n",sqrt(s));
	} else {
		printf("Tu segundo vector tiene un norma mayor a la del primero: %f\n",sqrt(s1));
	}
	system ("pause");
	return 0;
}
