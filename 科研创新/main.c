
#include<stdio.h>
int main()
{
    int k=100;
    if(k>50){
        printf("k>50\n");
        
    }else{
        printf("k<50\n");
       
    }

    int i, n, f;
    scanf("%d",&n);
   
    n=5;
    i = 2;
    f = 1;
    while (i <= n)
    {
        f = f * i;
        i = i + 1;
    }
    printf("½×³ËÎª%d\n",f);
   
}