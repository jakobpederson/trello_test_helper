LIST_NAMES = ('backlog', 'in progress', 'production', 'coding done', 'qa', 'final qa')
TRELLO_BOARDS = ('vector', 'imaging', 'claims', 'apps', 'mips', 'infrastructure', 'misc')
LABELS = (
    ('task', 'red'),
    ('production feedback', 'blue'),
    ('staging feedback', 'green'),
    ('q1', 'black'),
)

class Helper():

    def __init__(self):
        self.boards = []

    def add_board(self, name):
        return DummyBoard(name)

    def create_test_data(self):
        for board_name in TRELLO_BOARDS:
            board = self.add_test_lists(DummyBoard('{}'.format(board_name)))
            self.add_test_labels_to_board(board)
            self.boards.append(board)
        return self.boards

    def add_test_labels_to_board(self, board):
        for label in LABELS:
            label = DummyLabel(label[0], label[1])
            board.add_label(label)
        return board

    def add_test_lists(self, board):
        for list_name in LIST_NAMES:
            trello_list = board.add_list(list_name)
            self.add_test_cards(trello_list)
        return board

    def add_test_cards(self, trello_list):
        for j in range(1, 5):
            new_card = trello_list.add_card('List {} Card {}'.format(trello_list.name, j))
            self.add_test_labels(new_card, j)
        return trello_list

    def add_test_labels(self, card, count):
        for label in ADD_LABELS[count]:
            card.add_label(label)
        return card

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

ADD_LABELS = {
    1: (),
    2: (DummyLabel(LABELS[0][0], LABELS[0][1]),),
    3: (DummyLabel(LABELS[0][0], LABELS[0][1]), DummyLabel(LABELS[1][0], LABELS[1][1])),
    4: (DummyLabel(LABELS[0][0], LABELS[0][1]), DummyLabel(LABELS[1][0], LABELS[1][1]), DummyLabel(LABELS[2][0], LABELS[2][1]))
}
