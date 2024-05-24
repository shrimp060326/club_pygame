import pygame

pygame.init()

screen_width = 1280
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

clock = pygame.time.Clock()

pygame.display.set_caption("Game Title")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0,0,0), [100, 100, 100, 100])                 #x, y,가로, 세로

    pygame.display.update()

pygame.quit()
