# This allows us to use code from the open-source
# pygame library throughout this file
import pygame
from constants import *
from logger import log_state
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    dt = 0
    clock = pygame.time.Clock()
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(x, y)
    
    while True:
        dt = clock.tick(60) / 1000
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)         # formerly player.update(dt)
        
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)         # formerly player.draw(screen)
            
        pygame.display.flip()   
        
if __name__ == "__main__":
    main()


