from multiprocessing import Pool
import time

def work(mess):
    for i in range(10):
        print('---{}---第{}ji'.format(i, mess))
        time.sleep(0.1)


if __name__ == '__main__':
    po = Pool(3)
    for i in range(10):
        po.apply_async(work, (i,))

    print('---start----')
    po.close()
    po.join()
    print('---end---')