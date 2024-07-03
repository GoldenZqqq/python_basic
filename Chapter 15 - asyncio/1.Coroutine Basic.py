# 协程
import asyncio, time


async def singing():
    print("开始唱歌")
    # time.sleep(1)
    await asyncio.sleep(1)
    print("结束唱歌")


async def dancing():
    print("开始跳舞")
    # time.sleep(3)
    await asyncio.sleep(3)
    print("结束跳舞")


async def main():
    # await singing()
    # await dancing()
    # task1 = asyncio.create_task(singing())
    # task2 = asyncio.create_task(dancing())
    # await asyncio.wait([task1, task2])
    tasks = []
    for i in range(4):
        tasks.append(asyncio.create_task(singing()))
        tasks.append(asyncio.create_task(dancing()))
    await asyncio.wait(tasks)


if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    end_time = time.time()
    print("总共用时：", end_time - start_time)
