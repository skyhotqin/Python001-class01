import scrapy
from scrapy.selector import Selector
from movies.items import MoviesItem
from scrapy.utils.response import get_base_url
import urllib.parse


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']
    top_n = 10

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse)

    def parse(self, response):
        base_url = get_base_url(response)
        movies = Selector(response=response).xpath('//dd')
        c = 0
        for movie in movies:
            c += 1
            if c == self.top_n:
                break
            hover_title = movie.xpath(
                './div[@class="movie-item film-channel"]/div[@class="movie-item-hover"]/a/div/div/text()')
            info = [i.strip() for i in hover_title.getall() if i.strip()]
            title = movie.xpath('./div[@class="channel-detail movie-item-title"]/a/text()')
            link = movie.xpath('./div[@class="channel-detail movie-item-title"]/a/@href')
            item = MoviesItem()
            item["source"] = self.name
            item["title"] = title.extract_first().strip()
            item["category"] = info[0]
            item["actor"] = info[1]
            item["release_time"] = info[2]
            item["link"] = urllib.parse.urljoin(base_url, link.extract_first().strip())
            yield scrapy.Request(url=item["link"], meta={"item": item},
                                 callback=self.parse_detail)

    def parse_detail(self, response):
        item = response.meta["item"]
        content = Selector(response=response).xpath('//div[@class="mod-content"]/span/text()')
        item["content"] = content.extract_first().strip()
        yield item
