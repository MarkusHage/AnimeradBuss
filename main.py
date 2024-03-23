import pygame, sys
from button import Button
import random

size = width, height = (1280, 720)


pygame.init()
running = True
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bosses Buss")
clock = pygame.time.Clock()

font = pygame.font.SysFont('comicsans', 5)
bg = pygame.image.load("./assets/121an.jpg")
bg = pygame.transform.scale(bg, size)
buss_bild = pygame.image.load("./assets/buss.png")
buss_bild = pygame.transform.scale(buss_bild, (600,400))



class Buss():
    def __init__(self):
        self.items=[]

    def lägg_till_ny_passagerare(self):
        if len(buss.items) < 25:
            ålder = random.randint(5,99)
            self.items.append(ålder)
            print(f"En passagerare som är {buss.items[-1]} år gammal hoppade på bussen. Totalt {len(buss.items)} passagerare på bussen.")
        else:
            print("Tyvärr grabbar, inga slots lediga. Bussen är full.") 

    def skriv_ut_lista(self):
        if len(buss.items) > 0:
            print(buss.items)
        else:
            print("Bussen är tom!")

    def skriv_ut_sammanlagd_ålder(self):
        if len(buss.items) > 0:
            print(sum(buss.items))
        else:
            print("Bussen är tom!")


    

class Button(pygame.sprite.Sprite):
    def __init__(self, color, color_hover, rect, callback, outline=None, text=''):
        super().__init__()
        self.text = text
        temp_rect = pygame.Rect(0, 0, *rect.size)

        self.org = self._create_image(color, outline, text, temp_rect)
        self.hov = self._create_image(color_hover, outline, text, temp_rect)

        self.image = self.org
        self.rect = rect
        self.callback = callback

    def _create_image(self, color, outline, text, rect):
        img = pygame.Surface(rect.size)
        if outline:
            img.fill(outline)
            img.fill(color, rect.inflate(-4, -4))
        else:
            img.fill(color)

        if text != '':
            text_surf = get_font(10).render(text, 1, pygame.Color('black'))
            text_rect = text_surf.get_rect(center=rect.center)
            img.blit(text_surf, text_rect) 
        return img 

    def update(self, events):
        pos = pygame.mouse.get_pos()
        hit = self.rect.collidepoint(pos)
        self.image = self.hov if hit else self.org
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and hit:
                self.callback(self)

   
  
buss = Buss()



def get_font(size):
    return pygame.font.Font("./assets/font.ttf", size)





        
""" def skriv_ut_lista():
    if len(buss.items) > 0:
        print(buss.items)
    else:
        print("Bussen är tom!")

def skriv_ut_sammanlagd_ålder():
    if len(buss.items) > 0:
        print(sum(buss.items))
    else:
        print("Bussen är tom!") """

def avsluta():
    print("Avslutar programmet...")
    pygame.quit()
    quit()

        

sprites = pygame.sprite.Group()
sprites.add(Button(pygame.Color('lightblue'),
                    pygame.Color('red'),
                    pygame.Rect(800, 50, 300, 100),
                    lambda b: buss.lägg_till_ny_passagerare(),
                    pygame.Color('black'),
                    'Lägg till'))

sprites.add(Button(pygame.Color('lightblue'),
                    pygame.Color('red'),
                    pygame.Rect(800, 200, 300, 100),
                    lambda b: buss.skriv_ut_lista(),
                    pygame.Color('black'),
                    'Skriv ut lista',))

sprites.add(Button(pygame.Color('lightblue'),
                    pygame.Color('red'),
                    pygame.Rect(800, 350, 300, 100),
                    lambda b: buss.skriv_ut_sammanlagd_ålder(),
                    pygame.Color('black'),
                    'Skriv ut sammanlagd ålder'))

sprites.add(Button(pygame.Color('lightblue'),
                   pygame.Color('red'),
                   pygame.Rect(800, 500, 300, 100),
                   lambda b: avsluta(),
                   pygame.Color('black'),
                   'Avsluta'))



while running:

    events = pygame.event.get()
    for event in events:    
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    screen.blit(bg, (0, 0))
    screen.blit(buss_bild, (50, 300))  
    sprites.update(events)
    #screen.fill(pygame.Color('white'))
    sprites.draw(screen)
    pygame.display.update()
    clock.tick(60)
    
    pygame.display.update()

pygame.quit()
