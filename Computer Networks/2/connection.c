#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include "error.h"

int establish_connection(const char *server_ip, int port) {
		int sockfd = socket(AF_INET, SOCK_DGRAM, O);
		if (sockfd == -1) {
				handle_error("");
				return -1;
		}

		// Ustalenie adresu i portu serwera
		struct sockaddr_in server_addr;
		server_addr.sin_family = AF_INET;
		server_addr.sin_port = htons(port);
		if (inet_pton(AF_INET, server_ip, &server_addr.sin_addr) != 1) {
				handle_error("Nieprawidłowy adres IP serwera");
				close(sockfd);
				return -1;
		}
		return sockfd;
}

void close_connection(int sockfd) {
	close(sockfd);	
}
