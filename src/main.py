from services.scraper.amazon import AmazonSpider


spider = AmazonSpider()

print(spider.get_suggest())