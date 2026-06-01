#include <stdio.h>

#define MAX 100

int main( )
{
    int n, i, j;
    int graph[MAX][MAX];
    int indegree[MAX] = {0};
    int visited[MAX] = {0};
    int count = 0;

    printf("Enter number of vertices: ");
    scanf("%d", &n);

    printf("Enter adjacency matrix:\n");

    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            scanf("%d", &graph[i][j]);
        }
    }
    
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            if (graph[i][j] == 1)
            {
                indegree[j]++;
            }
        }
    }

    printf("\nTopological Ordering:\n");

    while (count < n)
    {
        int found = 0;

        for (i = 0; i < n; i++)
        {
            if (indegree[i] == 0 && !visited[i])
            {
                printf("%d ", i);

                visited[i] = 1;
                found = 1;
                count++;

                
                for (j = 0; j < n; j++)
                {
                    if (graph[i][j] == 1)
                    {
                        indegree[j]--;
                    }
                }
            }
        }

        /* Cycle detection */
        if (!found)
        {
            printf("\nGraph contains cycle. Topological sort not possible.\n");
            return 1;
        }
    }

    return 0;
}
