from http import HTTPStatus

from fastapi.testclient import TestClient

from simplefastapi.app import app


def test_root_retorna_ok_e_hello_world():
    client = TestClient(app)
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'Olá': 'Mundo!'}
