from flask_frozen import Freezer
from app import app  # Importa la aplicación Flask desde tu archivo app.py

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
