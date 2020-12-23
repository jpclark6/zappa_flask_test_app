import pytest

from rest_api import app


@pytest.fixture
def client():
    app.app.config['TESTING'] = True

    with app.app.test_client() as client:
        yield client

def test_empty_db(client):
    """Start with a blank database."""

    rv = client.get('/')
    assert b'Hello, World!' == rv.data

def test_mock_email(client):
    emails = [{'email': 'test_email_1@example.com'}, {'email': 'test_email_2@example.com'}]

    rv = client.post('/email', json=emails)

    assert rv.json == {'emailsSaved': ['test_email_1@example.com', 'test_email_2@example.com'], 'status': 'success'}