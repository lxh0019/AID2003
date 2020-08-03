"""
创建二级子进程处理僵尸
"""

from os import *
from time import *


def f1():
    for i in range(3):
        sleep(2)
        print("写代码")


def f2():
    for i in range(2):
        sleep(4)
        print("测代码")


pid = fork()
if pid < 0:
    print("Create process failed")
elif pid == 0:
    p = fork()  # 创建二级子进程
    if p == 0:
        f1()
    else:
        _exit(0)  # 一级子进程退出
else:
    pid, status = wait()  # 等待回收一级子进程
    f2()
