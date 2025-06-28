# Gestión de Profesores - Sistema de Asistencia

## Nuevas Funcionalidades Implementadas

### 1. Almacenamiento en JSON
- Los datos de los profesores ahora se almacenan en el archivo `profesores.json`
- Persistencia de datos entre sesiones
- Carga automática al iniciar el programa

### 2. Funciones Principales

#### Cargar Profesores (`cargar_profesores()`)
- Carga los profesores desde el archivo JSON
- Si el archivo no existe, crea uno con datos por defecto
- Manejo de errores de lectura/escritura

#### Guardar Profesores (`guardar_profesores()`)
- Guarda los cambios en el archivo JSON
- Codificación UTF-8 para caracteres especiales
- Manejo de errores de escritura

#### Eliminar Profesor (`eliminar_profesor()`)
- Muestra lista de profesores disponibles
- Solicita ID del profesor a eliminar
- Confirmación antes de eliminar
- Guarda cambios automáticamente en JSON

### 3. Menú Actualizado

El menú de profesores ahora incluye:
1. Ingresar
2. Cargar nuevo profesor
3. Modificar profesor
4. Mostrar listado de profesores
5. Cambiar contraseña
6. **Eliminar profesor** (NUEVO)
7. Salir

### 4. Estructura del Archivo JSON

```json
{
    "1": {
        "nombre": "Maria",
        "apellido": "Gonzalez",
        "email": "maria@gmail.com",
        "contraseña": "Contra123",
        "seguridad": "Pepita",
        "materia": "Matematica"
    }
}
```

### 5. Funciones Modificadas

Todas las funciones que modifican datos ahora:
- Guardan automáticamente los cambios en JSON
- Manejan errores de escritura
- Proporcionan feedback al usuario

### 6. Archivos Modificados

- `profesores.py`: Funciones principales de gestión
- `main.py`: Menú actualizado con opción de eliminar
- `profesores.json`: Archivo de almacenamiento (se crea automáticamente)
- `test_profesores.py`: Script de pruebas

### 7. Uso

1. **Ejecutar el programa principal:**
   ```bash
   python main.py
   ```

2. **Ejecutar pruebas:**
   ```bash
   python test_profesores.py
   ```

3. **Eliminar un profesor:**
   - Seleccionar opción 6 en el menú de profesores
   - Elegir el ID del profesor a eliminar
   - Confirmar la eliminación

### 8. Características de Seguridad

- Confirmación antes de eliminar profesores
- Validación de IDs antes de eliminar
- Restauración automática en caso de error de escritura
- Manejo de errores de archivo JSON

### 9. Compatibilidad

- Mantiene compatibilidad con el código existente
- Los datos existentes se migran automáticamente a JSON
- No requiere cambios en otros módulos del sistema 