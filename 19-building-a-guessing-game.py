secret_word = "giffgaff"
guess = ""

attempts = 0
available_attempts = 5

while guess != secret_word:
    attempts += 1
    guess = input("Guess the word: ")

    if attempts >= available_attempts:
        print(f"You're out of guesses. The word was {secret_word}")
        break
# `else` on a while loop triggers when the condition becomes false
# It does NOT trigger on a `break`
else:
    print(f"Congratulations! The word was {secret_word}.")
