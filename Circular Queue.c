#include<stdio.h>
int size;
struct queue
{
    int a[30];
    int front;
    int rear;
};
void enqueue(struct queue *p)
{   int item;
    printf("Enter the item:");
    scanf("%d",&item);
    if(p->rear==-1)
    {


        p->rear++;
        p->front++;
        p->a[p->rear]=item;
    }
    else
    {
        int next;
        next=(p->rear+1)%size;
        p->a[++p->rear]=item;
        if(next!=p->front)
        {
            p->rear=next;
            p->a[p->rear]=item;
        }
        else
        {
            printf("Queue is full");

        }
    }
}
void dequeue(struct queue *p)
{
    if(p->front==-1)
    {
        printf("Queue is empty");
    }
    else
    {
        int item;
        item=p->a[p->front];
        printf("Deleted item=%d",item);
        if(p->rear==p->front)
        {
            p->front=-1;
            p->rear=-1;
        }
        else
        {
            p->front=(p->front+1)%size;
        }
    }
}

void display(struct queue *p)
{
    int i;
    printf("Circular queue");
    if(p->front>p->rear)
    {
        for(i=p->front;i<=size-1;i++)
            printf("%d",p->a[i]);
        for(i=0;i<p->rear;i++)
            printf("%d",p->a[i]);
    }
    else
    {
        for(i=p->front; i<=p->rear; i++)
        {
            printf("%d ",p->a[i]);
        }
        printf("\n");
    }
}
void main()
{
    int ch,t=1;
    struct queue q;
    q.front=-1;
    q.rear=-1;
    printf("Enter the size:");
    scanf("%d",&size);
    while(t==1)
    {
        printf("Enter the choice\n 1.ENQUEUE\n 2.DEQUEUE\n");
        scanf("%d",&ch);
        switch(ch)
        {
        case 1:
            enqueue(&q);
            display(&q);
            break;
        case 2:
            dequeue(&q);
            display(&q);
            break;

        default:
            printf("Invalid choice\n");
        }
        printf("\nDo you want to continue \n1.yes 2.no\n");
        scanf("%d",&t);
    }

}
