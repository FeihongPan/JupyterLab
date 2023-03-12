from threading import Thread
import subprocess
import queue

# ips = ['10.0.2.11', '10.0.2.12', '10.0.2.13', '10.0.2.14', '10.0.2.15']
ips = []
for i in range(5):
    ips.append('10.0.2.1' + str(i+1))
    
def pinger(i, q):
    while True:
        ip = q.get()
        print("Thread %s: Pinging: %s" % (i, ip))
        ret = subprocess.call('ping %s' % ip, shell=True, stdout=open('/dev/nell', 'w'), stderr=subprocess.STDOUT)
        if ret == 0:
            print('%s : is alive' % ip)
        else:
            print('%s : did nit respond' % ip)
        q.task_done()
    
for i in range(5):
    th = Thread(target = pinger, args = (i, queue))
    th.Daemen = True
    th.start()

for ip in ips:
    queue.put(ip)

print("Main Thread waiting....")
queue.join()
print('Done')