from wework.contact.testcase.token import Weiwork


class TestWeixin:
    def test_get_token(self):
        assert Weiwork.get_token() != ""
