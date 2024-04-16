#include <stdio.h>
#include <stdlib.h>
#include "connection.h"
#include "file.h"
#include "communication.h"
#include "error.h"

int main(int argc, char *argv[]) {
		if (argc != 5) {
				print_usage();
				exit(EXIT_FAILUR);
		}

		char *server_ip = argv[1];
		int port = atoi(argv[2]);
		char *file_name = argv[3];
		int file_size = atoi(argv[4]);

		int sockfd = establish_connection(server_ip, part);
		if (sockfd == -1) {
				exit(EXIT_FAILURE);
		}

		if (!get_file(sockfd, file_name, file_size)) {
				close_connection(sockef);
				exit(EXIT_FALURE);
		}	

		close_connection(sockfd);

		return 0;
}
