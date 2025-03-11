import multiprocessing as mp
import time

def producer(condition, buffer):
    for i in range(5):
        with condition:  # 获取条件锁
            while buffer.value != -1:  # 如果缓冲区非空，等待
                condition.wait()
            print(f"生产者生产 {i}")
            buffer.value = i  # 写入数据
            condition.notify()  # 通知消费者

def consumer(condition, buffer):
    for _ in range(5):
        with condition:
            while buffer.value == -1:  # 如果缓冲区为空，等待
                condition.wait()
            print(f"消费者消费 {buffer.value}")
            buffer.value = -1  # 清空缓冲区
            condition.notify()  # 通知生产者

if __name__ == "__main__":
    condition = mp.Condition()
    buffer = mp.Value('i', -1)  # 共享变量，初始值为-1（空）
    p = mp.Process(target=producer, args=(condition, buffer))
    c = mp.Process(target=consumer, args=(condition, buffer))
    p.start()
    c.start()
    p.join()
    c.join()