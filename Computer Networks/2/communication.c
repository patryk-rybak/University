#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <sys/select.h>
#include "error.h"

#define MAX_BUFFER_SIZE 1024

void generate_get_request(int start, int length, char *request) {
		sprintf(request, "GET %d %d\n", start, length);
}

int check_packets_available(int sockfd, struct sockaddr_in *server_addr) {
// sprawdz funckją recive i pętlą while pakity w gnieździe i jeżeli trafisz na pakiet od naszego servera i portu to zwróć wartość 1, 
}

int send_get_request(int sockfd, struct sockaddr_in *server_addr, int start, int length) {
		char request[MAX_BUFFER_SIZE];
		generate_get_request(start, length, request);

		// Ustawienie maksymalnego czasu oczekiwania na odpowiedź
		struct timeval timeout;
		timeout.tv_sec = 2;  // Maksymalny czas oczekiwania na odpowiedź w sekundach
		timeout.tv_usec = 0;

		while (1) {
				// Wysłanie żądania GET
				if (sendto(sockfd, request, strlen(request), 0, (struct sockaddr *)server_addr, sizeof(*server_addr)) == -1) {
						handle_error("Błąd podczas wysyłania żądania GET");
						return 0;
				}

				// Sprawdzenie dostępności pakietów
				fd_set read_fds;
				FD_ZERO(&read_fds);
				FD_SET(sockfd, &read_fds);
				int select_result = select(sockfd + 1, &read_fds, NULL, NULL, &timeout);
				if (select_result == -1) {
						handle_error("Błąd funkcji select");
						return 0;
				} else if (select_result == 0) {
						// Przekroczono maksymalny czas oczekiwania na odpowiedź

						// Obliczenie pozostałego czasu do wykorzystania w kolejnym wywołaniu select
						if (timeout.tv_sec == 0 && timeout.tv_usec == 0) {
								// Wykorzystano już maksymalny czas, nie ma sensu kontynuować
								handle_error("Przekroczono maksymalny czas oczekiwania na odpowiedź");
								return 0;
						} else if (timeout.tv_usec >= 500000) {
								timeout.tv_usec -= 500000; // Odejmujemy 0.5s
						} else {
								timeout.tv_sec -= 1;
								timeout.tv_usec += 500000; // Dodajemy 0.5s
						}

						continue;  // Powtórzenie pętli, aby wysłać ponownie żądanie GET
				}

				// Sprawdzenie, czy adres źródłowy i port źródłowy się zgadzają
				struct sockaddr_in source_addr;
				socklen_t source_addr_len = sizeof(source_addr);
				getsockname(sockfd, (struct sockaddr *)&source_addr, &source_addr_len);
				if (source_addr.sin_addr.s_addr != server_addr->sin_addr.s_addr || source_addr.sin_port != server_addr->sin_port) {
						handle_error("Niepoprawny adres źródłowy lub port źródłowy");
						return 0;
				}

				break;
		}

		return 1; // Wysłano żądanie GET i otrzymano potwierdzenie zgodne z oczekiwaniami
}

int receive_data_response(int sockfd, char *data, int length) {
		// Odbieranie odpowiedzi DATA
		int bytes_received = recv(sockfd, data, length, 0);
		if (bytes_received == -1) {
				handle_error("Błąd podczas odbierania danych");
				return 0;
		}

		return bytes_received;
}

