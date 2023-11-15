from constantes import *

# Recibe: un item en pantalla
# Devuelve: una tupla correspondiente a sus limites en el eje X
def get_x(item):
    return (item[0],item[0]+item[2])

# Recibe: un item en pantalla
# Devuelve: una tupla correspondiente a sus limites en el eje Y
def get_y(item):
    return (item[1], item[1]+item[3])

# Recibe: un item en pantalla
# Devuelve: sus coordenadas especificas
def get_item_coordinates(item):
    return (get_x(item),get_y(item))

# Recibe: Las coordenadas donde se clickeo la pantalla y un item especifico de la pantalla
# Devuelve:
    # True: si las coordenadas estan dentro de las coordenadas de ese item
    # False: si no corresponden
def is_coord_in_range(input_coordinates, item):
    x = input_coordinates[0]
    y = input_coordinates[1]

    coord_range = get_item_coordinates(item)

    x_range = coord_range[0]
    y_range = coord_range[1]

    if (x>=x_range[0] and x<=x_range[1]) and (y>=y_range[0] and y<= y_range[1]):
        return True
    
    return False

# Recibe: las coordenadas donde se clickeo en pantalla
# Devuelve: el item que fue clickeado
def get_item_clicked(input_coordinates):
    for coordinate in CLICKABLE_COORDS:
        for key,value in coordinate.items():
            if is_coord_in_range(input_coordinates,value):
                return key

# Recibe: una lista de preguntas, respuestas, y rta correcta
# Devuelve: un diccionario de listas
def normalize_list(lista):
    questions = [pregunta["pregunta"] for pregunta in lista]
    a = [pregunta["a"] for pregunta in lista]
    b = [pregunta["b"] for pregunta in lista]
    c = [pregunta["c"] for pregunta in lista]
    right = [pregunta["correcta"] for pregunta in lista]

    return {"questions": questions, "a": a, "b": b, "c": c, "right": right}

# Recibe:
    # item_clicked: El item en pantalla que fue clickeado
    # right_answer: La respuesta correcta
    # attempts: Intentos que le quedan al usuario
    # index: El numero de pregunta
    # score: El puntaje del jugador
# Evalua si la respuesta es correcta o no
# Devuelve un array con:
    # attempts: Intentos restantes
    # index: El numero de pregunta siguiente (puede ser el mismo)
    # score: El puntaje resultante
def handle_answer(item_clicked,right_answer,attempts,index,score):
    answer = ""
    if item_clicked == "ANSWER_A":
        answer = "a"
    elif item_clicked == "ANSWER_B":
        answer = "b"
    elif item_clicked == "ANSWER_C":
        answer = "c"


    if answer == right_answer:
        score = score + 10
        index = index + 1
        attempts = 2
    elif attempts > 0:
        attempts = attempts - 1
    else:
        attempts = 0

    return [attempts, index, score]

# Devuelve un array con valores iniciales
def reset():
    #question, answer_a, answer_b, answer_c, right_answer, attempts, score
    return["","","","","",2,0]

#Recibe:
    # font: El obj fuente
    # text: Lo que se quiere renderizar
    # screen: El obj pantalla
    # coordinates: Las coordenadas donde se quiere renderizar
def render_text(font,text,screen,coordinates):
    txt_render = font.render(text, True, COLOR_BLANCO)
    screen.blit(txt_render,coordinates)