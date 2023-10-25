import httpx
from httpx import Client
from typing import Any

from services.scraper.amazon import AmazonSpider

def main():
    headers: dict[str, Any] = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}
    response = httpx.get(url="https://www.amazon.co.uk/s?k=computer&ref=nb_sb_noss", headers=headers)


    # write response
    if response.status_code == 200:
        f = open("response.html", 'w+')
        f.write(response.text)
        f.close()
    else:
        print(response.status_code)

def run():
    spider: AmazonSpider = AmazonSpider()
    spider.run()

if __name__ == '__main__':
    run()