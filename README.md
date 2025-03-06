1. README.md (Descripción del proyecto)
Este archivo explica el proyecto y cómo usarlo.


# CMS Project - El Anacrónico 📰

Este es un CMS (Sistema de Gestión de Contenidos) minimalista y eficiente, diseñado para portales de noticias. Permite la creación, gestión y visualización de artículos en orden cronológico.

## 📌 Características
- Publicación de artículos con título, resumen y contenido.
- Listado de artículos en la página principal, mostrando los más recientes primero.
- Enlace a cada artículo para su lectura detallada.
- Diseño tipo periódico en blanco y negro.

## 🚀 Instalación y ejecución

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/TuUsuario/cms_project.git
   cd cms_project
Crear un entorno virtual e instalar dependencias

bash
Copiar
Editar
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
pip install -r requirements.txt
Configurar la base de datos

bash
Copiar
Editar
flask db upgrade
Ejecutar la aplicación

bash
Copiar
Editar
flask run
📄 Estructura del Proyecto
arduino
Copiar
Editar
cms_project/
│── app/
│   ├── templates/
│   │   ├── index.html
│   │   ├── post.html
│   ├── static/
│   │   ├── styles.css
│   ├── models.py
│   ├── app.py
│   ├── __init__.py
│── migrations/ (control de versiones de la DB)
│── config.py
│── requirements.txt
│── README.md
│── .gitignore
✨ Tecnologías utilizadas
Python + Flask
PostgreSQL + SQLAlchemy
HTML + CSS
¡Gracias por visitar este proyecto! 🚀