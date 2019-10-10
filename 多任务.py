import time
import threading

def sing():
    for i in range(10):
        print('唱歌.....')
        time.sleep(0.3)

def dance():
    for i in range(10):
        print('跳舞.....')
        time.sleep(0.3)

def main():
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    print(len(threading.enumerate()))
    t1.start()
    t2.start()
    print(len(threading.enumerate()),'查看线程数')

if __name__ == '__main__':
    main()