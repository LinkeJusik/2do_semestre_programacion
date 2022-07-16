//poner en un arreglo los primero n número primos

#include<stdio.h>
#include <stdlib.h>
#include <math.h>

void primos(int n, int *m){
	int i,j,p=0,cont,*l;
	l=m;
	for(i=0;p<n;i++){
		cont=0;
		j=1;
		while(j<=i){
			if(i%j==0){
				cont++;
			}
			j++;
		}
		if(cont==2){
			*m++=i;
			p++;
		}
	}
	for(i=0;i<n;i++){
		if(i==0){
			printf("[%d, ",*l++);
		}else if(i<n-1){
			printf("%d, ",*l++);
		}else{
			printf("%d]",*l++);
		}

	}
}

int main(){
	int a,*c;
	
	printf("Ingrese cuantos número primos desea calcular: ");
	scanf("%d",&a);
	
	c=(int *) malloc(a*sizeof(int));
	
	primos(a,c);
	printf("\n\n");
	
	system("pause");
	return 0;
}
