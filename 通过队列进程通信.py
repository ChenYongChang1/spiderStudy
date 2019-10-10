import multiprocessing
from multiprocessing import Queue
import time
def download(q):
    while 1:
        if not q.full():
            data = [11, 2, 3, 4, 5]
            q.put(data)
        else:
            print('满了')
        time.sleep(0.6)
def analysis_data(q):
    while 1:
        # 分析数据
        if not q.empty():
            print(q.get())
        else:
            print('还没数据呢')
        time.sleep(0.5)
def main():
    q = Queue(4)
    q.empty()
    p1 = multiprocessing.Process(target=download,args=(q,))
    p2 = multiprocessing.Process(target=analysis_data,args=(q,))
    p1.start()
    p2.start()
if __name__ == '__main__':
    main()