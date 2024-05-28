import os
import sys
import datetime
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models import Persona, Alumno, Profesor, Asignatura, Curso


def test_persona_init():
    ari = Persona("Ari", datetime.datetime(2004, 9, 30))
    assert ari.nombre == "Ari"
    assert ari.FechaNacimiento == datetime.datetime(2004, 9, 30)
    assert ari.edad == datetime.datetime.today().year - 2004 - ((datetime.datetime.today().month, datetime.datetime.today().day) < (9, 30))

def test_alumno_init():
    alumno = Alumno("Ari", datetime.datetime(2004, 9, 30), "20210001")
    assert alumno.nombre == "Ari"
    assert alumno.FechaNacimiento == datetime.datetime(2004, 9, 30)
    assert alumno.carnet == "20210001"

def test_profesor_init():
    profesor = Profesor("Dr. John Doe", datetime.datetime(1980, 5, 15), 1, "PhD", "Matemáticas", "Contratado")
    assert profesor.nombre == "Dr. John Doe"
    assert profesor.FechaNacimiento == datetime.datetime(1980, 5, 15)
    assert profesor.Id_Profesor == 1
    assert profesor.Titulo == "PhD"
    assert profesor.Jefatura == "Matemáticas"
    assert profesor.Contrato == "Contratado"

def test_asignatura_init():
    asignatura = Asignatura("MAT101", "Matemáticas", 4)
    assert asignatura.Id_Asignatura == "MAT101"
    assert asignatura.Nombre == "Matemáticas"
    assert asignatura.Creditos == 4

def test_curso_init():
    asignatura = Asignatura("MAT101", "Matemáticas", 4)
    profesor = Profesor("Dr. John Doe", datetime.datetime(1980, 5, 15), 1, "PhD", "Matemáticas", "Contratado")
    curso = Curso("CUR101", [], asignatura, "2024-1", "Presencial", {}, profesor)
    assert curso.Id_Curso == "CUR101"
    assert curso.Alumnos == []
    assert curso.Asignatura == asignatura
    assert curso.CicloAcademico == "2024-1"
    assert curso.Modalidad == "Presencial"
    assert curso.Notas == {}
    assert curso.Profesor == profesor

def test_curso_agregar_alumno():
    asignatura = Asignatura("MAT101", "Matemáticas", 4)
    profesor = Profesor("Dr. John Doe", datetime.datetime(1980, 5, 15), 1, "PhD", "Matemáticas", "Contratado")
    curso = Curso("CUR101", [], asignatura, "2024-1", "Presencial", {}, profesor)
    alumno = Alumno("Ari", datetime.datetime(2004, 9, 30), "20210001")
    assert curso.AgregarAlumno(alumno) == True
    assert curso.AgregarAlumno(alumno) == False

def test_curso_eliminar_alumno():
    asignatura = Asignatura("MAT101", "Matemáticas", 4)
    profesor = Profesor("Dr. John Doe", datetime.datetime(1980, 5, 15), 1, "PhD", "Matemáticas", "Contratado")
    curso = Curso("CUR101", [], asignatura, "2024-1", "Presencial", {}, profesor)
    alumno = Alumno("Ari", datetime.datetime(2004, 9, 30), "20210001")
    curso.AgregarAlumno(alumno)
    assert curso.EliminarAlumno(alumno) == True
    assert curso.EliminarAlumno(alumno) == False

def test_curso_registrar_nota():
    asignatura = Asignatura("MAT101", "Matemáticas", 4)
    profesor = Profesor("Mero abraham", datetime.datetime(1980, 5, 15), 1, "MSc", "Matemáticas", "Contratado")
    curso = Curso("CUR101", [], asignatura, "2024-1", "Presencial", {}, profesor)
    alumno = Alumno("Ari", datetime.datetime(2004, 9, 30), "20210001")
    curso.AgregarAlumno(alumno)
    curso.RegistrarNota(alumno, 95.0)
    assert curso.Notas[alumno] == 95.0

def test_curso_obtener_notas():
    asignatura = Asignatura("ADS101", "Analisis y Disenio de Sistemas", 4)
    profesor = Profesor("Aarock Cisneros", datetime.datetime(1980, 5, 15), 1, "Ing", "Sistemas", "Diario")
    curso = Curso("CUR101", [], asignatura, "2024-1", "Presencial", {}, profesor)
    alumno = Alumno("Ari", datetime.datetime(2004, 9, 30), "20210001")
    curso.AgregarAlumno(alumno)
    curso.RegistrarNota(alumno, 95.0)
    notas = curso.ObtenerNotas()
    assert notas[alumno] == 95.0

if __name__ == "__main__":
    pytest.main()
