import pygame

def draw_stickman(screen):
    black = (0, 0, 0)
    pygame.draw.circle(screen, black, (200,200), 30, 5)
    pygame.draw.line(screen, black, (200, 230), (200, 350), 5)
    pygame.draw.line(screen, black, (200, 260), (140, 310), 5)
    pygame.draw.line(screen, black, (200, 260), (260, 310), 5)
    pygame.draw.line(screen, black, (200, 350), (150, 430), 5)
    pygame.draw.line(screen, black, (200, 350), (250, 430), 5)

pygame.init()
bg = pygame.display.set_mode((600,600))

bg_img = pygame.image.load("hangman/R.jpeg")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    bg.blit(bg_img,(0,0))
    draw_stickman(bg_img)
    pygame.display.flip()


pygame.quit()