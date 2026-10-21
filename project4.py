import random

words = [
    "apple", "grape", "beach", "train", "smile",
    "house", "plant", "chair", "bread", "water",
    "stone", "cloud", "light", "music", "story",
    "green", "black", "white", "peace", "dream",
    "river", "ocean", "tiger", "happy", "school"
]

secret_word = random.choice(words)
won = False

print("guess the word")
print("if one of the letters is upercase that means its green")
print("if one of the letter is lowercase then thatmeans its yellow")
print("if you see the little star thing that means its not good")

for word in words:
    if won == False:
        guess = input("Your guess: ")

        if guess == secret_word:
            print("You win!")
            won = True
        elif guess[4:5] == "":
            print("Your guess needs 5 letters.")
        else:
            hint = ""

            for place in (0, 1, 2, 3, 4):
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

