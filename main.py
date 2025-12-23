import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    clock = pygame.time.Clock()
    dt = 0

    while True: # Main game loop
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the game loop when the window is closed
        screen.fill((0, 0, 0))  # Clear the screen with black color
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()  # Update the display
        dt = clock.tick(60) / 1000  # Limit the frame rate to 60 FPS. Store delta as milliseconds


if __name__ == "__main__":
    main()
