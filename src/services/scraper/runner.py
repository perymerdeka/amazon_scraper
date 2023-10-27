from typing import Any
from rich import print

from loguru import logger

from services.scraper.amazon import AmazonSpider


class Runner(object):
    def __init__(self, spider: AmazonSpider = AmazonSpider()) -> None:
        self.spider: AmazonSpider = spider

    def search_product(self, keyword: str, page_number: int = 1):
        all_products: list[dict[str, Any]] = []
        soup = self.spider.get_response(query=keyword, page_number=page_number)

        pages = self.spider.get_page_number(soup=soup)

        for index, page in enumerate(range(1, pages)):
            logger.info("Process on page, {}".format(index))
            response = self.spider.get_response(query=keyword, page_number=page)
            products = self.spider.get_product(soup=response)

            # scrape process
            for product in products:
                detail = self.spider.get_product_detail(url=product["product url"])
                product["detail product"] = detail
                all_products.append(product)

        return all_products
