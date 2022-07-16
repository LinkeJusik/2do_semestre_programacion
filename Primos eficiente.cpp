#include<stdio.h>

int main(){
	int n, i, j, cont, aux=0;
	
	printf("Ingrese el la cantidad de n\243meros primos que desee calcular: ");
	scanf("%d",&n);
	
	for(i=0;aux<n;i++){
		cont=0;
		j=1;
		while(j<=i/2){
			if(i%j==0){
				cont++;
			}
			j++;
		}
		if(cont==1){
			aux++;
			printf("%d es el elemento n\243mero %d de los primos\n",i,aux);
		}
	}
	return 0;
}
