#include <stdio.h> 
 
struct process { 
    int pid;      // process ID 
    int at;       // arrival time 
    int bt;       // burst time 
    int priority; // priority (lower value = higher priority) 
    int wt;       // waiting time 
    int tat;      // turnaround time 
    int completed; // flag to check if process is done 
}; 
 
int main() { 
    int n, i, time = 0, completed = 0; 
    float total_wt = 0, total_tat = 0; 
    struct process p[20]; 
 
    printf("Enter total number of processes: "); 
    scanf("%d", &n); 
 
    printf("Enter Arrival Time, Burst Time, and Priority for each process:\n"); 
    for (i = 0; i < n; i++) { 
        p[i].pid = i + 1; 
        printf("P%d Arrival Time: ", i + 1); 
        scanf("%d", &p[i].at); 
        printf("P%d Burst Time: ", i + 1); 
        scanf("%d", &p[i].bt); 
        printf("P%d Priority: ", i + 1); 
        scanf("%d", &p[i].priority); 
        p[i].completed = 0; 
    } 
 
    printf("\nProcess\tArrival\tBurst\tPriority\tWaiting\tTurnaround\n"); 
 
    while (completed != n) { 
        int idx = -1; 
        int min_priority = 9999; 
 
        // Find process with highest priority that has arrived and not completed 
        for (i = 0; i < n; i++) { 
            if (p[i].at <= time && p[i].completed == 0) { 
                if (p[i].priority < min_priority) { 
                    min_priority = p[i].priority; 
                    idx = i; 
                } 
                // If priorities are equal, choose the one that arrived first 
                else if (p[i].priority == min_priority && p[i].at < p[idx].at) { 
                    idx = i; 
                } 
            } 
        } 
 
        if (idx != -1) { 
            // Calculate waiting time and turnaround time 
            p[idx].wt = time - p[idx].at; 
            if (p[idx].wt < 0) p[idx].wt = 0; // handle idle CPU time 
            time += p[idx].bt; 
            p[idx].tat = p[idx].wt + p[idx].bt; 
            p[idx].completed = 1; 
            completed++; 
 
            printf("P%d\t%d\t%d\t%d\t\t%d\t%d\n", 
                   p[idx].pid, p[idx].at, p[idx].bt, p[idx].priority, 
                   p[idx].wt, p[idx].tat); 
 
            total_wt += p[idx].wt; 
            total_tat += p[idx].tat; 
        } else { 
            // No process has arrived yet, increment time 
            time++; 
        } 
    } 
    printf("\nAverage Waiting Time = %.2f", total_wt / n); 
    printf("\nAverage Turnaround Time = %.2f\n", total_tat / n); 
    return 0; 
} 
 
