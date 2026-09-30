import pygame

pygame.init()
bg = pygame.display.set_mode((600,600))

bg_img = pygame.image.load("hangman/R.jpeg")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    bg.blit(bg_img,(0,0))
    pygame.display.flip()

pygame.quit()