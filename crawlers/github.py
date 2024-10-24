import playwright
from .universal import Crawler

class GithubCrawler(Crawler):
    def __init__(self, cache: classmethod, plataform: classmethod):
        super().__init__(cache, plataform)