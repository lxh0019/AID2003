"""
用两个子进程分别拷贝图片的上半部分和下半部分
"""
import os
from multiprocessing import Process


# 获取文件大小
size = os.path.getsize("time")
print(size)

# 获取文件上半部分
def read1():
    f = open("time", "rb")
    data = f.read(size // 2)
    f.close()
    p = open("file1", "wb")
    p.write(data)

# 获取文件下半部分
def read2():
    f = open("time", "rb")
    f.seek(size // 2)
    data = f.read()
    f.close()
    p = open("file2", "wb")
    p.write(data)


p1 = Process(target=read1())
p1.start()
p2 = Process(target=read2())
p2.start()
p1.join()
p2.join()