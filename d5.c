 
#include <windows.h> 
#include <stdio.h> 
 
int main() 
{ 
    HANDLE hPipe; 
    DWORD dwWritten; 
    char message[] = "Hi"; 
 
 
    printf("Waiting for reader process to connect...\n"); 
 
    
    hPipe = CreateFile( 
        TEXT("\\\\.\\pipe\\MyPipe"),   
        GENERIC_WRITE,                
        0,                            
        NULL,                        
        OPEN_EXISTING,                
        0,                          
        NULL);                     
 
    if (hPipe == INVALID_HANDLE_VALUE) { 
        printf("Failed to connect to pipe. Error code: %ld\n", GetLastError()); 
        return 1; 
    } 
 
    if (WriteFile(hPipe, message, sizeof(message), &dwWritten, NULL)) 
        printf("Data written to pipe: %s\n", message); 
    else 
        printf("WriteFile failed. Error code: %ld\n", GetLastError()); 
 
  
    CloseHandle(hPipe); 
    printf("Writer process finished.\n"); 
 
    return 0; 
} 