from socket import *
import os, sys

ADDR = ("0.0.0.0", 8989)


# 退出
def do_quit(s, name):
    msg = "\n%s 退出聊天室" % name
    for i in user:
        if i != name:  # 其他人
            s.sendto(msg.encode(), user[i])
        else:
            s.sendto(b'EXIT', user[i])
    del user[name]  # 删除该用户


def do_chat(s, name, text):
    msg = "\n%s: %s" % (name, text)
    for i in user:
        # 刨除本人
        if i != name:
            s.sendto(msg.encode(), user[i])


# 处理登录
def do_login(s, name, addr):
    if name in user:
        s.sendto("用户已存在".encode(), addr)
        return
    # 用户不存在，可以进入聊天室
    s.sendto("OK".encode(), addr)
    # 通知其他人
    msg = "\n欢迎%s进入聊天室" % name
    for i in user:
        s.sendto(msg.encode(), user[i])
    user[name] = addr


def do_request(s):
    while True:
        data, addr = s.recvfrom(2048)
        tem = data.decode().split(" ")
        # 根据不同的请求类型分发函数处理
        # L 进入  C 聊天 Q退出
        if tem[0] == "L":
            do_login(s, tem[1], addr)
        elif tem[0] == 'C':
            text = " ".join(tem[2:])
            do_chat(s, tem[1], text)
        elif tem[0] == 'Q':
            if tem[1] in user:
                do_quit(s, tem[1])


# 存储用户信息
user = {}


def main():
    # udp 服务端
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(ADDR)
    pid = os.fork()
    if pid == 0:
        # 子进程处理管理员消息
        while True:
            msg = input("管理员消息:")
            msg = "C 管理员 " + msg
            s.sendto(msg.encode(), ADDR)
    else:
        # 处理客户端请求
        do_request(s)


main()
