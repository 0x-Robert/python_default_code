"두개의 프로그램을 동시에 쓸 수 있음"
"서버에서 cpu성능에 따라 어느것을 쓰는게 좋은지 보는게 좋음"

import threading
import time
import logging


logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def worker1(x,y=1):
    logging.debug('start')
    time.sleep(x)
    time.sleep(y)
    time.sleep(5)
    logging.debug('end')
def worker2():
    logging.debug('start')
    time.sleep(2)
    logging.debug('end')


if __name__ == '__main__':
    t = threading.Timer(3,worker1,args=(100,),kwargs={'y':200})
    t.start()



