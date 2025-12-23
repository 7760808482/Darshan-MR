#include<stdio.h>
#include<window.h>
int main()
{
	HANDLE hPIPE;
	CHAR BUFFER[128];
	dword DWrEAD;
	hPipe=CreateNamedPipe(
	TEXT_ACCESS_INBOUND,
	PIPE_TYPE_BYDE |PIPE_WAIT,
	1,
	0,
	0,
	0,
	NULL);
	
	if(hPipe==INVALD_HANDLE_VALUE){
		printf("CreateNamedPipe failed>Error code:%d\n",GetlastError());
		return 1;
	}
	printf("Waiting for writer to connect...\n");
	ConnectNamedPipe(hPipe,NULL);
	READfILE(HpIPE,BUFFER,SIZEOF(BUFFER),&DWrEAD,null);
	PRINTF("dATA RECEVIE FROM WRITER:%*s\n",(int)dwRead,buffer);
	CloseHandle(hPipe);
	printf("Reader procrss finished\n");
	return 0;
}