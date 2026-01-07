import asyncio

import aiohttp

from config import naver_search_base_url, naver_client_id, naver_client_secret


class NaverBookScraper:
    def __init__(self):
        self.naver_search_base_url = naver_search_base_url
        self.naver_client_id = naver_client_id
        self.naver_client_secret = naver_client_secret

    async def search(self, query):
        # urls = [f"{self.naver_search_base_url}?q={query}&display=20&start={1+i*20}" for i in range(1, 10)]
        urls = [f"{self.naver_search_base_url}?query={query}&display=20"]
        async with aiohttp.ClientSession() as session:
            await asyncio.gather(
                *[self.fetch(session, url) for i, url in enumerate(urls)]
            )

    async def fetch(self, session, url):
        headers = {
            "X-Naver-Client-Id": self.naver_client_id,
            "X-Naver-Client-Secret": self.naver_client_secret,
        }
        async with session.get(url, headers=headers) as response:
            result = await response.json()
            items = result["items"]


if __name__ == "__main__":
    scraper = NaverBookScraper()
    asyncio.run(scraper.search("cat"))
