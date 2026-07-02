import pytest
import server

@pytest.fixture(scope="session", autouse=True)
def close_server():
    """Ensure the test server is closed after all tests run."""
    yield
    server.close()
