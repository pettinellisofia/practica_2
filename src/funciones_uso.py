import random
import string

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


def calcular_costoenvio (peso, zona):
    zona = zona.lower()

    zonas_validas = ["local", "regional", "nacional"]
    if zona not in zonas_validas:
        return f"Zona no válida. Las zonas disponibles son_ {', '.join(zonas_validas)}."
    
    costo = 0

    if peso <= 1:
        if zona == "local": costo = 500
        elif zona == "regional": costo = 1000
        else: costo = 2000
    elif 1 < peso <= 5:
        if zona == "local": costo = 1000
        elif zona == "regional": costo = 2500
        else: costo = 4500
    else:
        if zona == "local": costo = 2000
        elif zona == "regional": costo = 5000
        else: costo = 8000

    return f"Costo de envío: ${costo}"


def analizar_hashtags(lista_posts):
    conteo_hstgs = {}

    for post in lista_posts:
        palabras = post.split()
        for palabra in palabras:
            if palabra.startswith('#'):
                if palabra in conteo_hstgs:
                    conteo_hstgs[palabra] += 1
                else:
                    conteo_hstgs[palabra] = 1
    print("Hashtags trending con más de una aparición:")

    for hashtag, cantidad in conteo_hstgs.items():
        if cantidad > 1:
            print(f"{hashtag}: {cantidad} veces")

    total_unicos = len(conteo_hstgs)
    print(f"Total de hashtags únicos: {total_unicos}")   


def sortear_amigo_inv(nombres):
    lista_nom = nombres.split(', ')
    participantes = []

    for nombre in lista_nom:
        nombre_ok = nombre.strip().title()

        if nombre_ok not in participantes:
            participantes.append(nombre_ok)
    
    if len(participantes) < 3:
        print("Se necesitan al menos 3 participantes para realizar el sorteo.")
        return
    
    random.shuffle(participantes)

    print("Resultados del sorteo de amigo invisible:")

    for i in range(len(participantes)):
        if i == len(participantes) - 1:
            amigo_asig = participantes[0]
        else:
            amigo_asig = participantes[i + 1]
        print(f"{participantes[i]} le regala a {amigo_asig}")


def cifrado_cesar (mensaje, desplaza):
    abc_min = string.ascii_lowercase
    abc_may = string.ascii_uppercase

    cifrado = [
        abc_min[(abc_min.index(c) + desplaza) % 26] if c in abc_min else
        abc_may[(abc_may.index(c) + desplaza) % 26] if c in abc_may else 
        c

        for c in mensaje
    ]
    return "".join(cifrado)


def descifrar_mensaje (mensaje, desplazamiento):
    return cifrado_cesar(mensaje, -desplazamiento)


def limpiar_alumnos (lista_alumnos):
    alumnos = {}

    for alu in lista_alumnos:
        alumno_ok = alu['name']
        nota = alu['grade']
        
        if alumno_ok is not None and alumno_ok.strip() != "":
            if nota is not None and str(nota).isdigit():
                nombre_listo = alumno_ok.strip().title()
                nota_ok = int(nota)
            
                prolijo = alu['status'].strip().title() if alu['status'] else "Sin estado"
                
                if nombre_listo not in alumnos or nota_ok > alumnos[nombre_listo]['grade']:
                    alumnos[nombre_listo] = {'grade': nota_ok, 'status': prolijo}

    return sorted(alumnos.items())

