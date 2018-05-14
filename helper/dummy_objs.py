class TrelloBase():

    def __init__(self, name):
        self.name = name
        self.closed = False
        self.id = name + '_id'

    def close(self):
        self.closed = True

    def open(self):
        self.closed = False


class DummyBoard(TrelloBase):

    def __init__(self, name):
        self.trello_lists = []
        self.labels = []
        super().__init__(name)

    def open_lists(self):
        return self.trello_lists

    def open_cards(self):
        cards = []
        for trello_list in self.trello_lists:
            cards.extend(trello_list.list_cards())
        return cards

    def add_list(self, name):
        new_list = DummyList(name)
        self.trello_lists.append(new_list)
        return new_list

    def add_label(self, label):
        self.labels.append(label)

    def get_labels(self):
        return self.labels


class DummyList(TrelloBase):

    def __init__(self, name):
        self.cards = []
        super().__init__(name)

    def add_card(self, name):
        new_card = DummyCard(name)
        self.cards.append(new_card)
        return new_card

    def list_cards(self, card_filter="open"):
        card_state = {
            "open": False,
            "closed": True
        }
        return [card for card in self.cards if card.closed == card_state[card_filter]]


class DummyCard(TrelloBase):

    def __init__(self, name):
        self.labels = []
        super().__init__(name)

    @property
    def list_labels(self):
        return self.labels

    def set_closed(self):
        self.closed = True

    def add_label(self, label):
        self.labels.append(label)


class DummyLabel(TrelloBase):

    def __init__(self, name, color):
        self.color = color
        super().__init__(name)
