# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pandas as pd


class MoviesPipeline:

    def process_item(self, item, spider):
        my_list = [item["source"], item["title"], item["category"], item["release_time"], item["actor"], item["link"],
                   item["content"]]
        movie = pd.DataFrame(data=my_list)
        movie.to_csv("./movie.csv", encoding="utf8", mode="a", index=False, header=False)
        return item
