#include "util.h"
#include <errno.h>
#include <signal.h>
#include <sys/wait.h>
void delchild(int signum)
{
	pid_t pid;
	int stat;
	while ((pid = waitpid(-1, &stat, WNOHANG)) > 0)
		printf("child %d terminated!\n",pid);
	return;
}
int main(int argc, char **argv)
{
	int listenfd, connfd, opt=1;
	pid_t childpid;
	socklen_t clilen;
	struct sockaddr_in cliaddr, servaddr;
	if (argc != 2) {
		err_quit("Usage: %s listenport", argv[0]);
	}
	if ((listenfd = socket(AF_INET, SOCK_STREAM, 0)) == -1)
		err_quit("socket error");
	bzero(&servaddr, sizeof(servaddr));
	servaddr.sin_family = AF_INET;
	servaddr.sin_addr.s_addr = htonl(INADDR_ANY);
	servaddr.sin_port = htons(atoi(argv[1]));
	setsockopt(listenfd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));
	if (bind(listenfd, (struct sockaddr*)&servaddr, sizeof(servaddr)) == -1)
		err_quit("bind error");
	if (listen(listenfd, 300) == -1)
		err_quit("listen error");
	signal(SIGCHLD, delchild);
	clilen = sizeof(cliaddr);
	while(1) {
		if ((connfd = accept(listenfd, (struct sockaddr*)&cliaddr, &clilen)) < 0) {
			if(errno==EINTR)
				continue;
			else
				err_quit("accept error");
		}
		if ((childpid = fork()) == 0) {
			close(listenfd);
			str_echo(connfd);
			exit(0);
		}
		close(connfd);
	}
}
