import pandas as pd

from loguru import logger
from typing import Any

class Extractor(object):
    def __init__(self) -> None:
        pass

    def extract_to_csv(self, datas: list[dict[str, Any]], filename: str):
        logger.info("Extract data to CSV")
        df = pd.DataFrame(datas, index=False)
        df.to_csv(filename, index=False)

    def extract_to_excel(self, datas: list[dict[str, Any]], filename: str):
        logger.info("Extract data to Excel")
        df = pd.DataFrame(datas, index=False)
        df.to_excel(filename, index=False)