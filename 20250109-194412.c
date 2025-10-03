#include<stdio.h>
void main()
{
float marks,percentage;
char name[50];
printf("enter your name");
scanf("%s",&name);
printf("enter your marks");
scanf("%f",&marks);
percentage=marks/600*100;
printf("\n your percentage is %f",percentage);
if(marks<200)
printf("\n failed");
else
if(marks<=539)
printf("\n first class");
else
if(marks>=540)
printf("\n distinction");
}
    