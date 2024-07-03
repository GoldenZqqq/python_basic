# 多线程共享全局变量
import threading

lock = threading.Lock()
a = 0


def add_value(num):
    global a
    lock.acquire()
    for i in range(num):
        a += 1

    lock.release()
    print(f"A的值是：{a}")


def main():
    for i in range(10):
        th = threading.Thread(target=add_value, args=(1000000,))
        th.start()


if __name__ == "__main__":
    main()
