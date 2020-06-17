from unittest import TestCase

from wework.contact.testcase.token import Weiwork


class TestWeixin(TestCase):
    def test_get_token(self):
        print(Weiwork.get_token())
        assert Weiwork.get_token() !=""