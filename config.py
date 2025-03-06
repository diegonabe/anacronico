import os

class Config:
    # Configuración de la base de datos
    SQLALCHEMY_DATABASE_URI = 'postgresql://diego:ruudkrkr@localhost:5432/tu_basededatos'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configuración de seguridad
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave_secreta_segura'

    # Otras configuraciones relevantes para Flask
    DEBUG = True  # Cambia a False en producción
