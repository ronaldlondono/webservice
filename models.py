from peewee import *
import os
from peewee import PostgresqlDatabase

# Configuración de la base de datos
DATABASE_URL = ['DATABASE_URL']
if DATABASE_URL[0]:
    db = PostgresqlDatabase(DATABASE_URL[0], sslmode='require')
else:
    # Configuración local para desarrollo
    # Asegúrate de que estas credenciales sean correctas y seguras
    # No las compartas públicamente
    print("❌ DATABASE_URL no está configurada, usando configuración local")

db = PostgresqlDatabase(
    database='formativa_db',
    user='ronald',
    password='GaiUbnny4ZAWa6VEbmmTkiaZgHtuJcH3',
    host='dpg-d17f0cidbo4c73fs4nk0-a.oregon-postgres.render.com',
    port=5432,
    sslmode='require'  # Esto es crucial para Render
)

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