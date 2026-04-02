README correspondiente a la Práctica 2

## Estructura del proyecto:
 /notebooks/: tiene los archivos Jupyter Notebook con el programa principal que corresponde a cada ejercicio.

 /src/: tiene el archivo "funciones_uso.py" con las funciones necesarias para resolver los ejercicios.

 ## Pasos para instalar el entorno:

 1. Bajar o clonar el repositorio

 2. Abrir la carpeta del proyecto en el entorno que se desee (en mi caso uso Visual Studio)

 3. Crear un entorno virtual para aislar el proyecto. En la terminal de comando escribir:
        python -m venv .venv

4. Activarlo según el sistema operativo:
    Windows: a mi me funcionó ".venv/Scripts/activate"

5. Instalar Jupyter en el entorno para poder correr los notebooks:
    pip install jupyter


## Ejecutar los ejercicios

Una vez que tenemos el entorno virtual activado:

1. Ir a la carpeta "notebooks" y abrir el archivo "ejercicio_10.ipynb"
2. Verificar que el kernel seleccionado sea el del entorno virtual
3. Correr el programa con normalidad (Run All)