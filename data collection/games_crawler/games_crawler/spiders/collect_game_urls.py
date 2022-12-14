import scrapy

class collect_game_url(scrapy.Spider):
    name = 'game_urls'

    list_url = []

    def start_requests(self):
        urls = [
            'https://www.metacritic.com/browse/games/score/metascore/all/all/filtered?sort=desc&page=0',
            'https://www.metacritic.com/browse/games/score/metascore/all/all/filtered?sort=desc&page=1',
            'https://www.metacritic.com/browse/games/score/metascore/all/all/filtered?sort=desc&page=2',
            'https://www.metacritic.com/browse/games/score/metascore/all/all/filtered?sort=desc&page=3',
            'https://www.metacritic.com/browse/games/score/metascore/all/all/filtered?sort=desc&page=4',
            'https://www.metacritic.com/browse/games/score/metascore/all/all/filtered?sort=desc&page=5',
            'https://www.metacritic.com/browse/games/score/metascore/all/all/filtered?sort=desc&page=6',
            'https://www.metacritic.com/browse/games/score/metascore/all/all/filtered?sort=desc&page=7',
            'https://www.metacritic.com/browse/games/score/metascore/all/all/filtered?sort=desc&page=8',
            'https://www.metacritic.com/browse/games/score/metascore/all/all/filtered?sort=desc&page=9',
            'https://www.metacritic.com/browse/games/score/metascore/all/all/filtered?sort=desc&page=10',
            'https://www.metacritic.com/browse/games/score/metascore/all/all/filtered?sort=desc&page=11',
            'https://www.metacritic.com/browse/games/score/metascore/all/all/filtered?sort=desc&page=12',
            'https://www.metacritic.com/browse/games/score/metascore/all/all/filtered?sort=desc&page=13',
            'https://www.metacritic.com/browse/games/score/metascore/all/all/filtered?sort=desc&page=14',
            ]

        # urls1 = [
        #     'https://www.metacritic.com/browse/games/score/metascore/year/all/filtered?year_selected=2022&distribution=&sort=desc&view=detailed',
        #     'https://www.metacritic.com/browse/games/score/metascore/year/all/filtered?year_selected=2021&distribution=&sort=desc&view=detailed',
        #     'https://www.metacritic.com/browse/games/score/metascore/year/all/filtered?year_selected=2020&distribution=&sort=desc&view=detailed',
        #     'https://www.metacritic.com/browse/games/score/metascore/year/all/filtered?year_selected=2019&distribution=&sort=desc&view=detailed',
        #     'https://www.metacritic.com/browse/games/score/metascore/year/all/filtered?year_selected=2018&distribution=&sort=desc&view=detailed',
        #     'https://www.metacritic.com/browse/games/score/metascore/year/all/filtered?year_selected=2017&distribution=&sort=desc&view=detailed',
        #     'https://www.metacritic.com/browse/games/score/metascore/year/all/filtered?year_selected=2016&distribution=&sort=desc&view=detailed',
        #     'https://www.metacritic.com/browse/games/score/metascore/year/all/filtered?year_selected=2015&distribution=&sort=desc&view=detailed',
        #     'https://www.metacritic.com/browse/games/score/metascore/year/all/filtered?year_selected=2014&distribution=&sort=desc&view=detailed',
        #     'https://www.metacritic.com/browse/games/score/metascore/year/all/filtered?year_selected=2013&distribution=&sort=desc&view=detailed',
        #     'https://www.metacritic.com/browse/games/score/metascore/year/all/filtered?year_selected=2012&distribution=&sort=desc&view=detailed',
        #     'https://www.metacritic.com/browse/games/score/metascore/year/all/filtered?year_selected=2011&distribution=&sort=desc&view=detailed',
        #     'https://www.metacritic.com/browse/games/score/metascore/year/all/filtered?year_selected=2010&distribution=&sort=desc&view=detailed',
        #     'https://www.metacritic.com/browse/games/score/metascore/year/all/filtered?year_selected=2009&distribution=&sort=desc&view=detailed',
        #     'https://www.metacritic.com/browse/games/score/metascore/year/all/filtered?year_selected=2008&distribution=&sort=desc&view=detailed',
        #     'https://www.metacritic.com/browse/games/score/metascore/year/all/filtered?year_selected=2007&distribution=&sort=desc&view=detailed',
        #     'https://www.metacritic.com/browse/games/score/metascore/year/all/filtered?year_selected=2006&distribution=&sort=desc&view=detailed',
        #     'https://www.metacritic.com/browse/games/score/metascore/year/all/filtered?year_selected=2005&distribution=&sort=desc&view=detailed',
        #     'https://www.metacritic.com/browse/games/score/metascore/year/all/filtered?year_selected=2004&distribution=&sort=desc&view=detailed',
        #     'https://www.metacritic.com/browse/games/score/metascore/year/all/filtered?year_selected=2003&distribution=&sort=desc&view=detailed',
        #     'https://www.metacritic.com/browse/games/score/metascore/year/all/filtered?year_selected=2002&distribution=&sort=desc&view=detailed',
        #     'https://www.metacritic.com/browse/games/score/metascore/year/all/filtered?year_selected=2001&distribution=&sort=desc&view=detailed',
        #     'https://www.metacritic.com/browse/games/score/metascore/year/all/filtered?year_selected=2000&distribution=&sort=desc&view=detailed',
        # ]

        for url in urls:
            data = scrapy.Request(url=url, callback=self.parse)
            yield data

    def parse(self, response):
        game_urls = response.xpath('//td[@class="clamp-summary-wrap"]/a/@href').getall()
        # print(game_urls)
        for game_url in game_urls:
            yield {
                'game_url': 'https://www.metacritic.com' + game_url
            }
