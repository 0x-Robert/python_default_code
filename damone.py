"두개의 프로그램을 동시에 쓸 수 있음"
"서버에서 cpu성능에 따라 어느것을 쓰는게 좋은지 보는게 좋음"

import threading
import time
import logging


logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def worker1():
    logging.debug('start')
    time.sleep(5)
    logging.debug('end')
def worker2():
    logging.debug('start')
    time.sleep(2)
    logging.debug('end')


if __name__ == '__main__':
    threads = []
    for _ in range(5):
        t = threading.Thread(target=worker1)
        t.setDaemon(True)
        t.start()
        #threads.append(t)
    print(threading.enumerate())   
    for thread in threading.enumerate():
        if thread is threading.currentThread():
            print(thread)
            continue
        thread.join()




