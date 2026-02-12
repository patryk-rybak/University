from abc import ABC, abstractmethod
import random, string
import os
import shutil
from queue import Queue
import threading
import time


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class FTPDownloadCommand(Command):
    def __init__(self, file_name):
        self.file_name = file_name

    def execute(self):
        print(f"downloading {self.file_name} via ftp")


class HTTPDownloadCommand(Command):
    def __init__(self, file_name):
        self.file_name = file_name

    def execute(self):
        print(f"downloading {self.file_name} via http")


class CreateFileCommand(Command):
    def __init__(self, file_name):
        self.file_name = file_name

    def randomword(self, length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    def execute(self):
        with open(self.file_name, 'w') as f:
            f.write(self.randomword(50))
        print(f"File {self.file_name} created with 50-character string")


class CopyFileCommand(Command):
    def __init__(self, source_file, destination_file):
        self.source_file = source_file
        self.destination_file = destination_file

    def execute(self):
        if os.path.exists(self.source_file):
            shutil.copy(self.source_file, self.destination_file)
            print(f"file {self.source_file} copied to {self.destination_file}")
        else:
            print(f"error - Ssurce file {self.source_file} does not exist")


# Queue/Invoker


class CommandQueue:
    def __init__(self):
        self.queue = Queue()

    def add_command(self, command):
        self.queue.put(command)

    def get_command(self):
        return self.queue.get()


class CommandWorker(threading.Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            if not self.queue.queue.empty():
                command = self.queue.get_command()
                command.execute()


class CommandProducer(threading.Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        for i in range(10):
            self.queue.add_command(FTPDownloadCommand(f"file_{i}.txt"))
            self.queue.add_command(HTTPDownloadCommand(f"file_{i}.txt"))
            self.queue.add_command(CreateFileCommand(f"new_file_{i}.txt"))
            self.queue.add_command(CopyFileCommand(f"new_file_{i}.txt", f"copied_file_{i}.txt"))
            time.sleep(1)


class Invoker:
    def __init__(self):
        self.command_queue = CommandQueue()

    def start_processing(self):
        for _ in range(2):
            worker = CommandWorker(self.command_queue)
            worker.daemon = True
            worker.start()

        producer = CommandProducer(self.command_queue)
        producer.start()


invoker = Invoker()
invoker.start_processing()
