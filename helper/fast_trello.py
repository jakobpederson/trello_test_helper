from collections import namedtuple
from itertools import cycle
import os
from trello import TrelloClient
from trello.exceptions import Unauthorized

FILE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '.trello'))


class FastTrello():

    def __init__(self):
        self.content = []
        with open(FILE_PATH, 'r') as f:
            for line in f.readlines():
                self.content.append(line.strip().split(','))
        self.client_list = self.content
        self.user_info = self.get_client()

    def get_client(self):
        for user in cycle(self.client_list):
            yield TrelloClient(user[0], user[1])
