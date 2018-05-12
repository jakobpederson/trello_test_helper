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

