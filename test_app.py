from app import app


def test_status_api():
    client = app.test_client()

    resposta = client.get("/")

    assert resposta.status_code == 200
    assert resposta.json["status"] == "online"


def test_lista_produtos():
    client = app.test_client()

    resposta = client.get("/produtos")

    assert resposta.status_code == 200
    assert len(resposta.json) == 3
    
def test_lista_usuarios():
    client = app.test_client()

    resposta = client.get("/usuarios")

    assert resposta.status_code == 200
    assert len(resposta.json) == 3
    assert resposta.json[0]["nome"] == "João"