from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Category

categories_bp = Blueprint('categories', __name__)

# Ruta para ver todas las categorías
@categories_bp.route('/')
def listar_categorias():
    categorias = Category.query.all()
    return render_template('categories/listar_categorias.html', categories=categorias)

#Ruta /categories crear una nueva categoría
@categories_bp.route('/new', methods=['GET','POST'])
def add_category():
    if request.method == 'POST':
        name = request.form['nombre']
        new_category = Category(name=name)
        db.session.add(new_category)
        db.session.commit()

        return redirect(url_for('categories.listar_categorias'))
    
    #Aqui sigue si es GET
    return render_template('categories/create_category.html')

#Actualizar categoria
@categories_bp.route('/update/<int:id>', methods=['GET','POST'])
def update_category(id):
    category = Category.query.get(id)
    if request.method == 'POST':
        category.name = request.form['nombre']
        db.session.commit()
        return redirect(url_for('categories.listar_categorias'))
    
    return render_template('categories/update_category.html', category=category)

#Eliminar categoria
@categories_bp.route('/delete/<int:id>')
def delete_category(id):
    category = Category.query.get(id)
    if category:
        db.session.delete(category)
        db.session.commit()
    return redirect(url_for('categories.listar_categorias'))