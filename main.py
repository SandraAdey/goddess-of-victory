import pygame

from fighter import Fighter


pygame.init()

#create game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Brawler")

#loading back ground image
bg_image = pygame.image.load("image/nikke.png").convert_alpha()

def draw_bg():
  scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
  screen.blit(scaled_bg, (0, 0))

#creating 2 fighters
fighter_1 = Fighter(200, 310)
fighter_2 = Fighter(700, 310)

#game loop
run = True
while run:
  
  #draw background
  draw_bg()

  #draw fighters
  fighter_1.draw(screen)
  fighter_2.draw(screen)


  #event handler
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False


  pygame.display.update()     

pygame.quit()