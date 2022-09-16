from abc import ABCMeta, abstractmethod

class BaseScript(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def position(self):
        pass

    @abstractmethod
    def do(self):
        pass 

    def run(self):
        self.position()
        # figure out a way to stop??
        while True:
            self.do()
