#include<stdio.h>
void main()
{
 int a[100],i,j,pos,n,swap;
 printf("Enter the limit:");
 scanf("%d",&n);
 for(i=0;i<n;i++)
    scanf("%d",&a[i]);
 for(i=0;i<n-1;i++)
 {
     pos=i;
     for(j=i+1;j<n;j++)
     {
        if(a[pos]>a[j])
        {
            pos=j;
        }
     }
     if(pos!=i)
     {
         swap=a[i];
         a[i]=a[pos];
         a[pos]=swap;

     }
 }
 for(i=0;i<n;i++)
    printf("%d ",a[i]);
}
