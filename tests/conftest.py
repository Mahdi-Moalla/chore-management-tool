import pytest


@pytest.fixture(scope='session', autouse=True)
def _enable_db():
    """Enable database access for all tests."""
    yield
