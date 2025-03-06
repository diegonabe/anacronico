from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    # Importar después de definir app para evitar ciclos
    from app.app import main
    app.register_blueprint(main)

    with app.app_context():  # Asegurar que la app esté en contexto
        from app.models import Contenido  # Importar modelos aquí
        db.create_all()  # Crear tablas si no existen

    return app

