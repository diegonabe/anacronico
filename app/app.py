from flask import Blueprint, render_template, request, redirect, url_for, session
from werkzeug.security import check_password_hash
from app.models import db, Contenido, Usuario  # Importar la base de datos y el modelo

main = Blueprint('main', __name__)

@main.route('/')
def home():
    contenidos = Contenido.query.order_by(Contenido.fecha_creacion.desc()).all()
    return render_template('index.html', contenidos=contenidos)  # Pasar datos a la plantilla

@main.route('/manager', methods=['GET', 'POST'])
def manager():
    if request.method == 'POST':
        titulo = request.form['titulo']
        resumen = request.form['resumen']
        texto = request.form['texto']

        # Guardar en la base de datos
        nuevo_contenido = Contenido(titulo=titulo, resumen=resumen, texto=texto)
        db.session.add(nuevo_contenido)
        db.session.commit()

        return redirect(url_for('main.manager'))  # Redirigir a la misma página

    return render_template('admin.html')  # Renderizar la plantilla del formulario

@main.route('/post/<int:post_id>')
def show_post(post_id):
    post = Contenido.query.get_or_404(post_id)  # Busca el post o muestra error 404 si no existe
    return render_template('post.html', post=post)  # Renderiza la plantilla de lectura

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        pin = request.form['pin']
        user = Usuario.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.pin_hash, pin):
            session['user_id'] = user.id  # Guardar usuario en sesión
            return redirect(url_for('main.manager'))
        
    return render_template('login.html')

@main.route('/logout')
def logout():
    session.pop('user_id', None)  # Eliminar usuario de la sesión
    flash('Sesión cerrada', 'info')
    return redirect(url_for('main.login'))
