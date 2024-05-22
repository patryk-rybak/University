CC = gcc
CFLAGS = -Wall
LDFLAGS =

SRCS = traceroute.c util.c
OBJS = $(SRCS:.c=.o)
TARGET = traceroute

.PHONY: all clean distclean

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) $(LDFLAGS) $^ -o $@

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJS)

distclean: clean
	rm -f $(TARGET)

