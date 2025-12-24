#include <stdio.h>
struct poly
{
    int coef;
    int exp;
    struct poly *link;
};

struct poly *p1 = NULL;
struct poly *p2 = NULL;
struct poly *Res = NULL;

struct poly* create(int c, int e)
{
    struct poly *new1;
    new1 = (struct poly*)malloc(sizeof(struct poly));
    new1->coef = c;
    new1->exp = e;
    new1->link = NULL;
    return new1;
}

void insatend(struct poly **head, int c, int e)
{
    struct poly *new1, *i;
    new1 = create(c, e);

    if (*head == NULL)
    {
        *head = new1;
        return;
    }
    else
    {
        i = *head;
        while (i->link != NULL)
        {
            i = i->link;
        }
        i->link = new1;
    }
}

void add()
{
    while (p1 != NULL && p2 != NULL)
    {
        if (p1->exp == p2->exp)
        {
            insatend(&Res, p1->coef + p2->coef, p1->exp);
            p1 = p1->link;
            p2 = p2->link;
        }
        else if (p1->exp > p2->exp)
        {
            insatend(&Res, p1->coef, p1->exp);
            p1 = p1->link;
        }
        else
        {
            insatend(&Res, p2->coef, p2->exp);
            p2 = p2->link;
        }
    }

    while (p1 != NULL)
    {
        insatend(&Res, p1->coef, p1->exp);
        p1 = p1->link;
    }

    while (p2 != NULL)
    {
        insatend(&Res, p2->coef, p2->exp);
        p2 = p2->link;
    }
}

void display(struct poly *head)
{
    if (head == NULL)
    {
        printf("0");
        return;
    }

    while (head != NULL)
    {
        printf("%dx^%d", head->coef, head->exp);
        if (head->link != NULL)
            printf("+");
        head = head->link;
    }
}

void main()
{
    
    clrscr();
    insatend(&p1, 3, 3);
    insatend(&p1, 4, 2);
    insatend(&p1, 3, 0);

    printf("\nPolynomial 1:");
    display(p1);

    insatend(&p2, 7, 3);
    insatend(&p2, 2, 1);
    insatend(&p2, 5, 0);

    printf("\nPolynomial 2:");
    display(p2);

    printf("\n");
    add();

    printf("\nAddition of two polynomials:\n");
    display(Res);
    getch();

}