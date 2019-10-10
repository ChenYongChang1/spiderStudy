from threading import Thread
import time
import multiprocessing

def text1():
    while 1:
        print(1)
        time.sleep(1)

def text2():
    while 1:
        print(2)
        time.sleep(1)

def main():
    p1 = multiprocessing.Process(target=text1)
    p2 = multiprocessing.Process(target=text2)
    p1.start()
    p2.start()
    # t1 = Thread(target=text1)
    # t2 = Thread(target=text2)
    # t1.start()
    # t2.start()
if __name__ == '__main__':
    main()