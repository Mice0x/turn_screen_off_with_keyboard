from ctypes import windll
from pynput.keyboard import Key, Listener
import time

class MonitorController:
    def __init__(self, key1, key2):
        self.key1 = key1
        self.key2 = key2

        self.keylist = set()
        listener = Listener(on_press=self.on_press, on_release=self.on_release)
        listener.start()
        listener.join()
    def on_press(self,key):
        self.keylist.add(str(key))
        #print(str(key))
        #print(self.keylist)
        if self.key1 in self.keylist and self.key2 in self.keylist:
            time.sleep(0.3)
            windll.user32.PostMessageA(0xffff, 0x0112, 0xf170, 2)
    def on_release(self,key):
        if str(key) in self.keylist:
            self.keylist.remove(str(key))
if __name__ == "__main__":
    key1 = "Key.cmd"
    key2 =  "\'o\'"
    MonitorController(key1, key2)
