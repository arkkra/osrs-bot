from abc import ABCMeta, abstractmethod
from pynput import keyboard

class BaseScript(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self._stop = False
        self.listener = keyboard.Listener(on_press=self._key_pressed,
                                          on_release=self._key_released)
        self.listener.start()

    @property
    def stop(self):
        return self._stop
    
    @stop.setter
    def stop(self, new_value):
        self._stop = new_value
        self.stop_pressed()

    def _key_pressed(self, key):
        try:
            print('alphanumeric key {0} pressed'.format(
                key.char))
        except AttributeError:
            print('special key {0} pressed'.format(
                key))

    def _key_released(self, key):
        print(key)
        if key == keyboard.Key.esc:
            self.stop = not self.stop

    @abstractmethod
    def pre(self):
        pass

    @abstractmethod
    def do(self):
        pass

    @abstractmethod
    def post(self):
        pass

    @abstractmethod
    def stop_pressed(self):
        pass

    def run(self):
        self.pre()
        self.do()   
        self.post()
