#include <stdio.h>
#include <stdlib.h>

int main()
{
    int *p, i, n;

    printf("Enter the number of elements: ");
    scanf("%d", &n);

    p = (int *)malloc(sizeof(int) * n);

    if (p == NULL)
    {
        printf("Memory not allocated");
        exit(0);
    }

    printf("Enter %d elements:\n", n);
    for (i = 0; i < n; i++)
    {
        scanf("%d", &p[i]);
    }

    printf("Entered elements are:\n");
    for (i = 0; i < n; i++)
    {
        printf("%d ", *(p + i));
    }

    free(p);   
    return 0;
}
