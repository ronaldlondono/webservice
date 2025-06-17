from peewee import *
import os
from peewee import PostgresqlDatabase

# Lee la URL de la variable de entorno
db_url = os.getenv('DATABASE_URL')
if not db_url:
    raise RuntimeError("❌ DATABASE_URL no está configurada")
# Peewee permite pasar sslmode en la URL
db = PostgresqlDatabase(db_url, sslmode='require')


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