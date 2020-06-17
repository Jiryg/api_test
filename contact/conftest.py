import pytest
from wework.contact.testcase.token import Weiwork


@pytest.fixture(scope="session")
def token():
    return Weiwork.get_token_new()