"두개의 프로그램을 동시에 쓸 수 있음"
"서버에서 cpu성능에 따라 어느것을 쓰는게 좋은지 보는게 좋음"

import threading
import time
import logging


logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

#글로벌에서 lock를 쓸 수 있지만 추천하지않음 인수로 넘겨주는게 더 나음

def worker1(d,lock):
    logging.debug('start')
    with lock: #with에서 실행후에 진행되는 코드 
        i = d['x']
        time.sleep(5)
        d['x'] = i + 1
        logging.debug(d)
        with lock:
            d['x'] = i + 1 #Rlock
    logging.debug('end')

def worker2(d,lock):
    logging.debug('start')
    lock.acquire() #다른 스레드에 영향을 받지 않게 하기위해 씀
    i = d['x']
    d['x'] = i + 1
    logging.debug(d)
    lock.release() #다른 스레드에 영향을 받지 않게 하기위해 씀
    logging.debug('end')


if __name__ == '__main__':
    d = {'x':0}
    #lock = threading.Lock()
    lock = threading.RLock()
    t1 = threading.Thread(target=worker1, args=(d,lock))
    t2 = threading.Thread(target=worker2, args=(d,lock))
    t1.start()
    t2.start()




