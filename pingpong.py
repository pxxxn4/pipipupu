import pygame, sys

pygame.init()
clock = pygame.time.Clock()
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ping Pong")
FPS = 60

white = (255, 255, 255)
black = (0, 0, 0)

ball = pygame.Rect(width/2 - 15, height/2 - 15, 30, 30)
player = pygame.Rect(width - 20, height/2 - 70,  10, 140)
opp = pygame.Rect(10, height/2 - 70,  10, 140)

bg_color = white

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()  

    screen.fill(bg_color)
    pygame.draw.rect(screen, black, player)
    pygame.draw.rect(screen, black, opp)
    pygame.draw.ellipse(screen, black, ball)
    pygame.display.flip()
    clock.tick(FPS)