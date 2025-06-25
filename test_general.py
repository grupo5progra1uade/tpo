from validaciones import capitalizar
from alumnos import (
    alumnos_presentes,
    asistencia_total_ponderada,
    get_alumnos)

def test_capitalizar():
    assert capitalizar("hola") == "Hola"
    assert capitalizar("HOLA") == "Hola"
    assert capitalizar("") == ""
    assert capitalizar("python") != "PYTHON"


"""def test_alumnos_presentes(): # Test para verificar que la función alumnos_presentes() devuelve una lista de alumnos presentes (Osea, con estado 1 en el subindice 4)
    presentes = alumnos_presentes()
    assert len(presentes) > 0  
    for alumno in presentes:
        assert alumno[4] == 1  # Verifica que el estado sea 1 (presente)
        assert type(alumno) == list  # Verifica que cada alumno sea una lista
        assert len(alumno) == 5  # Verifica que cada alumno tenga 5 elementos


def test_get_alumnos(): # 
    alumnos = get_alumnos()
    assert len(alumnos) > 0
    for alumno in alumnos:
        assert type(alumno) == list
        assert len(alumno) == 5
        assert type(alumno[0]) == int  # legajo
        assert type(alumno[1]) == str  # apellido
        assert type(alumno[2]) == str  # nombre
        assert type(alumno[3]) == str  # fecha
        assert type(alumno[4]) == int  # estado"""

def test_asistencia_total_ponderada(): 
    total_ponderada = asistencia_total_ponderada()
    assert type(total_ponderada) == int or type(total_ponderada) == float # Verifica que el resultado sea un número
    assert total_ponderada >= 0 # Verifica que la asistencia total ponderada no sea negativa
    assert total_ponderada <= len(get_alumnos())  # Asumo que la asistencia total no puede ser mayor que el número de alumnos
    

