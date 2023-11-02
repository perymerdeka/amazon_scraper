import json
from loguru import logger
from typing import Any
from glob import glob
from os.path import join

class Dump(object):
    def dump_json(self, datas: list[dict[str, Any]], filename: str) -> None:
        with open("{}.json".format(filename), 'w+') as f:
            json.dump(datas, f)

    def dump_from_directory(self, path: str) -> list[dict[str, Any]]: 
        json_data: list[dict[str, Any]] = []
    
        # Menggunakan glob untuk mencocokkan semua file JSON dalam direktori
        json_files: list[str] = glob(join(path, '*.json'))
        
        # Loop melalui file JSON yang ditemukan
        for json_file in json_files:
            try:
                with open(json_file, 'r') as file:
                    # Membaca data JSON dari file dan menambahkannya ke list json_data
                    data = json.load(file)
                    json_data.append(data)
            except Exception as e:
                logger.error(f"Error reading {json_file}: {e}")
        
        return json_data
