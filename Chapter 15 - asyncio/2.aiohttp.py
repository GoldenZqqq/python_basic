# 同步 request.get() --> 异步 aiohttp 替换
import asyncio, aiohttp, aiofiles

urls = [
    "https://images.pexels.com/photos/19793123/pexels-photo-19793123.jpeg?auto=compress&cs=tinysrgb&w=600&lazy=load",
    "https://images.pexels.com/photos/26836541/pexels-photo-26836541.jpeg?auto=compress&cs=tinysrgb&w=600&lazy=load",
    "https://images.pexels.com/photos/26741269/pexels-photo-26741269.jpeg?auto=compress&cs=tinysrgb&w=600&lazy=load",
]


async def downloads(url):
    filename = url.split("/")[-1].split("?")[0]
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as r:  # session.get() == requests.get()
            # with open(
            #     rf"E:\Learn\python_basic\Chapter 15 - asyncio\img\{filename}", "wb"
            # ) as f:
            #     f.write(await r.content.read())
            #     print(f"已完成...{filename}")
            async with aiofiles.open(
                rf"E:\Learn\python_basic\Chapter 15 - asyncio\img\{filename}", "wb"
            ) as f:
                await f.write(await r.content.read())
                print("已完成...{filename}")


async def main():
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(downloads(url)))
    await asyncio.wait(tasks)


if __name__ == "__main__":
    asyncio.run(main())
