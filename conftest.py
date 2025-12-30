import pytest
from random import randint


@pytest.fixture
def public_fixture():
    return randint(1, 100)
