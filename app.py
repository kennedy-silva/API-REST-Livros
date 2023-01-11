from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'O Senhor dos Aneis',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'titulo': 'Harry Potter',
        'autor': 'J.K Howling'
    },
    {
        'id': 3,
        'titulo': 'Filoteia',
        'autor': 'São Francisco de Sales'
    },
]

#obter todos os livros
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

#obter livro por ID
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

#editar um livro
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

#criar um novo livro
@app.route('/livros/addLivro', methods=['POST'])
def criar_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

# excluir livro de acordo com o ID
@app.route('/livros/excluir/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)


app.run(port=5000, host='localhost', debug=True)