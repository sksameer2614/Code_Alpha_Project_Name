import random
def select_word():
    words = [
        ("python", "a programming language"),
        ("development", "the process of creating software"),
        ("hangman", "a classic word-guessing game"),
        ("challenge", "a task or situation that tests someone's abilities"),
        ("programming", "the act of writing computer programs")
    ]
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word, hint = select_word()
    guessed_letters = set()
    max_incorrect_guesses = int(len(word) * 0.8)
    incorrect_guesses = 0

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")
    print(f"The word is related to: {hint}.")
    print(f"You have {max_incorrect_guesses} chances to guess the word.\n")
    print(display_word(word, guessed_letters))
    
    while incorrect_guesses < max_incorrect_guesses:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
        else:
            incorrect_guesses += 1
            print(f"Incorrect guess. You have {max_incorrect_guesses - incorrect_guesses} incorrect guesses left.")

        current_state = display_word(word, guessed_letters)
        print(current_state)

        if "_" not in current_state:
            print(f"Congratulations! You guessed the word: {word}")
            break
    else:
        print(f"Sorry, you've run out of guesses. The word was: {word}")

if __name__ == "__main__":
    hangman()
