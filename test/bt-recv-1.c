/*
 * TEMPLATE main.c
 */
#include <stdio.h>
#include <stdlib.h>

#define _GNU_SOURCE
#include <string.h>

#include <sys/un.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <stddef.h>
#include <unistd.h>

#define SOCK_FL "/tmp/bt-server.sock"

int main(int argc, char **argv)
{
	int fd,len, i;
	struct sockaddr_un un;
	char buf[100], *pb, *pa;

	fd = socket(AF_UNIX, SOCK_STREAM, 0);

	memset(&un, 0, sizeof(un));
	un.sun_family = AF_UNIX;
	strcpy(un.sun_path, SOCK_FL);
	if (-1 == connect(fd, (struct sockaddr *)&un, sizeof(un)))
		printf("Connected failed\n");

	printf("Connect: %d\n", fd);

	while (1) {	
		memset(buf, 0, sizeof(buf));
		if ( 0 == read(fd, buf, 100))
			break;

		printf("\t %s \n", buf);
	}
	close(fd);
	return 0;
}

