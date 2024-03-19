import pygame, sys
from button import Button
import random

pygame.init()
running = True

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Bosses Buss")

PassagerarLista = []

def get_font(size):
    return pygame.font.Font("./assets/font.ttf", size)


def lägg_till_ny_passagerare()
    if len(PassagerarLista) < 25:
        RandomÅlder = random.randint(5,99)
        PassagerarLista += RandomÅlder
        

#def skriv_ut_lista   

while running:
    screen.fill("black")

    mouse_position = pygame.mouse.get_pos()

    meny_text = get_font(40).render("Bosses Buss", True, "#b68f40")
    meny_rect = meny_text.get_rect(center=(640, 100))

    lägg_till_ny_passagerare_knapp = get_font(20).render("Lägg till passagerare", True, "#b68f40")
    lägg_till_ny_passagerare_rect = lägg_till_ny_passagerare_knapp.get_rect(center=(640, 200))

    skriv_ut_lista_knapp = get_font(20).render("Skriv ut ålder på passagerare", True, "#b68f40")
    skriv_ut_lista_rect = skriv_ut_lista_knapp.get_rect(center=(640, 300))

    screen.blit(meny_text, meny_rect)
    screen.blit(lägg_till_ny_passagerare_knapp, lägg_till_ny_passagerare_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if lägg_till_ny_passagerare_knapp.checkForInput(mouse_position):
                lägg_till_ny_passagerare()
            if skriv_ut_lista.checkForInput(mouse_position):
                skriv_ut_passagerare()
            if skriv_ut_sammanlagd_ålder.checkForInput(mouse_position):
                skriv_ut_sammanlagd_ålder()
            if avsluta.checkForInput(mouse_position):
                running = False
            

    
    pygame.display.update()

pygame.quit()
