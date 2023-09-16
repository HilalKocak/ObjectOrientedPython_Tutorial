from abc import ABC, abstractmethod

class OperationError(Exception):
    pass

class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise OperationError("Zaten dosya acik")
        self.opened = True

    def close(self):
        if not self.opened:
            raise OperationError("Zaten dosya kapali") 
        self.opened = False
    
    @abstractmethod
    def read(self):
        pass

class FileStream(Stream): # concrete
    def read(self):
        print("Dosyadan data okunuyor")
        

class NetworkStream(Stream):
    def read(self):
        print("Agdan data okunuyor")

class MemoryStream(Stream):
    pass



