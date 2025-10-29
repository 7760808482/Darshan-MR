#include <stdio.h>
#include<conio.h>
void stringmatch();
char str[100], pat[10], rep[10], res[100];
int a = 0, b = 0, c = 0, d = 0, e = 0, flag = 0;
void main()
{
    clrscr();

    printf("Enter the string: ");
    gets(str);

    printf("Enter the pattern: ");
    gets(pat);

    printf("Enter the replace: ");
    gets(rep);

    printf("\nOriginal string: %s", str);

    stringmatch();

    if (flag == 1)
        printf("\nNew string: %s", res);
    else
        printf("\nPattern not found %s", res);

    getch();
}

void stringmatch()
{
    while (str[a] != '\0')
    {
        if (str[b] == pat[c])
        {
            b++;
            c++;
            if (pat[c] == '\0')
            {
                flag = 1;
                for (d = 0; rep[d] != '\0'; d++)
                {
                    res[e] = rep[d];
                    e++;
                }
                c = 0;
                a = b;
            }
        }
        else
        {
            res[e] = str[a];
            e++;
            a++;
            b = a;
            c = 0;
        }
    }
    res[e] = '\0';
}