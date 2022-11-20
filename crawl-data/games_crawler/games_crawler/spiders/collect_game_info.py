import scrapy
import json
import re

class collect_game_info(scrapy.Spider):
    name = 'games_info'

    def __init__(self):
        try:
            with open('dataset/game_urls.json') as f:
                self.games = json.load(f)

        except IOError:
            print("File not found")

    def start_requests(self):
        for game_url in self.games:
            yield scrapy.Request(url=game_url['game_url'], callback=self.parse)
            

        # yield scrapy.Request(url='https://www.metacritic.com/game/wii/metroid-prime-trilogy', callback=self.parse)

    def parse(self, response):
        title = response.xpath("//div[@class='product_title']//h1/text()").get()
        platform = response.xpath("//div[@class='product_title']//span/a/text()").get()
        
        if platform is None:
            platform = response.xpath("//div[@class='product_title']//span/text()").get()

        publisher = response.xpath("//div[@class='product_data']/ul/li[@class='summary_detail publisher']/span[@class='data']/a/text()").get()
        release_date = response.xpath("//div[@class='product_data']/ul/li[@class='summary_detail release_data']/span[@class='data']/text()").get()
        other_platforms = response.xpath("//div[@class='product_data']/ul/li[@class='summary_detail product_platforms']/span[@class='data']/a/text()").getall()

        if len(other_platforms) == 0:
            other_platforms = "NA"
        
        developer = response.xpath("//ul[@class='summary_details']/li[@class='summary_detail developer']/span[@class='data']/a/text()").getall()
        genres = response.xpath("//ul[@class='summary_details']/li[@class='summary_detail product_genre']/span[@class='data']/text()").getall()
        num_of_players = response.xpath("//ul[@class='summary_details']/li[@class='summary_detail product_players']/span[@class='data']/text()").get()

        if num_of_players is not None:
            num_of_players = num_of_players.strip()
        else:
            num_of_players = "NA"

        rating = response.xpath("//ul[@class='summary_details']/li[@class='summary_detail product_rating']/span[@class='data']/text()").get()

        if rating is None:
            rating = "NA"

        meta_score = response.xpath("//span[@itemprop='ratingValue']/text()").get()
        num_of_critic_reviews = response.xpath("//div[@class='score_summary metascore_summary']//div[@class='summary']//span[@class='count']/a/span/text()").get()

        user_score = response.xpath("//div[@class='userscore_wrap feature_userscore']/a/div/text()").get()
        num_of_user_reviews = response.xpath("//div[@class='score_summary']//div[@class='summary']//span[@class='count']/a/text()").get()
        num_of_user_reviews = re.findall(r'^[^\s]+', num_of_user_reviews)[0]

        data = {
            'Title': title,
            'Release date': release_date,
            'Platform': platform.strip(),
            'Other platforms': other_platforms,
            'Publisher': publisher.strip(),
            'Developer': developer,
            'Genres': genres,
            'Rating': rating,
            'Number of players': num_of_players,
            'Metascore': float(meta_score),
            'Number of critic reviews': int(num_of_critic_reviews.strip()),
            'User Score': float(user_score),
            'Number of user reviews': int(num_of_user_reviews)
        }

        # print(data)

        yield data
