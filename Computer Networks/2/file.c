#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "error.h"


int open_file(const char *file_name) {
    int fd = open(file_name, O_WRONLY | O_CREAT | O_TRUNC, S_IRUSR | S_IWUSR);
    if (fd == -1) {
        handle_error("Nie można otworzyć pliku");
    }
    return fd;
}

void write_to_file(int fd, const char *data, size_t size) {
    ssize_t bytes_written = write(fd, data, size);
    if (bytes_written != size) {
        handle_error("Błąd podczas zapisywania do pliku");
    }
}

void close_file(int fd) {
    if (close(fd) == -1) {
        handle_error("Błąd podczas zamykania pliku");
    }
}

int get_file(int sockfd, const char *file_name, int file_size) {
    open_file(file_name);
    send_get_request();
}