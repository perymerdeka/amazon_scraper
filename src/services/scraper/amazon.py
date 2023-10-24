from httpx import Client
from typing import Any

from fake_useragent import UserAgent as ua
from rich import print_json
from bs4 import BeautifulSoup
from os.path import join


from core.settings.base import BASE_DIR

class AmazonSpider(object):
    def __init__(self) -> None:
        self.base_url: str = "https://www.amazon.co.uk/s"
        self.client: Client = Client(headers={"User-Agent": ua.random})

    def get_response(self, params: dict[str, Any]) -> str:
        params: dict[str, Any] = {
            "k": "keyboard cleaner",
            "crid": "3I7W6DAZVIT0Z",
            "sprefix": "keyboard,aps,630",
            "ref": "nb_sb_ss_ts-doa-p_3_8",
        }

        response = self.client.get(
            self.base_url, params=params
        )

        # save html file
        f = open(join(BASE_DIR, "response.html"))
        f.write(response.text)
        f.close()

        # soup object
        soup: BeautifulSoup = BeautifulSoup(response.text)
        return soup
    
    
    def get_pages(self, soup: BeautifulSoup):
        contents = soup.find()


    def get_suggest(self):
        suggest_url: str = "https://completion.amazon.co.uk/api/2017/suggestions?"
        params: dict[str, Any] = {
            "limit": 11,
            "prefix": "computer",
            "suggestion-type": "WIDGET",
            "suggestion-type": "KEYWORD",
            "page-type": "Search",
            "alias": "aps",
            "site-variant": "desktop",
            "version": "3",
            "event": "onfocuswithsearchterm",
            "wc": "",
            "lop": "en_GB",
            "last-prefix": "",
            "avg-ks-time": "0",
            "fb": 1,
            "session-id": "259-3531655-8896020",
            "request-id": "KSPRG4K9W5NH6W5D7EZ2",
            "mid": "A1F83G8C2ARO7P",
            "plain-mid": 3,
            "client-info": "amazon-search-ui",
        }

        response = self.client.get(suggest_url, params=params)

        if response.status_code == 200:
            print_json(response.json())
        else:
            pass