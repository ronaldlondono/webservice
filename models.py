from peewee import *
import os
import urllib.parse
from playhouse.db_url import connect

DATABASE_URL = os.getenv('DATABASE_URL')
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL no está configurada")

# Parsear la URL para manejar SSL
url = urllib.parse.urlparse(DATABASE_URL)
db = connect(DATABASE_URL)


class Libro(Model):
    id = AutoField()
    titulo = CharField(max_length=100)
    autor = CharField(max_length=100)
    año_publicacion = IntegerField()
    genero = CharField(max_length=50)
    prestado = BooleanField(default=False)

    class Meta:
        database = db

# Manejo de errores para conexión
try:
    db.connect()
    db.create_tables([Libro], safe=True)
    print("✅ Conectado a la base de datos y tablas creadas")
except Exception as e:
    print(f"❌ Error de conexión: {e}")