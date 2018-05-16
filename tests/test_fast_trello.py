from unittest import TestCase

from helper.fast_trello import FastTrello


class FastBuilderTests(TestCase):

    def test_cycle_generator(self):
        builder = FastTrello()
        self.assertEqual('a', builder.user_info.__next__().api_key)
        self.assertEqual('b', builder.user_info.__next__().api_key)
        self.assertEqual('c', builder.user_info.__next__().api_key)
        self.assertEqual('a', builder.user_info.__next__().api_key)
        self.assertEqual('b', builder.user_info.__next__().api_key)
        self.assertEqual('c', builder.user_info.__next__().api_key)
