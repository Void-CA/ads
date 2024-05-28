import datetime

class Persona:
    """
    Representa a una persona con un nombre y una fecha de nacimiento.

    Attributes:
        nombre (str): El nombre de la persona.
        FechaNacimiento (datetime.datetime): La fecha de nacimiento de la persona.
        edad (int): La edad calculada de la persona.
    """

    def __init__(self, nombre: str, fecha_nacimiento: datetime.datetime):
        """
        Inicializa una nueva instancia de la clase Persona.

        Args:
            nombre (str): El nombre de la persona.
            fecha_nacimiento (datetime.datetime): La fecha de nacimiento de la persona.
        """
        self.nombre = nombre
        self.FechaNacimiento = fecha_nacimiento
        self.edad = self.__CalcularEdad()
        
    def __CalcularEdad(self) -> int:
        """
        Calcula la edad de la persona basado en la fecha de nacimiento.

        Returns:
            int: La edad calculada de la persona.
        """
        today = datetime.datetime.today()
        birthday_passed = (today.month, today.day) < (self.FechaNacimiento.month, self.FechaNacimiento.day)
        return today.year - self.FechaNacimiento.year - birthday_passed
    
    def saludar(self) -> None:
        """
        Imprime un saludo con el nombre y la edad de la persona.
        """
        print("Que onda soy " + self.nombre + " tengo " + str(self.edad))
    

class Alumno(Persona):
    """
    Representa a un alumno que es una persona con un carnet de estudiante.

    Attributes:
        carnet (str): El carnet de estudiante del alumno.
    """

    def __init__(self, nombre: str, fecha_nacimiento: datetime.datetime, carnet: str):
        """
        Inicializa una nueva instancia de la clase Alumno.

        Args:
            nombre (str): El nombre del alumno.
            fecha_nacimiento (datetime.datetime): La fecha de nacimiento del alumno.
            carnet (str): El carnet de estudiante del alumno.
        """
        super().__init__(nombre, fecha_nacimiento)
        self.carnet = carnet
    
    def saludar(self) -> None:
        """
        Imprime un saludo con el nombre y el carnet del alumno.
        """
        print("Que onda soy " + self.nombre + " y soy estudiante, este es mi carnet " + self.carnet)


class Profesor(Persona):
    """
    Representa a un profesor que es una persona con un título, jefatura, y contrato.

    Attributes:
        Id_Profesor (int): El identificador único del profesor.
        Titulo (str): El título del profesor.
        Jefatura (str): La jefatura del profesor.
        Contrato (TipoContrato): El tipo de contrato del profesor.
    """

    def __init__(self, nombre: str, fecha_nacimiento: datetime.datetime, id_profesor: str, titulo: str, jefatura: str, contrato):
        """
        Inicializa una nueva instancia de la clase Profesor.

        Args:
            nombre (str): El nombre del profesor.
            fecha_nacimiento (datetime.datetime): La fecha de nacimiento del profesor.
            id_profesor (int): El identificador único del profesor.
            titulo (str): El título del profesor.
            jefatura (str): La jefatura del profesor.
            contrato (TipoContrato): El tipo de contrato del profesor.
        """
        super().__init__(nombre, fecha_nacimiento)
        self.Id_Profesor = id_profesor
        self.Titulo = titulo
        self.Jefatura = jefatura
        self.Contrato = contrato
        
    def saludar(self) -> None:
        """
        Imprime un saludo con el nombre, el título, y el rol del profesor.
        """
        print(f"Hola soy {self.nombre}, soy {self.Titulo} y profesor de ULSA")


class Asignatura:
    """
    Representa una asignatura con un ID, nombre y número de créditos.

    Attributes:
        Id_Asignatura (int): El identificador único de la asignatura.
        Nombre (str): El nombre de la asignatura.
        Creditos (int): El número de créditos de la asignatura.
    """

    def __init__(self, id: str, nombre: str, creditos: int):
        """
        Inicializa una nueva instancia de la clase Asignatura.

        Args:
            id (int): El identificador único de la asignatura.
            nombre (str): El nombre de la asignatura.
            creditos (int): El número de créditos de la asignatura.
        """
        self.Id_Asignatura = id
        self.Nombre = nombre
        self.Creditos = creditos

class Curso:
    """
    Representa un curso con un ID, una lista de alumnos, una asignatura, ciclo académico, modalidad, notas y un profesor.

    Attributes:
        Id_Curso (int): El identificador único del curso.
        Alumnos (list): La lista de alumnos inscritos en el curso.
        Asignatura (Asignatura): La asignatura del curso.
        CicloAcademico (str): El ciclo académico del curso.
        Modalidad (str): La modalidad del curso (presencial, online, etc.).
        Notas (dict): Un diccionario con las notas de los alumnos.
        Profesor (Profesor): El profesor del curso.
    """

    def __init__(self, id_curso: str, alumnos: list, asignatura: Asignatura, ciclo_academico: str, modalidad: str, notas: dict, profesor: Profesor):
        """
        Inicializa una nueva instancia de la clase Curso.

        Args:
            id_curso (int): El identificador único del curso.
            alumnos (list): La lista de alumnos inscritos en el curso.
            asignatura (Asignatura): La asignatura del curso.
            ciclo_academico (str): El ciclo académico del curso.
            modalidad (str): La modalidad del curso (presencial, online, etc.).
            notas (dict): Un diccionario con las notas de los alumnos.
            profesor (Profesor): El profesor del curso.
        """
        self.Id_Curso = id_curso
        self.Alumnos = alumnos
        self.Asignatura = asignatura
        self.CicloAcademico = ciclo_academico
        self.Modalidad = modalidad
        self.Notas = notas
        self.Profesor = profesor
    

    def AgregarAlumno(self, alumno: Alumno) -> bool:
        """
        Agrega un alumno a la lista de alumnos del curso si no está ya presente.

        Args:
            alumno (Alumno): El alumno a agregar.

        Returns:
            bool: True si el alumno fue agregado, False si ya estaba en la lista.
        """
        if alumno not in self.Alumnos:
            self.Alumnos.append(alumno)
            return True
        return False
    

    def EliminarAlumno(self, alumno: Alumno) -> bool:
        """
        Elimina un alumno de la lista de alumnos del curso si está presente.

        Args:
            alumno (Alumno): El alumno a eliminar.

        Returns:
            bool: True si el alumno fue eliminado, False si no estaba en la lista.
        """
        if alumno in self.Alumnos:
            self.Alumnos.remove(alumno)
            return True
        return False
    

    def RegistrarNota(self, alumno: Alumno, nota: float) -> None:
        """
        Registra la nota de un alumno en el curso.

        Args:
            alumno (Alumno): El alumno cuya nota se va a registrar.
            nota (float): La nota a registrar.
        """
        if alumno in self.Alumnos:
            self.Notas[alumno] = nota
    
    
    def ObtenerNotas(self) -> dict:
        """
        Obtiene el diccionario de notas de los alumnos del curso.

        Returns:
            dict: El diccionario de notas de los alumnos.
        """
        return self.Notas
        