#include <stdio.h>
#include <stdlib.h>

#define MAX 5

void push(int);
int pop();
void palindrome();
void display();

int S[MAX];
int top = -1;

int main()
{
    int ch, item;

    while (1)
    {
        printf("\n1. Push\n2. Pop\n3. Palindrome\n4. Display\n5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &ch);

        switch (ch)
        {
        case 1:
            printf("Enter the element to be pushed: ");
            scanf("%d", &item);
            push(item);
            break;

        case 2:
            item = pop();
            if (item == -1)
                printf("Stack underflow");
            else
                printf("Element popped: %d", item);
            break;

        case 3:
            palindrome();
            break;

        case 4:
            display();
            break;

        case 5:
            return 0;

        default:
            printf("Invalid Choice");
        }
    }
    return 0;
}

void push(int n)
{
    if (top == MAX - 1)
    {
        printf("Stack Overflow");
        return;
    }
    top++;
    S[top] = n;
}

int pop()
{
    int ele;
    if (top == -1)
        return -1;

    ele = S[top];
    top--;
    return ele;
}

void palindrome()
{
    int i, flag = 1;

    for (i = 0; i <= top / 2; i++)
    {
        if (S[i] != S[top - i])
            flag = 0;
    }

    if (flag == 1)
        printf("It is a palindrome");
    else
        printf("It is not a palindrome");
}

void display()
{
    int i;

    if (top == -1)
    {
        printf("Stack underflow");
        return;
    }

    for (i = top; i >= 0; i--)
        printf("\n%d", S[i]);
}