from unittest import TestCase

from helper.fast_trello import FastTrello


class FastBuilderTests(TestCase):

    def setUp(self):
        self.builder = FastTrello()
        self.var = self.builder.user_info

    def test_cycle_generator(self):
        self.assertEqual('a', self.var.__next__().api_key)
        self.assertEqual('b', self.var.__next__().api_key)
        self.assertEqual('c', self.var.__next__().api_key)
        self.assertEqual('x', self.var.__next__().api_secret)
        self.assertEqual('y', self.var.__next__().api_secret)
        self.assertEqual('z', self.var.__next__().api_secret)
        self.assertEqual('a', self.var.__next__().api_key)
        self.assertEqual('b', self.var.__next__().api_key)
        self.assertEqual('c', self.var.__next__().api_key)
