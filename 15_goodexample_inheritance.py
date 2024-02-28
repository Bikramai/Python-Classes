class InvalidOperationError(Exception):
    pass

class Stream:
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise IndentationError("Stream is already open.")
        self.opened = True

    def close(self):
        if not self.opened:
            raise IndentationError("Stream is already closed.")
        self.opened = False

class FileStream(Stream):
    def read(self):
        print("Reading data from a file")

class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")