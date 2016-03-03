

/*******************************************************************************
  This program is used to change a runing process limits!

  such as:
	There is a bug on program A which is runing, but it started with core
	size 1K. How to coredump it?

	Yeah, processlimit can do it!
		#processlimit -p `pidof A` -c unlimited
		#kill -6 `pidof A`
	Bingo!
  
  Copyright(c) 2008-2013 

  This program is free software; you can redistribute it and/or modify it
  under the terms and conditions of the GNU General Public License,
  version 2, as published by the Free Software Foundation.

  This program is distributed in the hope it will be useful, but WITHOUT
  ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
  FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
  more details.

  You should have received a copy of the GNU General Public License along with
  this program; if not, write to the Free Software Foundation, Inc.,
  51 Franklin St - Fifth Floor, Boston, MA 02110-1301 USA.

  The full GNU General Public License is included in this distribution in
  the file called "COPYING".

  Version:  0.1

  Date: 2013-09-27 14:02:47 CST

  Contact Information:
  Tony <tingw.liu@gmail.com>
  Jiangxi Road 11, Qingdao, China. 
*******************************************************************************/




#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/time.h>
#include <sys/resource.h>
#include <stdlib.h>
#include <limits.h>
#include <getopt.h>


#define SYS_PRLIMIT 302

char option;
const char *options = "hc:d:f:p:n:s:";
const struct option long_options[] = {
	{"help", 0, NULL, 'h'},
	{"pid", 1, NULL, 'p'},
	{"core size", 1, NULL, 'c'},
	{"data seg size", 1, NULL, 'd'},
	{"file size", 1, NULL, 'f'},
	{"open files", 1, NULL, 'n'},
	{"stack size", 1, NULL, 's'},
	{NULL, 0, NULL, 0}
};

void help()
{
	printf("Usage: processlimit -p pid [-cdfns] [limit]\n");
	printf("\nIt is similar to ulimit which for running process," 
			"you can get param information from 'unlimit -a'!\n");
	printf("Caution: All value unit is 1 (blocks, bytes, files...)\n");
	printf("\n\nAny question to Tony <tingw.liu@gmail.com>\n");
	exit(-1);
}

int main(int argc, char **argv)
{
	unsigned int pid = 0;
	struct rlimit newlimit;
	long int value;
	char *softlimit;
	int ret, type = 0;
	int done = 0;
	opterr = 0;
	while ((option = getopt_long(argc, argv, options, long_options, NULL)) != -1)
	{
		switch (option)
		{
			case 'h':
				help();
				break;
			case 'p':
				pid = atoi(optarg);
				break;
			case 'c':
				softlimit = strdup(optarg);
				type = RLIMIT_CORE;
				++done;
				break;
			case 'd':
				softlimit = strdup(optarg);
				type = RLIMIT_DATA;
				++done;
				break;
			case 'f':
				softlimit = strdup(optarg);
				type = RLIMIT_FSIZE;
				++done;
				break;
			case 'n':
				softlimit = strdup(optarg);
				type = RLIMIT_NOFILE;
				++done;
				break;
			case 's':
				softlimit = strdup(optarg);
				type = RLIMIT_STACK;
				++done;
				break;
			default:
				help();
		}
	}
	if (pid == 0 || done != 1)
		help();

	if (strncmp(softlimit, "unlimited", strlen(softlimit)) == 0) {
		newlimit.rlim_cur = RLIM_INFINITY;
		newlimit.rlim_max = RLIM_INFINITY;
	} else {
		value =  strtol(softlimit, NULL, 10);
		if (value == LONG_MIN || value == LONG_MAX) {
			printf("Can't convert softlimit to long int\n");
			return -1;
		}
		newlimit.rlim_cur = value;
		newlimit.rlim_max = value;
	}
	free(softlimit);	
	//printf("pid=%d, type=%d, limit=%llu\n", pid, type, newlimit.rlim_cur);
	ret = syscall(SYS_PRLIMIT, pid, type, &newlimit, NULL);
	if (ret) {
		printf("Can't change softlimt and hardlimit!\n");
		return -1;
	}
}
