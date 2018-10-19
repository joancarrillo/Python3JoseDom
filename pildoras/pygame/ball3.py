import sys, pygame
pygame.init()

size = width, height = 800, 600
screen = pygame.display.set_mode(size)

run=True
while run:
    pygame.time.delay(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False
pygame.quit()