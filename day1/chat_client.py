from socket import *
import os
import sys

# 服务器地址
ADDR = ('127.0.0.1', 8989)

# 进入聊天室
def login(s):
    while True:
        try:
            name = input("请输入昵称:")
            if not name:
                continue
        except KeyboardInterrupt:
            sys.exit("谢谢使用")
        msg = "L " + name
        s.sendto(msg.encode(),ADDR)
        #　接收反馈结果
        data,addr = s.recvfrom(128)
        if data.decode() == 'OK':
            print("您已进入聊天室")
            return name
        else:
            print(data.decode())

def recv_msg(s):
    while True:
        data ,addr = s.recvfrom(2048)
        # 接收进程退出
        if data.decode() == 'EXIT':
            sys.exit()
        print(data.decode() + '\n头像:', end='')
        # print(data.decode)

def send_msg(s,name):
    while True:
        try:
            text = input("头像:")
        except KeyboardInterrupt:
            text = 'quit'
        # 退出聊天室
        if text.strip() == 'quit':
            msg = "Q " + name
            s.sendto(msg.encode(), ADDR)
            sys.exit('退出聊天室')
        msg = "C %s %s" % (name, text)
        s.sendto(msg.encode(), ADDR)


def main():
    s = socket(AF_INET, SOCK_DGRAM)
    #进入聊天室
    name = login(s)  # 请求进入聊天室
    # 创建新的进程
    pid = os.fork()
    if pid < 0:
        print("Error!!")
        return
    elif pid == 0:
        send_msg(s, name)  # 子进程发送消息
    else:
        recv_msg(s)  # 父进程接收消息


main()