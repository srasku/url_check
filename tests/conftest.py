"""
Test configuration
"""
import pytest

from url_check import create_app


@pytest.fixture
def app():
    """
    Fixture to create app to connect to.
    """
    the_app = create_app()
    yield the_app


@pytest.fixture
def client(app):  # pylint: disable=redefined-outer-name
    """
    Fixture to create client for tests
    """
    return app.test_client()


@pytest.fixture
def runner(app):  # pylint: disable=redefined-outer-name
    """
    Test runner for the app's Click commands.
    This allows us to run the `init-db` command from tests.
    """
    return app.test_cli_runner()
