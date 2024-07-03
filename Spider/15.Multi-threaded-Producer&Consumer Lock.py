# 多线程-生产者和消费者-Lock版
import threading
import random
import time

lock = threading.Lock()
cycle_time = 10
count = 0
total_money = 0


class Producer(threading.Thread):
    def run(self) -> None:
        global total_money, cycle_time, count
        while True:
            lock.acquire()
            if count > cycle_time:
                print("生产者已经完成工作了")
                lock.release()
                break
            money = random.randint(100, 5000)
            total_money += money
            count += 1
            print(f"{threading.current_thread().name}赚了{money}元")
            lock.release()


class Consumer(threading.Thread):
    def run(self) -> None:
        global total_money
        while True:
            lock.acquire()
            money = random.randint(100, 5000)
            if total_money >= money:
                total_money -= money
                print(f"{threading.current_thread().name}消费了{money}元")
            else:
                if count > cycle_time:
                    print(
                        f"{threading.current_thread().name}想消费{money}元，但是余额不足，并且生产者不再生产了"
                    )
                    lock.release()
                    break
                print(
                    f"{threading.current_thread().name}想消费{money}元，但是余额不足，只有{total_money}"
                )
            lock.release()
            time.sleep(0.5)


def main():
    for i in range(5):
        th1 = Producer(name=f"生产者{i}号")
        th1.start()

    for t in range(5):
        th2 = Consumer(name=f"消费者{t}号")
        th2.start()


if __name__ == "__main__":
    main()
