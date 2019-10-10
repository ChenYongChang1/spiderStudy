import threading
import time
g_num = 0
class MyThreading(threading.Thread):
    def run(self):
        global g_num
        for i in range(1000000):
            mutext.acquire()
            g_num+=1
            mutext.release()

if __name__ == '__main__':
    mutext = threading.Lock()
    t1 = MyThreading()
    t2 = MyThreading()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('gnum:{}'.format(g_num))