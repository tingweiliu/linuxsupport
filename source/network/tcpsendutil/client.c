#include "util.h"
#include <errno.h>

void help()
{
	printf("Usage:tcpclient <IP address> <IP port> <packet size> <delay>\n");
	printf("Send a packet with size <packet size> every <delay> microsends to <IP address>:<IP port>\n");
	printf("\nAny questions and sponsors to <tingw.liu@gmail.com>\n");
	exit(-1);
}

int main(int argc,char **argv)
{
	int sockfd;
	int keepalive = 1;
	struct sockaddr_in servaddr;
	int count;
	if (argc != 5)
		help();
	if ((sockfd = socket(AF_INET, SOCK_STREAM, 0)) == -1)
		err_quit("socket error");
	bzero(&servaddr, sizeof(servaddr));
	servaddr.sin_family = AF_INET;
	servaddr.sin_port = htons(atoi(argv[2]));
	inet_pton(AF_INET, argv[1], &servaddr.sin_addr);
	setsockopt(sockfd, SOL_SOCKET, SO_KEEPALIVE, &keepalive, sizeof(keepalive));
	if (connect(sockfd, (struct sockaddr*)&servaddr, sizeof(servaddr)) == -1)
		err_quit("connect error errno=%d", errno);
	str_cli(sockfd, atoi(argv[3]), atoi(argv[4]));
	exit(0);
}
