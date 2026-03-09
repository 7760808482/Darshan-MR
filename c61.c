#include<stdio.h>
#include<stdlib.h>
#include<time.h>
void selectionSort(int a[],int n)
{
    int i,j,min,temp;
    for(i=0;i<n;i++)
    {
        min=i;
    for(j=i+1;j<n;j++)
    {
        if(a[j]<a[min])
        {
            min=j;
        }
    }
    if(min!=i)
    {
        a[i]=temp;
        temp=a[min];
        a[min]=a[i];
    }
}
}
int main()
{
    int *a;
    int i,n;
    clock_t start,end;
    double time_taken;
    printf("Enter the number of elements(n>5000):");
    scanf("%d",&n);
    a=(int*)malloc(n*sizeof(int));
    srand(time(0));
    for(i=0;i<n;i++)
    {
        a[i]=rand()%10000;
    }
    start=clock();
    selectionSort(a,n);
    end=clock();
    time_taken=(double)(end-start)/CLOCKS_PER_SEC;
    printf("The time taken to sort %d element is %f",n,time_taken);
    free(a);
    return 0;
}

