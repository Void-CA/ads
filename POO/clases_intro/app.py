from flask import Flask, render_template, request, redirect, url_for
import datetime
from models import Alumno, Profesor

app = Flask(__name__)

datos_guardados = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    nombre = request.form['nombre']
    fecha_nacimiento = datetime.datetime.strptime(request.form['fecha_nacimiento'], '%Y-%m-%d')
    tipo = request.form['tipo']

    if tipo == 'alumno':
        carnet = request.form['carnet']
        alumno = Alumno(nombre, fecha_nacimiento, carnet)
        datos_guardados.append(f"Alumno: {alumno.nombre}, Fecha de Nacimiento: {alumno.FechaNacimiento}, Carnet: {alumno.carnet}, Edad: {alumno.edad}")
        alumno.saludar()
    elif tipo == 'profesor':
        id_profesor = request.form['id_profesor']
        titulo = request.form['titulo']
        jefatura = request.form['jefatura']
        contrato = request.form['contrato']
        profesor = Profesor(nombre, fecha_nacimiento, id_profesor, titulo, jefatura, contrato)
        profesor.saludar()
        datos_guardados.append(f"Profesor: {profesor.nombre}, Fecha de Nacimiento: {profesor.FechaNacimiento}, ID: {profesor.Id_Profesor}, Título: {profesor.Titulo}, Jefatura: {profesor.Jefatura}, Contrato: {profesor.Contrato}, Edad: {profesor.edad}")
    return redirect(url_for('index'))


@app.route('/visualize')
def visualize():
    return render_template('visualize.html', datos=datos_guardados)


if __name__ == '__main__':
    app.run(debug=True)
