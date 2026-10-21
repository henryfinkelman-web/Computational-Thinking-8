import random

words = [
    "apple", "grape", "beach", "train", "smile",
    "house", "plant", "chair", "bread", "water",
    "stone", "cloud", "light", "music", "story",
    "green", "black", "white", "peace", "dream",
    "river", "ocean", "tiger", "happy", "school",
    "table", "phone", "brush", "spoon", "shirt",
    "clock", "horse", "piano", "lemon", "candy"
]

secret_word = random.choice(words)
won = False

print("Guess the 5-letter word!")
print("Uppercase means the letter is in the right spot.")
print("Lowercase means it is in the word but in the wrong spot.")
print("* means the letter is not in the word.")

# This loop lets you guess 6 times.
for turn in range(6):
    if won == False:
        guess = input("Your guess: ")

        if guess == secret_word:
            print("You win!")
            won = True
        else:
            hint = ""

            for place in range(5):
                letter = guess[place]

                if letter == secret_word[place]:
                    hint = hint + letter.upper()
                elif letter in secret_word:
                    hint = hint + letter
                else:
                    hint = hint + "*"

            print("Hint:", hint)

if won == False:
    print("The word was", secret_word)