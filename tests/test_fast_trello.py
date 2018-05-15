from unittest import TestCase

from helper.fast_builder import FastBuilder


class FastBuilderTests(TestCase):

    def test_x(self):
        builder = FastBuilder()
        print(builder.user_info.next())
        self.fail('x')
