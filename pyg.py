import pygame

def draw_guess(guess):
    pass

def init_board(word):
    for i in range(len(word)):
        pygame.draw.rect(WIN, GRAY, (BOX_SIZE * i, 0, BOX_SIZE, BOX_SIZE))
        pygame.display.update()

def main():
    global WIDTH
    WIDTH = 1000
    global HEIGHT
    HEIGHT = 500
    pygame.init()
    global WIN
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Wordle Clone")
    # game init

    global FPS
    FPS = 60
    global WHITE
    WHITE = (255, 255, 255)
    global GRAY
    GRAY = (200, 200, 200)
    global GREEN
    GREEN = (0,128,0)
    # colors

    global BOX_SIZE
    BOX_SIZE = 100
    # vars

    clock = pygame.time.Clock()
    run = True

    WIN.fill(WHITE)
    pygame.display.update()

    word = "START"

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        init_board(word)

        # font = pygame.font.SysFont("Time New Roman, Arial", 30)
        # text = font.render("Hello World!", True, GREEN)
        # WIN.blit(text, (WIDTH/2 - text.get_rect().width/2, HEIGHT/2 - 100))
        # pygame.display.update()
        
    pygame.quit()


if __name__ == "__main__":
    main()