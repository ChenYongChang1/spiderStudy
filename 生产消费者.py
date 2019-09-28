import threading
import time
import random
MAX_BUFF_LEN = 5

buff = []
condition = threading.Condition()

class Producer(threading.Thread):
    def run(self):
        global buff
        while True:
            condition.acquire()
            if len(buff) < MAX_BUFF_LEN:
                # 如果共享区域未满，生产数据
                num = random.uniform(0, 5)
                buff.append(num)
                print('生产者向共享区域加入%f' % num)
                condition.notify()
            else:
                # 如果共享区满，停止生产
                print('共享区满，生产者阻塞！')
                condition.wait()
            condition.release()
            time.sleep(random.uniform(0, 1))

class Consumer(threading.Thread):
    def run(self):
        global buff
        while True:
            condition.acquire()
            if buff:
                # 如果共享区非空，消费数据
                num = buff.pop(0)
                print('消费者消费掉%f' %num)
                condition.notify()
            else:
                # 如果共享去空，停止消费
                print('共享区空，消费者阻塞！')
                condition.wait()
            condition.release()
            time.sleep(random.uniform(0, 1))

producer = Producer()
consumer = Consumer()
producer.setDaemon(True)
consumer.setDaemon(True)
try:
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
except KeyboardInterrupt:
    print('程序强制结束！')