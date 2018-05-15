from collections import Counter
from unittest import TestCase
from helper.helper import Helper


class HelperTests(TestCase):

    def setUp(self):
        self.helper = Helper()
        self.board = self.helper.add_board('Board Name')

    def test_board(self):
        self.assertEqual(self.board.name, 'Board Name')
        self.assertEqual(self.board.closed, False)
        self.board.close()
        self.assertEqual(self.board.closed, True)
        self.board.open()
        self.assertEqual(self.board.closed, False)
        self.assertEqual(self.board.id, 'Board Name_id')
        self.assertEqual(self.board.open_lists(), [])
        self.assertEqual(self.board.open_cards(), [])
        self.assertEqual(self.board.get_labels(), [])

    def test_list(self):
        trello_list_1 = self.board.add_list('List 1')
        trello_list_2 = self.board.add_list('List 2')
        trello_list_3 = self.board.add_list('List 3')
        self.assertEqual(self.board.open_lists(), [trello_list_1, trello_list_2, trello_list_3])

    def test_card(self):
        trello_list_1 = self.board.add_list('List 1')
        trello_list_2 = self.board.add_list('List 2')
        trello_list_3 = self.board.add_list('List 3')
        card_1 = trello_list_1.add_card('Card 1')
        card_2 = trello_list_1.add_card('Card 2')
        card_3 = trello_list_1.add_card('Card 3')
        self.assertEqual(trello_list_1.list_cards(), [card_1, card_2, card_3])

    def test_create_test_data(self):
        boards = self.helper.create_test_data()
        board_names = [board.name for board in boards]
        expected_boards = ['imaging', 'vector', 'claims', 'infrastructure', 'mips', 'misc', 'apps']
        self.assertCountEqual(board_names, expected_boards)
        expected_lists = {'coding done': 7, 'qa': 7, 'in progress': 7, 'production': 7, 'final qa': 7, 'backlog': 7}
        list_counter = Counter()
        for board in boards:
            list_counter += Counter([trello_list.name for trello_list in board.open_lists()])
        self.assertEqual(dict(list_counter), expected_lists)
        label_counter = Counter()
        no_labels = []
        for board in boards:
            cards = board.open_cards()
            for card in cards:
                if card.labels:
                    label_counter += Counter([label.name for label in card.list_labels])
                else:
                    no_labels.append(card)
        self.assertEqual(len(no_labels), 42)
        expected_labels = {'task': 126, 'production feedback': 84, 'staging feedback': 42}
        self.assertEqual(dict(label_counter), expected_labels)
