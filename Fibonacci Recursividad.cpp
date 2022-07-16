#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int Fibonacci(int n){
	if(n==0){
		return 0;
	}else if(n==1){
		return 1;
	}else{
		return Fibonacci(n-1) + Fibonacci(n-2);
	}
}

int main(){
	int a;

	printf("Introduce el n'simo número de Fibonacci que deseas calcular: ");
	scanf("%d",&a);

	if(a<0){
		printf("Necesito un número positivo, por el amor de dios");
	}else{
		printf("El elemento n\243mero %d de Fibonacci es: %d",a,Fibonacci(a));
	}
	printf("\n\n");
	system ("pause");
	return 0;
}
