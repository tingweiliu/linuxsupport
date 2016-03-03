#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <string.h>
#include <stdarg.h>
#include <stdlib.h>
#define MAXLINE 100
void err_quit(char *fmt,...);
void str_echo(int sockfd);
