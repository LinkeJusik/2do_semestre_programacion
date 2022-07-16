#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void moda(int *m,int *m2, int n){
	int x,y,cont,moda,aux;
	
	for(x=0;x<n;x++){
		cont=0;
		for(y=0;y<n;y++){
			if(*(m+x)==*(m+y)){
				cont++;
			}
		}
		*(m2+x)=cont;
	}
	
	for(y=0;y<n;y++){
		for(x=0;x<n-1;x++){
			if(*(m2+x)>*(m2+(x+1)) ){
				
				aux=*(m2+x);
				*(m2+x)=*(m2+(x+1));
				*(m2+(x+1))=aux;
				
				aux=*(m+x);
				*(m+x)=*(m+(x+1));
				*(m+(x+1))=aux;

			}
		}
	}
	
	if(*(m2+n-*(m2+n-1)-1)==*(m2+n-1)){
		printf("\nHay varios valores que se pueden conciderar moda, ya que %d y %d se repiten el mismo número de veces (%d veces)",*(m+n-2),*(m+n-1),*(m2+n-1));
	}else{
		printf("\nLa moda es %d repiriendose %d veces",*(m+n-1),*(m2+n-1));
	}

}

int main(){
	int n,*ptr,*ptr2,x;
	printf("Calcularemos la moda de un arreglo de números\nIngresa el número de elementos que deseas introducir: ");
	scanf("%d",&n);
	
	ptr=(int *) malloc(n*sizeof(int));
	ptr2=(int *) malloc(n*sizeof(int));
	
	for(x=0;x<n;x++){
		printf("Introduce tu elemento número %d: ",x+1);
		scanf("%d",&*(ptr+x));
	}
	
	for(x=0;x<n;x++){
		printf("%d, ",*(ptr+x));
	}
	
	moda(ptr,ptr2,n);
	
}
