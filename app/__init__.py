import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from dotenv import load_dotenv 

#Cargar las variables de entorno
load_dotenv()

#crear instancia
app =  Flask(__name__)

# Configuración de la base de datos PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#Importar los modelos
from app.models import Category
from app.models import Post

#Importar las rutas
from app.routes.category import categories_bp
from app.routes.post import posts_bp

app.register_blueprint(categories_bp, url_prefix='/categories')
app.register_blueprint(posts_bp, url_prefix='/posts')

#Ruta Raiz
@app.route('/')
def index():
    return "Hola Mundo"