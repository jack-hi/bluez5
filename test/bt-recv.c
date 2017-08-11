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

#define SOCK_FL "/tmp/bt.sock"

int main(int argc, char **argv)
{
	int fd, clifd, len, i;
	struct sockaddr_un un;
	char buf[100], *pb, *pa;

	fd = socket(AF_UNIX, SOCK_STREAM, 0);
	unlink(SOCK_FL);

	memset(&un, 0, sizeof(un));
	un.sun_family = AF_UNIX;
	strcpy(un.sun_path, SOCK_FL);
	len = offsetof(struct sockaddr_un, sun_path) \
		  + strlen(SOCK_FL);
	bind(fd, (struct sockaddr *)&un, len);
	listen(fd, 5);
	len = sizeof(un);
	clifd = accept(fd, (struct sockaddr *)&un, &len);
	while (1) {	
		memset(buf, 0, sizeof(buf));
		if ( 0 == read(clifd, buf, 100))
			break;

		pb = buf;
		for (i = 0; i < 3; i ++) { /* 0: Address 1: Name 2: RSSI */
			pa = (char *)strchrnul(pb, '&');
			*pa = 0;
			printf("%d: %s\t", strlen(pb), pb);
			pb = pa + 1;
		}	
		printf("\n");
	}
	close(clifd);
	close(fd);
	return 0;
}

