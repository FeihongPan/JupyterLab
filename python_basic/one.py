import time
import _thread
import threading

def t1(name,x,l):
    for i in range(x):
        print(i,name)
        time.sleep(1)
    l.release()

lock = _thread.allocate_lock()        
lock.acquire()

_thread.start_new_thread(t1,('huamian',5,lock))
_thread.start_new_thread(t1,('shengyin',5,lock))

while lock.locked():
    pass




