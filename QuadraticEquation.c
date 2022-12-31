#include <stdio.h>

 float sqr_x1_x2(float a, float b, float c);
 float my_pow(float num, float step);
 int   my_sqrt(int disc);

 int main()
{
    float a,b,c;
    

    puts("Enter Сoefficients \n");
    scanf("%f%f%f", &a, &b, &c);

    sqr_x1_x2(a,b,c);
}

 float  sqr_x1_x2(float a, float b, float c)
{
    float disc, x_1, x_2;

    
    disc = my_pow(b,2) - (4*a*c);
    if(disc < 0)
        return(puts("Corneu Net!!!"));
    
    if(disc > 0 && 2*a != 0)
    {
        x_1 = (-b + my_sqrt(disc))/(2*a);
        x_2 = (-b - my_sqrt(disc))/(2*a);
        return(printf(" x_1 ~= %.2f \n x_2 ~= %.2f", x_1, x_2));
    }
    
    if(disc == 0 && 2*a != 0)
        return(printf("x_1 = %.2f",x_1 = -b/(2*a)));
    
    puts("Delenie na 0 -> ERROR");
}

 float  my_pow(float num, float step)
{
    float res = 1;
    for(int i = 1; i <= step; i++)
        res *= num;
    return(res);
}

 int    my_sqrt(int disc)
{
    int temp = 0, x = 1;

    if(disc < 0)
        disc = -disc;
    while(temp != x)
    {
        temp = disc/x ;
        if(temp == x)
            return x;
        x++;
    }
}
