#include <stdio.h>

void hanoi(int n, char s, char temp, char d)
{
    if (n == 1)
    {
        printf("Move disk 1 from %c to %c\n", s, d);
        return;
    }
    hanoi(n - 1,  temp,s,d);
    printf("Move disk %d from %c to %c\n", n, s, d);
    hanoi(n - 1,s,d, temp);
}

int main(void)
{
    int n;
    printf("Enter the number of disks: ");
    scanf("%d", &n);
    hanoi(n, 'A', 'B', 'C');
    return 0;
}