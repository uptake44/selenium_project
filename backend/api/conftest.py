import pytest


@pytest.fixture
def public_api_fixture():
    pass

@pytest.fixture
def api_overwrite_fixture() -> str:
    return "public, not overwritten"
