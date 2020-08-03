import multiprocessing as mf
import time


def th1(a, name):
    time.sleep(a)
    print("%s在吃饭" % name)


def th2(a, name):
    time.sleep(a)
    print("%s在睡觉" % name)


def th3(a, name):
    time.sleep(a)
    print("%s在打豆豆" % name)


things = [th1, th2, th3]
re = [(4, "lan"), (2, "wo"), (1, "rt")]
ends = []
i = 0
for item in things:
    p = mf.Process(target=item, args=re[i])
    i += 1
    ends.append(p)
    p.start()
for i in ends:
    i.join()
