 
#include <windows.h> 
#include <stdio.h> 
 
int main() 
{ 
    HANDLE hPipe; 
    char buffer[128]; 
    DWORD dwRead; 
 

    hPipe = CreateNamedPipe( 
        TEXT("\\\\.\\pipe\\MyPipe"), 
        PIPE_ACCESS_INBOUND,           
        PIPE_TYPE_BYTE | PIPE_WAIT,  
        1,                    
        0,                     
        0,                    
        0,                        
        NULL);                 
 
    if (hPipe == INVALID_HANDLE_VALUE) { 
        printf("CreateNamedPipe failed. Error code: %ld\n", GetLastError()); 
        return 1; 
    } 
 
    printf("Waiting for writer to connect...\n"); 
    ConnectNamedPipe(hPipe, NULL); 
 
    
    ReadFile(hPipe, buffer, sizeof(buffer), &dwRead, NULL); 
    printf("Data received from writer: %.*s\n", (int)dwRead, buffer); 
 
    
    CloseHandle(hPipe); 
    printf("Reader process finished.\n"); 
 
    return 0; 
} 
 
 
