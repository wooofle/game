import pygame

pygame.init()

screen = pygame.display.set_mode((800, 800))

pygame.display.set_caption("TEST")

screenWidth = "empty"
screenHeight = "empty"
x = 50
y = 50

width = 40
height = 60
run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        pass
    if keys[pygame.K_RIGHT]:
        pass
    if keys[pygame.K_UP]:
        pass
    if keys[pygame.K_DOWN]:
        pass

    screen.fill((0, 0, 0))
    pygame.display.update()
    pygame.draw()


pygame.quit()
