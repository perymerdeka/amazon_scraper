import httpx
from httpx import Client
from rich import print
from typing import Any

from services.scraper.runner import Runner

def main():
    headers: dict[str, Any] = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}
    response = httpx.get(url="https://www.amazon.co.uk/ASUS-Vivobook-E1504FA-3-7320U-Windows/dp/B0BN1MXXMX/ref=sr_1_3?keywords=laptop&qid=1698300194&sr=8-3", headers=headers)


    # write response
    if response.status_code == 200:
        f = open("response.html", 'w+')
        f.write(response.text)
        f.close()
    else:
        print(response.status_code)

def run():
    spider: Runner = Runner()
    data = spider.search_product("laptop")
    print(data)

if __name__ == '__main__':
    run()