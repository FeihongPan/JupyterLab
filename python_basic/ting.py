import time
import threading

class MyThread(threading.Thread): 
    def __init__(self, threadID, threadname, delay, counter): # 重写父类方法
        self.threadID = threadID
        self.threadname = threadname
        self.delay = delay
        self.counter = counter
        threading.Thread.__init__(self) # 直接调用父类方法

    def run(self):
        print("Starting %s" % self.threadname)
        self.print_time(self.delay, self.counter)
        print("Exiting %s" % self.threadname)

    def print_time(self, delay, counter):
        while counter: # while counter == True -> 只要counter > 0
            time.sleep(delay)
            print(counter, "%s:%s" % (self.threadname, time.ctime()))
            counter -= 1
        
        
thread1 = MyThread(1, 'xiancheng1', eval(input('thread1:')), 3)
thread2 = MyThread(2, 'xiancheng2', eval(input('thread2:')), 3)

thread1.start()
thread2.start()

# th1.run()
# th2.run()

print("Exiting Main Thread")