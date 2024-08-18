from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/sobre-mi')
def sobre_mi():
    return render_template('sobre_mi.html')

@app.route('/proyectos')
def proyectos():
    return render_template('proyectos.html')

@app.route('/proyecto/<int:proyecto_id>')
def proyecto_detalle(proyecto_id):
    # Aquí puedes cargar los detalles de un proyecto según su ID
    return render_template('proyecto_detalle.html', proyecto_id=proyecto_id)

if __name__ == '__main__':
    app.run(debug=True)
