import httpx

from httpx import Client
from typing import Any


from fake_useragent import UserAgent
from rich import print_json
from bs4 import BeautifulSoup
from os.path import join


from core.settings.base import BASE_DIR

class AmazonSpider(object):
    def __init__(self) -> None:
        self.base_url: str = "https://www.amazon.co.uk/s"
        self.ua: UserAgent = UserAgent()
        self.client: Client = Client(headers={"User-Agent": self.ua.random})

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
    
    
    def get_product(self, soup: BeautifulSoup) -> (dict[str, Any] | None):
        contents = soup.find("span", attrs={"data-component-type": "s-search-results"}).find_all("div", attrs={"data-component-type": "s-search-result"})
        for content in contents:
            title = content.find("h2", attrs={"class": "s-line-clamp-2"}).find("span").text.strip()
            product_link = "https://www.amazon.co.uk/" + content.find("a", attrs={"class": "a-link-normal", "class": "s-no-outline"})['href']
            price = content.find("span", attrs={"class": "a-price", "data-a-size": "xl"})
            product_image = content.find("img", attrs={"class": "s-image"})['src']
            asin = content.get("data-asin")
            uuid = content.get("data-uuid")
            if price != None:
                price = price.find("span", attrs={"class": "a-offscreen"}).text.strip()
                
                #  data dict here
                data_dict: dict[str, Any] = {
                    "title": title,
                    "product_link": product_link,
                    "asin": asin,
                    "uuid": uuid,
                    "product image": product_image
                }

                return data_dict
    
    def get_page_number(self, soup: BeautifulSoup):
        pages = soup.find("div", attrs={"class": "a-section a-text-center s-pagination-container", "role": "navigation"}).find("span", attrs={"class": "s-pagination-strip"}).find("span", attrs={"class": "s-pagination-item s-pagination-disabled", "aria-disabled": "true"})
        page = int(pages.text.strip())
        print("Total Page Number: {}".format(page))
        return page
    
    def get_product_detail(self, soup: BeautifulSoup):
        # response = httpx.get(url=url, headers={"User-Agent": self.ua.random})
        details: list = []
        contents = soup.find("div",attrs={"class": "a-section a-spacing-small a-spacing-top-small"}).find_all("div", attrs={"class": "a-row"})
        for content in contents:
            details.append(content.text.strip())

        return details


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
    
    def run(self):
        with open(join(BASE_DIR, 'response.html'), 'r') as f:
            soup: BeautifulSoup = BeautifulSoup(f.read(), 'html.parser')
            self.get_page_number(soup=soup)