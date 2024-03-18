import pygame, sys
from button import Button

pygame.init()
running = True

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Bosses Buss")

def get_font(size):
    return pygame.font.Font("./assets/font.ttf", size)




while running:
    screen.fill("black")

    mouse_position = pygame.mouse.get_pos()

    meny_text = get_font(40).render("Bosses Buss", True, "#b68f40")
    meny_rect = meny_text.get_rect(center=(640, 100))

    lägg_till_passagerare_knapp = Button(image=None, pos=(900, 500),
                                            text_input="Lägg till passagerare", font=get_font(20), base_color="Green", hovering_color="White")
    
    skriv_ut_array = Button(image=None, pos=(900, 400),
                                            text_input="Skriv ut passagerare", font=get_font(20), base_color="Green", hovering_color="White")
    
    skriv_ut_sammanlagd_ålder = Button(image=None, pos=(900, 300),
                                            text_input="Skriv ut sammanlagd ålder", font=get_font(20), base_color="Green", hovering_color="White")        
    
    avsluta = Button(image=None, pos=(900, 150),
                                            text_input="Avsluta", font=get_font(20), base_color="Green", hovering_color="White")         

    screen.blit(meny_text, meny_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if lägg_till_passagerare_knapp.checkForInput(mouse_position):
                lägg_till_passagerare()
            if skriv_ut_array.checkForInput(mouse_position):
                skriv_ut_passagerare()
            if skriv_ut_sammanlagd_ålder.checkForInput(mouse_position):
                skriv_ut_sammanlagd_ålder()
            if avsluta.checkForInput(mouse_position):
                running = False
            

    
    pygame.display.update()

pygame.quit()
