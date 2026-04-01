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


def analizar_playlist(playlist):
    total_segundos = 0

    mas_larga = playlist[0]
    mas_corta = playlist[0]

    for cancion in playlist:
        tiempo_split = cancion["duration"].split(':')
        minutos = int(tiempo_split[0])
        segundos = int(tiempo_split[1])

        duracion_seg = (minutos * 60) + segundos
        total_segundos += duracion_seg

        if duracion_seg > (int(mas_larga["duration"].split(':')[0]) * 60 + int(mas_larga["duration"].split(':')[1])):
            mas_larga = cancion
        if duracion_seg < (int(mas_corta["duration"].split(':')[0]) * 60 + int(mas_corta["duration"].split(':')[1])):
            mas_corta = cancion

    total_m = total_segundos // 60
    total_s = total_segundos % 60 

    print(f"Duración total: {total_m}m {total_s}s")
    print(f'Canción más larga: "{mas_larga["title"]}" ({mas_larga["duration"]})')
    print(f'Canción más corta: "{mas_corta["title"]}" ({mas_corta["duration"]})')

def filtrar_spoilers (texto, palabras_spoiler):
    lista_spoilers = palabras_spoiler.split(', ')

    texto_filtrado = texto

    for spoiler in lista_spoilers:
        palabra = spoiler.strip()

        reemplazo = '*' * len(palabra)

        texto_filtrado = texto_filtrado.replace(palabra, reemplazo)
        texto_filtrado = texto_filtrado.replace(palabra.lower(), reemplazo)
        texto_filtrado = texto_filtrado.replace(palabra.capitalize(), reemplazo)

    return texto_filtrado


def validar_email(email):
    if email.count('@') != 1:
        return False
    
    if email.startswith('@') or email.endswith('@') or email.startswith('.') or email.endswith('.'):
        return False
    
    derecha = email.split('@')[1]
    if '.' not in derecha:
        return False
    
    punto = email.split('.')
    dom = punto[-1]
    if len(dom) < 2:
        return False
    
    return True