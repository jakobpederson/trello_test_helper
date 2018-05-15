from concurrent.futures import ThreadPoolExecutor
from itertools import cycle
import os
from trello import TrelloClient
from trello.exceptions import Unauthorized
# from .trello import client_list



FILE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '.trello'))

class FastTrello():

    def __init__(self):
        print(FILE_PATH)
        self.user_info = self.get_client()
        self.clients = client_list
        pass

    def get_client(self):
        for user in cycle(self.client_list):
            yield user_info
