letters = set()
def letters_guessed(guess, word):
    length = len(letters)
    letters.add(guess)
    if length == len(letters):
        print("Letter has already been guessed.")
    elif guess in word:
        print("You've guessed a correct letter!")
    else:
        print("Sorry, that letter isn't in the word.")

#Test cases
letters_guessed("s", "share")
letters_guessed("t", "share")
letters_guessed("t", "share")