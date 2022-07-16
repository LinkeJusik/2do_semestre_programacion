#include<stdio.h>

float Multi(float s,int n){
	if(n==0 && s>=0){
		return 0;
	}else if(n>0 && s>=0){
		return s + Multi(s,n-1);
	}else if(s<0){
		return -1* Multi(-s,n);
	}else{
		printf("El número de veces que deseas sumar tiene que ser natural ");
		return 0;
	}
}

int main(){
	int n;
	float s;
	
	printf("Inserta un número que desees sumar n veces: ");
	scanf("%f",&s);
	printf("Inserta el número de veces que desees sumarlo: ");
	scanf("%d",&n);
	
	printf("%.2f",Multi(s,n));
	
	return 0;	
}
