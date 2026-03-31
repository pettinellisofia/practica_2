def analizar_texto(text):
    lineas = text.split('\n')
    total_lineas = len(lineas)

    palabras = text.split()
    total_palabras = len(palabras)

    promedio = total_palabras / total_lineas

    print(f"Total de líneas: {total_lineas}")
    print(f"Total de palabras: {total_palabras}")
    print(f"Promedio de palabras por línea: {str(promedio)[:4]}")
    print(f"Lineas por encima del promedio ({str(promedio)[:4]} palabras):")

    for linea in lineas:
        palabras_linea = linea.split()
        cantidad = len(palabras_linea)

        if cantidad > promedio:
            print(f'  - "{linea}" ({cantidad} palabras)')