#include<stdio.h>
#include<stdlib.h>
struct node{
    int data;
    struct node *left ,*right;

};
struct node *root=NULL;
struct node *create(int val)
{
    struct node *new;
    new=(struct node*)malloc(sizeof(struct node));
    new->data=val;
    new->left=NULL;
    new->right=NULL;
    return new;
}
void insatend(int val)
{
    struct node *new,*current,*parent;
    new=create(val);
    current=root;
    parent=NULL;
    while(current!=NULL)
    {
        parent=current;
        if(current->data>val)
        {
        parent->left=new;}
    }
        else{
        parent->right=new;}

}
void inorder(struct node *temp)
{
    while(temp!=NULL)
    {
        inorder(temp->left);
        printf("%d",temp->data);
        inorder(temp->right);
    }
}
void preorder(struct node *temp)
{
    while(temp!=NULL)
    {
        printf("%d",temp->data);
        preorder(temp->left);
        preorder(temp->right);
    }
}
void postorder(struct node *temp)
{
    while(temp!=NULL)
    {
        postorder(temp->left);
        postorder(temp->right);
        printf("%d",temp->data);
    }
}
int main()
{
    int ch;
    while(1)
    {
        printf("1.Insert\n2.Inorder\n3.Preorder\n4.Postorder\n5.Exit\n");
        printf("Enter your choice:");
        scanf("%d",&ch);
        switch(ch)
        {
            case 1:
            {
                int val;
                printf("Enter the value to be inserted:");
                scanf("%d",&val);
                insatend(val);
                break;
            }
            case 2:
            {
                inorder(root);
                break;
            }
            case 3:
            {
                preorder(root);
                break;
            }
            case 4:
            {
                postorder(root);
                break;
            }
            case 5:
            {
                exit(0);
            }
            default:
            {
                printf("Invalid choice\n");
            }
        }
    }
}
