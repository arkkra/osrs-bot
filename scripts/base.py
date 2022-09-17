from abc import ABCMeta, abstractmethod

class BaseScript(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def pre(self):
        pass

    @abstractmethod
    def do(self):
        pass

    @abstractmethod
    def post(self):
        pass

    def run(self):
        self.pre()
        self.do()   
        self.post()
