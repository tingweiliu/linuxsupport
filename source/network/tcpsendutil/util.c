#include "util.h"
void err_quit(char * fmt,...)
{
	char buf[MAXLINE+1];
	va_list ap;
	va_start(ap,fmt);
	vsnprintf(buf, sizeof(buf), fmt, ap);
	va_end(ap);
	fputs(buf,stdout);
	fputs("\n",stdout);
	exit(1);
}
void str_echo(int sockfd)
{
	ssize_t n;
	char line[MAXLINE];
	bzero(line, MAXLINE);
	while(1){
		if((n=read(sockfd,line,MAXLINE)) <= 0)
			return;
		printf("%s\n", line);
	}
}
void str_cli(int sockfd, int len, int delay)
{
	char *sendline;
	int n = 0;
	if (len < 0)
		err_quit("packet size should greater than zero!");
	sendline = malloc(len);
	while(1) {
		memset(sendline, '1', len);
		n = write(sockfd, sendline, len);
		printf("send %d bytes!\n", n);
		usleep(delay);
	}
}
