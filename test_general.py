from validaciones import capitalizar
from alumnos import (
    asistencia_total_ponderada,
    get_alumnos)

def test_capitalizar():
    assert capitalizar("hola") == "Hola"
    assert capitalizar("HOLA") == "Hola"
    assert capitalizar("") == ""
    assert capitalizar("python") != "PYTHON"



def test_asistencia_total_ponderada(): 
    total_ponderada = asistencia_total_ponderada()
    assert type(total_ponderada) == int or type(total_ponderada) == float # Verifica que el resultado sea un número
    assert total_ponderada >= 0 # Verifica que la asistencia total ponderada no sea negativa
    assert total_ponderada <= len(get_alumnos())  # Asumo que la asistencia total no puede ser mayor que el número de alumnos
    

