from flask import Flask, jsonify, request
from flask_cors import CORS
from models import Libro

app = Flask(__name__)
CORS(app)  # Habilitar CORS para GitHub Pages

@app.route('/')
def home():
    return jsonify({
        "message": "Bienvenido a la API de Biblioteca",
        "endpoints": {
            "GET /libros": "Listar todos los libros",
            "POST /libros": "Crear nuevo libro",
            "PUT /libros/<id>": "Actualizar libro",
            "DELETE /libros/<id>": "Eliminar libro"
        }
    })

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
    try:
        data = request.get_json()
        
        # Validar que existan datos
        if not data:
            return jsonify({'error': 'Datos no proporcionados'}), 400
            
        libro = Libro.get_by_id(id)
        
        # Actualizar solo los campos proporcionados
        if 'titulo' in data:
            libro.titulo = data['titulo']
        if 'autor' in data:
            libro.autor = data['autor']
        if 'año_publicacion' in data:
            # Asegurar que sea un número
            try:
                libro.año_publicacion = int(data['año_publicacion'])
            except (TypeError, ValueError):
                return jsonify({'error': 'Año de publicación inválido'}), 400
        if 'genero' in data:
            libro.genero = data['genero']
        if 'prestado' in data:
            # Convertir a booleano
            libro.prestado = bool(data['prestado'])
        
        libro.save()
        return jsonify({
            'message': 'Libro actualizado',
            'libro': {
                'id': libro.id,
                'titulo': libro.titulo,
                'autor': libro.autor,
                'año_publicacion': libro.año_publicacion,
                'genero': libro.genero,
                'prestado': libro.prestado
            }
        })
    except Libro.DoesNotExist:
        return jsonify({'error': 'Libro no encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/libros/<int:id>', methods=['DELETE'])
def delete_libro(id):
    libro = Libro.get_by_id(id)
    libro.delete_instance()
    return jsonify({'message': 'Libro eliminado'}), 200

if __name__ == '__main__':
    app.run()