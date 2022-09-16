import pygame

def check_letter(word: str, letter: str, index: int) -> list[bool]: # checks if the letter is in the word or in position
    in_word, in_pos = False, False
    if letter in word:
        if word[index] == letter:
            in_pos = True
        else:
            in_word = True

    return [in_word, in_pos]
# in_word will be true if the letter is in the word (not in position) and in_pos will be false
# in_pos will be true if the letter is in the correct position but in_word will be false
# in_word and in_pos will be false if the letter is not in the word at all
# guaranteed only 1 to be True if the letter is in word

def check_guess(word: str, guess: str) -> dict[str, list[bool]]: # checks the guess
    res = {}

    for ind, i in enumerate(guess):
        res[i] = check_letter(word, i, ind)

    return res
# ouputs a dict of the letters with a bool array of in word and in position
# i.e. {"s": [True, False]} means the letter "s" is in the word but not in position

# def valid_guess(word, guess) -> bool:
#     if guess not in list_of_words or not len(word) == len(guess):
#         return False
#     return True


def start(word: str, tries: int) -> None: # starts the game
    curr_tries = 0
    won = False
    while curr_tries < tries:
        print("Guess: ")
        guess = str(input())

        if guess == word:
            won = True
            break

        if not len(guess) == len(word):
            print(f"Must be {len(word)} letters")
            continue
        
        # if not valid_guess(guess):
        #     print("This word is not in the word list")
        #     continue
    
        outcome = check_guess(word, guess)

        seen = set()
        for ind, i in enumerate(outcome):
            in_word, in_pos = outcome[i]
            if in_word and not i in seen:
                print(f"{i} is in the word")
                seen.add(i)
            elif in_pos:
                print(f"The {i} at position {ind + 1} is correctly placed")
                seen.add(i)
        
        curr_tries += 1

    if won:
        print("You won!")
    else:
        print(f"You lost! The word was {word}.")

def get_word() -> str:
    pass

def pygame_start():
    pygame.init()

    # Set up the drawing window
    screen = pygame.display.set_mode([500, 500])

    # run until the user asks to quit
    running = True
    while running:

        # did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the background with white
        screen.fill((255, 255, 255))
        
    pygame.quit()

def main():
    # start(get_word(), 6)
    start("hands", 6)
    # while True:
    #     print("Play again? Y/N")
    #     play_again = str(input)
    #     if play_again == "Y" or play_again == "y":
    #         start("stare", 6)
    #     elif play_again == "N" or play_again == "n":
    #         break
    # print(check_letter("stare", "s"))

    BOX_SIZE = 64


if __name__ == "__main__":
    main()
