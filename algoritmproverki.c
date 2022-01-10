#include <stdio.h>
#include <unistd.h>
#define N 1000

float method(int a, int b);

int main()
{
    for(int i = 4,j = 3; i <= N; i++,j++)
    {
        printf("%d/%d = %.14f\n",i,j,method(i,j));    
    }
            
}

float method(int a, int b)
{
    float resul, itog ,otnoshenie ;

    otnoshenie = a - b ;
    resul = otnoshenie / b ; 
    itog = otnoshenie + resul ;
    
    return(itog);
}