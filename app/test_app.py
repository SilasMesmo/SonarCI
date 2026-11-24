import pytest
from app import app, somar, dividir

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_somar():
    assert somar(2, 3) == 5
    assert somar(-1, 1) == 0

def test_dividir():
    assert dividir(10, 2) == 5

def test_dividir_por_zero():
    with pytest.raises(ValueError):
        dividir(10, 0)

def test_frontend_carrega(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"App de Teste da Esteira" in response.data

def test_frontend_calculo(client):
    response = client.post("/", data={"a": "10", "b": "5", "operacao": "somar"})
    assert response.status_code == 200
    assert b"Resultado: 15.0" in response.data