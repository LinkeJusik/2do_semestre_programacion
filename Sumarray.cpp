#include <stdlib.h>
#include <math.h>
#include <stdio.h>

float sumarray(float *a,int n){
	int i;
	float sum=0;
	
	for(i=0;i<n;i++){
		sum+= *(a+i);
	}
	return sum;
}

int main(){
	int tam,x;
	float *ptr;
	
	printf("Ingresa el tamaño de tu arreglo: ");
	scanf("%d",&tam);
	
	printf("\n");
	ptr=(float *)malloc(tam*sizeof(float));
	
	for(x=0;x<tam;x++){
		printf("Introduce un valor en tu arreglo: ");
		scanf("%f",&*(ptr+x));
	}
	
	for(x=0;x<tam;x++){
		if(x==0){
			printf("[%.2f, ",*(ptr+x));
		}else if(x==tam-1){
			printf("%.2f]",*(ptr+x));
		}else{
			printf("%.2f, ",*(ptr+x));
		}
	}
	
	printf("\nLa suma de los elementos en tu arreglo es %.2f\n\n",sumarray(ptr,tam));
	
	system("pause");
	return 0;
}
