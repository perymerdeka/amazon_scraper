from typing import Any
from rich import print

from loguru import logger

from services.scraper.amazon import AmazonSpider
from services.scraper.extractor import Extractor


class Runner(object):
    def __init__(self, spider: AmazonSpider = AmazonSpider(), extractor: Extractor = Extractor()) -> None:
        self.spider: AmazonSpider = spider
        self.extractor: Extractor = extractor

    def search_product(self, keyword: str, page_number: int = 1):
        all_products: list[dict[str, Any]] = []
        soup = self.spider.get_response(query=keyword, page_number=page_number)
        pages = self.spider.get_page_number(soup=soup)

        for index, page in enumerate(range(1, pages), 1):
            logger.info("Process on page, {}".format(index))
            response = self.spider.get_response(query=keyword, page_number=page)
            products = self.spider.get_product(soup=response)

            # scrape process
            for product in products:
                detail = self.spider.get_product_detail(url=product["product_link"])
                product["detail product"] = detail
                all_products.append(product)

        return all_products
    
    def get_product_for_one_page(self, keyword: str, page_number: str):
        all_products: list[dict[str, Any]] = []
        logger.info("Process on page, {}".format(page_number))
        response = self.spider.get_response(query=keyword, page_number=page_number)
        products = self.spider.get_product(soup=response)

        # scrape process
        for product in products:
            detail = self.spider.get_product_detail(url=product["product_link"])
            product["detail product"] = detail
            all_products.append(product)

        return all_products