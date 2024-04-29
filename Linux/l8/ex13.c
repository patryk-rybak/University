#include <unistd.h>

int main() {

  if (!fork())
    sleep(30);
  else
    sleep(10);

  return 0;
}

/*
 * systemd is a system and service manager for Linux operating systems. When run as first process on boot (as PID 1), it acts as init system that brings up and maintains userspace services. Separate instances are started for logged-in users to start their services.
 */

