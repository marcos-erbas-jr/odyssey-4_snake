import pygame

pygame.init()
screen = pygame.display.set_mode((400,300))
pygame.display.set_caption('Snake')
#icon = pygame.image.load('snakeicon.png')
#pygame.display.set_icon(icon)
clock = pygame.time.Clock()
running = True
font = pygame.font.SysFont("monospace", 15, bold=pygame.font.Font.bold)


increment = 0

playerx = 200
playery = 150
body = 3
snake_body = [[playerx, playery], [playerx+10, playery], [playerx+20, playery]]

score = 0

def background():
    screen.fill((0, 0, 0))
    pygame.draw.lines(screen, (255, 255, 255), True,
                      [(10, 10), (390, 10), (10, 10), (10, 290), (390, 290),
                       (390, 10)], 5)
    pygame.draw.lines(screen, (255, 255, 255), True,
                      [(10, 40), (390, 40)], 5)
    scoretext = font.render("SCORE: {0}".format(score), 0, (255,255,255))
    screen.blit(scoretext, (20, 17))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    background()

    #snake
    for b in range(0, body):

        pygame.draw.rect(screen, (255, 0, 0), (snake_body[b][0]+increment,
                                               snake_body[
            b][1], 10, 10))

    increment += 1

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()