from flask import Flask, jsonify, request
from flask_cors import CORS
from models import Libro

app = Flask(__name__)
CORS(app)  # Habilitar CORS para GitHub Pages

@app.route('/libros', methods=['GET'])
def get_libros():
    libros = Libro.select()
    return jsonify([{
        'id': libro.id,
        'titulo': libro.titulo,
        'autor': libro.autor,
        'año_publicacion': libro.año_publicacion,
        'genero': libro.genero,
        'prestado': libro.prestado
    } for libro in libros])

@app.route('/libros', methods=['POST'])
def create_libro():
    data = request.get_json()
    libro = Libro.create(
        titulo=data['titulo'],
        autor=data['autor'],
        año_publicacion=data['año_publicacion'],
        genero=data['genero']
    )
    return jsonify({'id': libro.id}), 201

@app.route('/libros/<int:id>', methods=['PUT'])
def update_libro(id):
    data = request.get_json()
    libro = Libro.get_by_id(id)
    libro.titulo = data.get('titulo', libro.titulo)
    libro.autor = data.get('autor', libro.autor)
    libro.año_publicacion = data.get('año_publicacion', libro.año_publicacion)
    libro.genero = data.get('genero', libro.genero)
    libro.prestado = data.get('prestado', libro.prestado)
    libro.save()
    return jsonify({'message': 'Libro actualizado'})

@app.route('/libros/<int:id>', methods=['DELETE'])
def delete_libro(id):
    libro = Libro.get_by_id(id)
    libro.delete_instance()
    return jsonify({'message': 'Libro eliminado'}), 200

if __name__ == '__main__':
    app.run()