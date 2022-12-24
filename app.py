from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'O Senhor dos Aneis',
        'autor': 'J.R.R. Tolkien'
    },
    {
        'id': 2,
        'titulo': 'O principe',
        'autor': 'Maquiavel'
    },
    {
        'id': 3,
        'titulo': 'O código da Vinci',
        'autor': 'Dan Brown'
    }
]

# consultar (todos)
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

# consultar (id)
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_id(id):
    for livro in livros:
        if livro['id'] == id:
            return jsonify(livro)

# editar
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro['id'] == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

# criar
@app.route('/livros', methods=['POST'])
def adicionar_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)

# excluir
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro_id(id):
    for indice, livro in enumerate(livros):
        if livro['id'] == id:
            del livros[indice]

    return jsonify(livros)

app.run(port=5000, host= 'localhost', debug=True)