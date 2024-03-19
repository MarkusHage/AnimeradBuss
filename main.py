import pygame, sys
from button import Button
import random

size = width, height = (1280, 720)


pygame.init()
running = True
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bosses Buss")

passagerarlista = []

def get_font(size):
    return pygame.font.Font("./assets/font.ttf", size)

""" def checkForInput(self, position):
    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
        return True
    return False """


def lägg_till_ny_passagerare():
    if len(passagerarlista) < 25:
        RandomÅlder = random.randint(5,99)
        passagerarlista.append(RandomÅlder)
        print(f"En passagerare som är {RandomÅlder} år gammal hoppade på bussen. Totalt {len(passagerarlista)} passagerare på bussen.")
    else:
       print("Tyvärr grabbar, inga slots lediga. Bussen är full.") 
        
def skriv_ut_lista():
    if len(passagerarlista) > 0:
        print(passagerarlista)
    else:
        print("Bussen är tom!")

def skriv_ut_sammanlagd_ålder():
    if len(passagerarlista) > 0:
        print(sum(passagerarlista))
    else:
        print("Bussen är tom!")

def avsluta():
    print("Avslutar programmet...")
    running = False

        

#def skriv_ut_lista   

while running:
    screen.fill("black")

    mouse_position = pygame.mouse.get_pos()

    meny_text = get_font(40).render("Bosses Buss", True, "#b68f40")
    meny_rect = meny_text.get_rect(center=(640, 100))

    lägg_till_ny_passagerare_knapp = get_font(20).render("Lägg till passagerare", True, "#b68f40")
    lägg_till_ny_passagerare_knapp_hover = get_font(20).render("Lägg till passagerare", True, "#7ec0ee")
    lägg_till_ny_passagerare_rect = lägg_till_ny_passagerare_knapp.get_rect(center=(640, 200))

    skriv_ut_lista_knapp = get_font(20).render("Skriv ut ålder på passagerare", True, "#b68f40")
    skriv_ut_lista_rect = skriv_ut_lista_knapp.get_rect(center=(640, 350))

    skriv_ut_sammmanlagd_ålder_knapp = get_font(20).render("Skriv ut sammanlagd ålder", True, "#b68f40")
    skriv_ut_sammanlagd_ålder_rect = skriv_ut_sammmanlagd_ålder_knapp.get_rect(center=(640, 500))

    avsluta_knapp = get_font(20).render("Avsluta", True, "#b68f40")
    avsluta_rect = avsluta_knapp.get_rect(center=(640, 650))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            if lägg_till_ny_passagerare_rect.collidepoint(mouse_position):
                    screen.blit(lägg_till_ny_passagerare_knapp_hover, lägg_till_ny_passagerare_rect)
            if skriv_ut_lista_rect.collidepoint(mouse_position):
                    print("Musen är över skriv ut lista-knappen")
            if skriv_ut_sammanlagd_ålder_rect.collidepoint(mouse_position):
                    print("Musen är över sammanlagd ålder-knappen")
            if avsluta_rect.collidepoint(mouse_position):
                    print("Musen är över avsluta-knappen")
            if event.type == pygame.MOUSEBUTTONDOWN:
                if lägg_till_ny_passagerare_rect.collidepoint(mouse_position):
                    lägg_till_ny_passagerare()
                if skriv_ut_lista_rect.collidepoint(mouse_position):
                    skriv_ut_lista()
                if skriv_ut_sammanlagd_ålder_rect.collidepoint(mouse_position):
                    skriv_ut_sammanlagd_ålder()
                if avsluta_rect.collidepoint(mouse_position):
                    running = False
            
    screen.blit(meny_text, meny_rect)
    screen.blit(lägg_till_ny_passagerare_knapp, lägg_till_ny_passagerare_rect)
    screen.blit(skriv_ut_lista_knapp, skriv_ut_lista_rect)
    screen.blit(skriv_ut_sammmanlagd_ålder_knapp, skriv_ut_sammanlagd_ålder_rect)
    screen.blit(avsluta_knapp, avsluta_rect)
    
    pygame.display.update()

pygame.quit()
