#include <stdio.h>
#include <stdlib.h>
void convert();
void push(char);
char pop();
int priority(char);
char s[50];
int top = -1;
void push(char operand)
{
    if (top == 49)
    {
        printf("Stack Overflow\n");
        exit(1);
    }
    top++;
    s[top] = operand;
}
char pop()
{
    if (top == -1)
    {
        printf("Stack Underflow\n");
        exit(1);
    }
    return s[top--];
}
int priority(char operator)
{
    switch (operator)
    {
        case '(': return 0;
        case '+':
        case '-': return 1;
        case '*':
        case '/':
        case '%': return 2;
        case '^': return 3;
    }
    return -1;
}
void convert()
{
    char temp, symbol, postfix[50], infix[50];
    int i, j = 0;

    printf("Enter the infix expression: ");
    scanf("%s", infix);

    for (i = 0; infix[i] != '\0'; i++)
    {
        symbol = infix[i];

        switch (symbol)
        {
            case '(':
                push(symbol);
                break;

            case ')':
                while ((temp = pop()) != '(')
                {
                    postfix[j++] = temp;
                }
                break;

            case '+':
            case '-':
            case '*':
            case '/':
            case '%':
            case '^':
                while (top != -1 && priority(s[top]) >= priority(symbol))
                {
                    postfix[j++] = pop();
                }
                push(symbol);
                break;

            default:
                postfix[j++] = symbol;
        }
    }

    while (top != -1)
    {
        postfix[j++] = pop();
    }

    postfix[j] = '\0';

    printf("The postfix expression is: %s\n", postfix);
}

int main()
{
    convert();
    return 0;
}
