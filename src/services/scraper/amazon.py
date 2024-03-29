import httpx, requests
import ssl, certifi

from httpx import Client
from typing import Any


from fake_useragent import UserAgent
from rich import print_json
from bs4 import BeautifulSoup
from os.path import join
from os import makedirs
from rich import print
from loguru import logger
from playwright.sync_api import sync_playwright


from core.settings.base import BASE_DIR, MEDIA_ROOT


class AmazonSpider(object):
    def __init__(self) -> None:
        self.base_url: str = "https://www.amazon.co.uk/s"
        self.ua: UserAgent = UserAgent()
        self.context = ssl.create_default_context()
        self.context.load_verify_locations(certifi.where())
        self.client: Client = Client(
            headers={"User-Agent": self.ua.random}, verify=self.context
        )

        # set Playwright browser
        self.PLAYWRIGHT_BROWSERS_PATH = join(BASE_DIR, "temp")

        # creating directory
        logger.info("Creating temporary directory")
        try:
            makedirs(join(BASE_DIR, "temp"))
        except FileExistsError:
            pass

         # creating directory
        logger.info("Creating screenshoot directory directory")
        try:
            makedirs(join(MEDIA_ROOT, "screenshoots"))
        except FileExistsError:
            pass

    def get_response(self, query: str, page_number: int = 1):
        params: dict[str, Any] = {
                "k": "{}".format(query),
                "page": "{}".format(page_number),
                "crid": "1ASBLLMQBJ4YW",
                "qid": "1698551383",
                "sprefix": "{},aps,504".format(query),
                "ref": "sr_pg_{}".format(page_number),
            }

        try:
            logger.info("Use httpx Module")
            response = self.client.get(self.base_url, params=params)
            if response == 200:
                logger.info(
                    "Process URL: {} Status {}".format(
                        response.url, response.status_code
                    )
                )

                # save html file
                f = open(join(BASE_DIR, "response.html"), "w+")
                f.write(response.text)
                f.close()

                print(
                    "Writing Response file: {} ".format(join(BASE_DIR, "response.html"))
                )

                # soup object
                soup: BeautifulSoup = BeautifulSoup(response.text, "html.parser")


                return soup

            elif response.status_code == 503:
                logger.info("Module Changed: Using requests module")

                response = httpx.get(
                    self.base_url,
                    params=params,
                    headers={"User-Agent": self.ua.chrome},
                    follow_redirects=True,
                )
                logger.info(
                    "Try to Process URL {} Status: {}".format(response.url, response.status_code)
                )

                # save html file
                f = open(join(BASE_DIR, "res.html"), "w+")
                f.write(response.text)
                f.close()

                logger.info(
                    "Writing Response file: {} ".format(join(BASE_DIR, "response.html"))
                )

                # soup object
                soup: BeautifulSoup = BeautifulSoup(response.text, "html.parser")

                return soup
        except:
            print("Error when using httpx, use requests module")
            response = requests.get(
                self.base_url, params=params, headers={"User-Agent": self.ua.chrome}
            )

            logger.error(
                "Returned Error: Try to Process URL {} Status: {}".format(
                    response.url, response.status_code
                )
            )

            # save html file
            f = open(join(BASE_DIR, "res_error.html"), "w+", encoding="UTF-8")
            f.write(response.text)
            f.close()

            logger.info(
                "Writing Response file: {} ".format(join(BASE_DIR, "response.html"))
            )

            # playwright handling
            
        
        # soup object
        
        soup: BeautifulSoup = BeautifulSoup(response.text, "html.parser")
        return soup


    def get_product(self, soup: BeautifulSoup) -> list[dict[str, Any]]:
        logger.info("Get Product ")
        products: list[dict[str, Any]] = []
        contents = soup.find_all(
            "div", attrs={"data-component-type": "s-search-result"}
        )
        logger.info("Total Data Scraped: {}".format(len(contents)))

        for content in contents:
            title = (
                content.find("h2", attrs={"class": "s-line-clamp-2"})
                .find("span")
                .text.strip()
            )
            product_link = (
                "https://www.amazon.co.uk"
                + content.find(
                    "a", attrs={"class": "a-link-normal", "class": "s-no-outline"}
                )["href"]
            )
            price = content.find(
                "span", attrs={"class": "a-price", "data-a-size": "xl"}
            )
            product_image = content.find("img", attrs={"class": "s-image"})["src"]
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
                    "product image": product_image,
                    "price": price,
                }
            else:
                data_dict: dict[str, Any] = {
                    "title": title,
                    "product_link": product_link,
                    "asin": asin,
                    "uuid": uuid,
                    "product image": product_image,
                    "price": "no price available",
                }
            products.append(data_dict)

        return products

    def get_page_number(self, soup: BeautifulSoup):
        pages = soup.find("span", attrs={"class": "s-pagination-strip"}).find(
            "span",
            attrs={
                "class": "s-pagination-item s-pagination-disabled",
                "aria-disabled": "true",
            },
        )
        page = int(pages.text.strip())
        print("Total Page Number: {}".format(page))
        return page

    def get_product_detail(self, url: str):
        details: list = []
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()

            # process the response
            page.goto(url=url, wait_until="load")
            
            logger.info("Process Product Detail on URL: {}".format(page.url))


            soup: BeautifulSoup = BeautifulSoup(page.content(), "html.parser")

            # save html file
            f = open(join(BASE_DIR, "response_detail.html"), "w+", encoding="UTF-8")
            f.write(page.content())
            f.close()

        # handling blocking here
        detect_captcha = soup.find("div", attrs={"class": "a-box-inner"}).find("p", attrs={"class": "a-last"}).text.strip()
        if detect_captcha == "Sorry, we just need to make sure you're not a robot. For best results, please make sure your browser is accepting cookies.":
            # proses screenshoot
            page.screenshot(join(join(MEDIA_ROOT, "screenshoot"), "blocking.png"))

            # proses screnshhot dengan solve capcha
            



            raise Exception("Captcha detected!")
        

        contents = soup.find(
            "div", attrs={"class": "a-section a-spacing-small a-spacing-top-small"}
        ).find_all("div", attrs={"class": "a-row"})
        for content in contents:
            details.append(content.text.strip())

        return details
