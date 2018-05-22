from helper.dummy_objs import DummyBoard, DummyLabel

LIST_NAMES = ('backlog', 'in progress', 'production', 'coding done', 'qa', 'final qa')
TRELLO_BOARDS = ('vector', 'imaging', 'claims', 'apps', 'mips', 'infrastructure', 'misc')
LABELS = (
    DummyLabel('task', 'red'),
    DummyLabel('production feedback', 'blue'),
    DummyLabel('staging feedback', 'green'),
    DummyLabel('q1', 'black'),
)
ADD_LABELS = {
    1: (),
    2: (LABELS[0],),
    3: (LABELS[0], LABELS[1]),
    4: (LABELS[0], LABELS[1], LABELS[2])
}


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

