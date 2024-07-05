# 协程爬取图片
import asyncio, aiohttp, aiofiles
from bs4 import BeautifulSoup
import chardet

headers = {
    "Cookie": "trenvecookieclassrecord=%2C8%2C",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
}


async def get_index_url(url, semaphore):
    # 控制协程并发数量
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as r:
                raw_data = await r.read()
                result = chardet.detect(raw_data)
                encoding = result["encoding"]
                soup = BeautifulSoup(await r.text(encoding, "ignore"), "html.parser")
                temp = soup.find("div", class_="list")
                info = temp.find_all("a")
                links = []
                for a in info:
                    link = a["href"]
                    if "http" in link:
                        continue
                    link = f"http://www.netbian.com{link}"
                    links.append(link)
        return links


async def get_hd_url(page, semaphore):
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            async with session.get(page, headers=headers) as r:
                raw_data = await r.read()
                result = chardet.detect(raw_data)
                encoding = result["encoding"]
                soup = BeautifulSoup(await r.text(encoding, "ignore"), "html.parser")
                pic = soup.find("div", class_="pic")
                if pic:
                    img = pic.find("img")
                    if img:
                        link = img["src"]
                        title = img["title"]
                    else:
                        print("No img tag found in div with class 'img'")
                        return None, None
                else:
                    print("No div with class 'pic' found")
                    return None, None
                return link, title


async def downloads(link, title, semaphore):
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            async with session.get(link, headers=headers) as r:
                # raw_data = await r.read()
                # result = chardet.detect(raw_data)
                # encoding = result["encoding"]
                async with aiofiles.open(
                    rf"C:\Learn\python_basic\Chapter 15 - asyncio\files\{title}.jpg",
                    "wb",
                ) as f:
                    await f.write(await r.content.read())
                    print(f"已完成...{title}")


async def main():
    task1 = []
    semaphore = asyncio.Semaphore(3)  # 控制并发数量
    for i in range(2, 6):
        if i == 1:
            index_url = f"http://www.netbian.com/huahui/"
        else:
            index_url = f"http://www.netbian.com/huahui/index_{i}.htm"
        task1.append(asyncio.create_task(get_index_url(index_url, semaphore)))
    dones, pendings = await asyncio.wait(task1)

    task2 = []
    for t in dones:
        pages = t.result()
        for page in pages:
            task2.append(asyncio.create_task(get_hd_url(page, semaphore)))
    dones, pendings = await asyncio.wait(task2)

    task3 = []
    for t in dones:
        link, title = t.result()
        if link and title:
            task3.append(asyncio.create_task(downloads(link, title, semaphore)))
    await asyncio.wait(task3)


if __name__ == "__main__":
    asyncio.run(main())
