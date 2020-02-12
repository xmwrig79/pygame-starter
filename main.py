
import pygame
pygame.init()

win = pygame.display.set_mode((800, 600))
img = pygame.image.load('assets/forest-assets/door.png').convert()

font = pygame.font.SysFont("arial", 72)
# Create the text object
text = font.render("Hello, world", True, (255, 255, 255))

# Load the spritesheet
spritesheet = pygame.image.load('assets/gfx/objects.png').convert()

# Create the first image
smol_img = pygame.Surface([16, 16]).convert()
smol_img.blit(spritesheet, (0, 0), (0, 0, 16, 16))

# Create the second image
smolr_img = pygame.Surface([16, 16]).convert()
smolr_img.blit(spritesheet, (0, 0), (16, 0, 16, 16))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0, 0, 0))
    win.blit(img, (400, 300))
    win.blit(smol_img, (100, 100))
    win.blit(smolr_img, (150, 100))


    pygame.display.update()

pygame.quit()