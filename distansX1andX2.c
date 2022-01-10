/*
# Программа для нахождения 
# Растояния  между точками 
# по координатам х1 и х2 . 
*/
#include <stdio.h>

int modul(int * x1,int * x2);

int main() {
    
    int dist,x1,x2;
    
    scanf("%d%d",&x1,&x2);
    printf("%d",modul(&x1,&x2));
    
    return 0;
}

int modul(int * x1 ,int * x2)
{
   int dist = 0;
       
if(*x1<0 && *x2<0)
        if(*x2<*x1)
            return (dist = *x1 -(*x2));
        else
            return (dist = *x2 -(*x1));
else if( *x1 > 0 && *x2 > 0)
        if(*x1>*x2)
            return(dist = *x1 - *x2);
        else
            return (dist = *x2 - *x1);
else if(*x2<0)
        {
            *x2 = *x2 * -1;
            return dist = *x2 + *x1;
        }
     if(*x1<0)
        {    
         *x1 = *x1 * -1;   
         return dist = *x1 + *x2; 
        }
else
    ;
}