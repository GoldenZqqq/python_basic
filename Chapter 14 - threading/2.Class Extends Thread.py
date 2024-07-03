# 多线程2 - 继承Thread类来创建多线程
import threading
import time


class Singing(threading.Thread):
    def __init__(self, delay):
        super(Singing, self).__init__()
        self.delay = delay

    def run(self) -> None:
        print(f"{threading.current_thread().name}开始唱歌")
        time.sleep(self.delay)
        print("结束唱歌")


class Dancing(threading.Thread):
    def __init__(self, delay):
        super(Dancing, self).__init__()
        self.delay = delay

    def run(self) -> None:
        print(f"{threading.current_thread().name}开始跳舞")
        time.sleep(self.delay)
        print("结束跳舞")


def multi_thread():
    task = []
    th1 = Singing(2)
    th1.start()
    task.append(th1)
    for i in range(3):
        th2 = Dancing(4)
        th2.start()
        task.append(th2)

    for t in task:
        t.join()


if __name__ == "__main__":
    start_time = time.time()
    multi_thread()
    end_time = time.time()
    print(f"总共消耗时间：{end_time - start_time}")
