from typing import Literal
from plataforms import Github
from cache import Manager

class CrawlerController:
    def __init__(self, plataform: Literal["github", "codeberg", "gitlab"]):
        pass