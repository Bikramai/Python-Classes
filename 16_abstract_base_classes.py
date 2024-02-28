from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass

class Stream(ABC): #Abstract Base Class
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

    @abstractmethod 
    # here we define read mithod. This method has no implementation.
    def read(self):
        pass

class FileStream(Stream):
    def read(self):
        print("Reading data from a file")

class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")

class MemoryStream(Stream):
    def read(self):
        print("Reading data from a memory stream.")



stream = MemoryStream()
stream.open()

#Note:- 
# Abstract Base Class :- is a half baked cookies. Its not ready to eat.
# It purpose is to provide some commom code to these derivitives.
        
# 1st step - ABC
# 2nd step - to define the common interface for all Streams. We want all Streams to have read method,
# a potentially right method in the future.
        


