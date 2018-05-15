from collections import namedtuple
from itertools import cycle
import os
from trello import TrelloClient
from trello.exceptions import Unauthorized
# from .trello import client_list



FILE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '.trello'))

class FastTrello():

    def __init__(self):
        self.content = []
        with open(FILE_PATH, 'r') as f:
            for line in f.readlines():
                self.content.append(line.strip().split(','))
        self.clients = [TrelloClient(x[0], x[1]) for x in self.content]
        print(self.clients)
        # self.user_info = self.get_client()
        # self.clients = client_list
        pass

    # def get_client(self):
    #     for user in cycle(self.client_list):
    #         yield user_info
