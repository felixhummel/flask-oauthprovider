import pytest

@pytest.fixture()
def app():
    from demoprovider import app
    return app

@pytest.fixture()
def client(app):
    app.config['TESTING'] = True
    return app.test_client()

@pytest.fixture()
def client_creds(app):
    from demoprovider.provider import ExampleProvider
    x = ExampleProvider(app)
    return {
            'key': x.generate_client_key(),
            'secret': x.generate_client_secret()
    }

def test(client):
    response = client.get('/')
    assert response.status_code == 200

def test_client_creds(client_creds):
    assert len(client_creds['key']) == 30
    assert len(client_creds['secret']) == 30

def test_login(client):
    # get renders form
    response = client.get('/login')
    assert response.status_code == 200
    # POST redirects
    response = client.post('/login?next=http://example.org/test?qoo=qux', data=dict(username='foo', password='bar'))
    assert response.status_code == 302
    assert response.location == 'http://example.org/test?qoo=qux'

