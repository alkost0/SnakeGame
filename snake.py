import pygame

FPS = 60

pygame.init

screen = pygame.display.set_mode([640, 480])
clock = pygame.time.Clock()

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            print('qiut event')
            is_running = False
    pygame.display.update
    clock.tick(FPS)

pygame.quit()


