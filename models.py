from peewee import *
import os

# Configuración de la base de datos
DATABASE_URL = 'postgresql://ronald:GaiUbnny4ZAWa6VEbmmTkiaZgHtuJcH3@dpg-d17f0cidbo4c73fs4nk0-a.oregon-postgres.render.com/formativa_db?sslmode=require'
db = PostgresqlDatabase(DATABASE_URL)

class Libro(Model):
    id = AutoField()
    titulo = CharField(max_length=100)
    autor = CharField(max_length=100)
    año_publicacion = IntegerField()
    genero = CharField(max_length=50)
    prestado = BooleanField(default=False)

    class Meta:
        database = db

db.connect()
db.create_tables([Libro], safe=True)