from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def inicio():
    return jsonify({
        "mensagem": "Nova versão publicada com CI/CD!",
        "status": "online"
    })


@app.route("/produtos")
def produtos():
    return jsonify([
        {
            "id": 1,
            "nome": "Notebook",
            "preco": 3500.00
        },
        {
            "id": 2,
            "nome": "Mouse",
            "preco": 80.00
        },
        {
            "id": 3,
            "nome": "Teclado",
            "preco": 150.00
        },
        {
            "id": 4,
            "nome": "Tablet",
            "preco": 2200.00
        }
    ])


@app.route("/usuarios")
def usuarios():
    return jsonify([
        {
            "id": 1,
            "nome": "João"
        },
        {
            "id": 2,
            "nome": "Maria"
        },
        {
            "id": 3,
            "nome": "Carlos"
        },
        {
            "id": 4,
            "nome": "Vinicius"
        }
    ])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)