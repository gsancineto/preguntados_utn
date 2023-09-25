# A. Analizar detenidamente el set de datos.
# B. Recorrer la lista guardando en sub-listas: la pregunta, cada opción y la respuesta correcta.
# C. Crear 2 botones (rectángulos) uno con la etiqueta “Pregunta”, otro con la etiqueta “Reiniciar”
# D. Imprimir el Score: 999 donde se va a ir acumulando el puntaje de las respuestas correctas. Cada respuesta correcta suma 10 puntos.
# E. Al hacer clic en el botón (rectángulo) “Pregunta” debe mostrar las preguntas comenzando por la primera y las tres opciones, 
# cada clic en este botón pasa a la siguiente pregunta.
# F. Al hacer clic en una de las tres palabras que representa una de las tres opciones, si es correcta, debe sumar el score y dejar de mostrar las opciones.
# G. Solo tiene 2 opciones para acertar la respuesta correcta y sumar puntos, si agotó ambas opciones, deja de mostrar las opciones y no suma score
# H. Al hacer clic en el botón (rectángulo) “Reiniciar” debe mostrar las preguntas comenzando por la primera y las tres opciones, cada clic pasa a la siguiente pregunta. 
# También debe reiniciar el Score.

import pygame
from datos import lista
from constantes import *
from funciones import *

pygame.init()

screen = pygame.display.set_mode([ANCHO_VENTANA,ALTO_VENTANA])
running = True
logo = pygame.image.load(LOGO_URI)
scaled_logo = pygame.transform.scale(logo, (logo.get_width() / 2, logo.get_height() / 2))
font_buttons = pygame.font.SysFont(FONT_NAME, 36,pygame.font.Font.bold)
font_info = pygame.font.SysFont(FONT_NAME,24)
font_question = pygame.font.SysFont(FONT_NAME, 28)
font_attempts = pygame.font.SysFont(FONT_NAME, 18)
font_final_score = pygame.font.SysFont(FONT_NAME, 42)
normalized_list = normalize_list(lista)
index = None
question, answer_a, answer_b, answer_c, right_answer, attempts, score =reset()
final_score = str(score)
initialized = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False

        if event.type == pygame.MOUSEBUTTONDOWN:
            coordinates = pygame.mouse.get_pos()
            item_clicked = get_item_clicked(coordinates)
            if item_clicked == "BTN_QUESTION":
                initialized = True
                attempts = 2
                if index is None:
                    index = 0
                else:
                    index = index +1
            elif item_clicked == "BTN_RESET":
                index = None
            elif item_clicked is not None and attempts > 0:
                    attempts,index,score = handle_answer(item_clicked,right_answer,attempts,index,score)
            
            final_score = str(score)
            
            if index == len(lista)-1:
                index = None

    #fill background
    screen.fill(BACKGROUND_COLOR)

    #render logo
    logo_rect = scaled_logo.get_rect()
    logo_rect.center = (scaled_logo.get_width() -40,scaled_logo.get_height()-40)
    screen.blit(scaled_logo, logo_rect)

    #render boton pregunta
    pygame.draw.rect(screen,BUTTONS_COLOR,pygame.Rect(BTN_PREGUNTA_COORD))
    render_text(font_buttons,"PREGUNTA",screen,BTN_PREGUNTA_TXT_COORD)

    #render score
    render_text(font_info,"SCORE: " + str(score),screen,SCORE_COORD)

    #render boton reiniciar
    pygame.draw.rect(screen, BUTTONS_COLOR, pygame.Rect(BTN_RESET_COORD))
    render_text(font_buttons,"REINICIAR",screen,BTN_RESET_TXT_COORD)

    #render preguntas
    pygame.draw.rect(screen,QA_BG_COLOR,pygame.Rect(QA_BG_COORD))

    if index is not None:
        question = str(index +1) + ". " + normalized_list["questions"][index]
        right_answer = normalized_list["right"][index]
        answer_a = "A. " + normalized_list["a"][index]
        answer_b = "B. " + normalized_list["b"][index]
        answer_c = "C. " + normalized_list["c"][index]
        # render intentos
        render_text(font_attempts,"Intentos: " + str(attempts),screen,ATTEMPTS_COORD)
    else:
        if initialized:
            render_text(font_final_score,"SU PUNTAJE FINAL ES " + final_score,screen,FINAL_SCORE_COORD)
        question, answer_a, answer_b, answer_c, right_answer, attempts, score =reset()

    render_text(font_question,question,screen,QUESTION_COORD)
    if attempts > 0:
        render_text(font_info,answer_a,screen,ANSWER_A_COORD)
        render_text(font_info,answer_b,screen,ANSWER_B_COORD)
        render_text(font_info,answer_c,screen,ANSWER_C_COORD)
    
    pygame.display.flip()

pygame.quit