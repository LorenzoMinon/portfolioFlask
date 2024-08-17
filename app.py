from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') # Home page

def inicio():
    return render_template('index.html')

@app.route('/about') # About page

def sobre_mi():
    return render_template('about.html')

@app.route('/proyectos')

def proyectos():
    return render_template('proyectos.html')

@app.route('proyectos/<int:proyecto_id>')

def proyecto_detalle(proyecto_id):
    return render_template('proyecto_detalle.html', proyecto_id=proyecto_id)    

if __name__ == '__main__':
    app.run(debug=True)