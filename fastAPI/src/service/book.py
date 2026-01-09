import asyncio

import aiohttp

from config import naver_search_base_url, naver_client_id, naver_client_secret


class NaverBookScraper:

    def __init__(self):
        self.category = "/book"
        self.naver_search_book_base_url = naver_search_base_url + self.category
        self.naver_client_id = naver_client_id
        self.naver_client_secret = naver_client_secret

    async def fetch(self, session, url, headers):
        async with session.get(url, headers=headers) as response:
            result = await response.json()
            return result["items"]

    def unit_url(self, keyword, display, start):
        return {
            "url": f"{self.naver_search_book_base_url}?query={keyword}&display={display}&start={start}",
            "headers": {
                "X-Naver-Client-Id": self.naver_client_id,
                "X-Naver-Client-Secret": self.naver_client_secret,
            },
        }

    async def search(self, keyword, display, totalPages):
        apis = [
            self.unit_url(keyword, display, 1 + i * display) for i in range(totalPages)
        ]

        async with aiohttp.ClientSession() as session:
            allData = await asyncio.gather(
                *[self.fetch(session, api["url"], api["headers"]) for api in apis]
            )
            results = list()
            for data in allData:
                if data is not None:
                    for book in data:
                        results.append(book)
                        # print(book["title"])
            return results


if __name__ == "__main__":
    scraper = NaverBookScraper()
    results = asyncio.run(scraper.search("고양이", 10, 2))
    print(results)
    print(len(results))
