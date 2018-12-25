
# _*_ encoding:utf-8 _*_
__author__ = ''
__date__ = '2018/12/25 11:17'

import threading


def worker():
    print('i am thread')
    tt = threading.current_thread()
    print(tt.getName())


t = threading.current_thread()
print(t.getName())

new_t = threading.Thread(target=worker, name='worker_thread')
new_t.start()



