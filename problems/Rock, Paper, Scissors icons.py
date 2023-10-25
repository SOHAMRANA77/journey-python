import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants for colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize screen and font
screen_width, screen_height = 600, 400
screen = pygame.display.set_mode((screen_width, screen_height))
font = pygame.font.Font(None, 36)

# Load icons
rock_icon = pygame.image.load('rock_icon.png')
paper_icon = pygame.image.load('paper_icon.png')
scissors_icon = pygame.image.load('scissors_icon.png')

# Function to display text on the screen
def display_text(text, x, y):
    text_surface = font.render(text, True, BLACK)
    screen.blit(text_surface, (x, y))

# Function to handle player's choice
def player_choice(choice):
    print(f"You chose: {choice}")

# Game loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill(WHITE)

        # Display icons for rock, paper, and scissors
        screen.blit(rock_icon, (65, 105))
        screen.blit(paper_icon, (235, 105))
        screen.blit(scissors_icon, (405, 105))

        pygame.display.flip()

if __name__ == "__main__":
    main()
