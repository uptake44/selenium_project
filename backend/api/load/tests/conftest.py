import pytest
from random import randint

@pytest.fixture
def load_only():
    pass

@pytest.fixture
def api_overwrite_fixture():
    return randint(1, 100)