import pygame
import time
pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('berdley.mp3')
pygame.mixer.music.play(-1)
sound = pygame.mixer.Sound('splat.wav')

kris = pygame.image.load('kris.png')
kris = pygame.transform.scale(kris, (50, 100))
kris_rect = pygame.Rect(100, 350, 50, 100)
banana = pygame.image.load('banana.jpg')
banana = pygame.transform.scale(banana, (30, 30))
banana_rect = pygame.Rect(500, 350, 30, 30)
queen = pygame.image.load('queen.png')
queen = pygame.transform.scale(queen, (72, 136))
potassium = pygame.image.load('potassium.png')
potassium = pygame.transform.scale(potassium, (300, 85))
getbanana = pygame.image.load('getbanana.png')
getbanana = pygame.transform.scale(getbanana, (300, 85))
win = pygame.image.load('win.png')
win = pygame.transform.scale(win, (300, 85))
home = pygame.image.load('home.png')
home = pygame.transform.scale(home, (300, 85))
more = pygame.image.load('more.png')
more = pygame.transform.scale(more, (300, 85))
run = True
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Deltarune Chapter 20')
banana_claimed = False
bg = pygame.image.load('bg.png')
bg = pygame.transform.scale(bg, (800, 600))
screen.blit(bg, (0, 0))
show1 = True
show2 = False
show3 = False
show4 = False
show5 = False

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                if show1:
                    show1 = False
                elif show2:
                    show2 = False
                    show3 = True
                elif show3:
                    show3 = False
                    show4 = True
                elif show4:
                    show4 = False
                    show5 = True
                elif show5:
                    show5 = False
                    time.sleep(1.5)
                    run = False

    keys = pygame.key.get_pressed()
    if not show1 and not show2 and not show3 and not show4 and not show5:
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            kris_rect.x += 5
            if kris_rect.x > 750:
                kris_rect.x = 750
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            kris_rect.x -= 5
            if kris_rect.x < 0:
                kris_rect.x = 0

    if not banana_claimed and kris_rect.colliderect(banana_rect):
        banana_claimed = True
        show2 = True
        sound.play()

    screen.blit(bg, (0, 0))
    screen.blit(kris, (kris_rect.x, kris_rect.y))
    if not banana_claimed:
        screen.blit(banana, (banana_rect.x, banana_rect.y))
    screen.blit(queen, (700, 350))
    if show1:
        screen.blit(getbanana, (250, 510))
    elif show2:
        screen.blit(potassium, (250, 510))
    elif show3:
        screen.blit(win, (250, 510))
    elif show4:
        screen.blit(home, (250, 510))
    elif show5:
        screen.blit(more, (250, 510))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()