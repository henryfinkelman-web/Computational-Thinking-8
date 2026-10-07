import random

# Pick a word at random
word_list = ["feets","ocean","poopy","jaxon","henry"]
hidden_word = random.choice(word_list)


# Guess a word
guess_word = input("ENTER A WORD: ")
output = ""

# First letter (in python, counting starts at 0 not 1)
if guess_word[0] == hidden_word[0]:
    output += "🟩🟩🟩🟩🟩"
elif guess_word[0] in hidden_word:
    output += "🟨🟨🟨🟨🟨"
else:
    output += "⬛⬛⬛⬛⬛"




# Result
print(f"Result: {output}")
if output == "🟩🟩🟩🟩🟩":
    print("You win")

# Guess a word
guess_word = input("ENTER A WORD: ")
output = ""

# First letter (in python, counting starts at 0 not 1)
if guess_word[0] == hidden_word[0]:
    output += "🟩🟩🟩🟩🟩"
elif guess_word[0] in hidden_word:
    output += "🟨🟨🟨🟨🟨"
else:
    output += "⬛⬛⬛⬛⬛"




# Result
print(f"Result: {output}")
if output == "🟩🟩🟩🟩🟩":
    print("You win")
print(f"Result: {output}")
if output == "🟩🟩🟩🟩🟩":
    print("You win")

# Guess a word
guess_word = input("ENTER A WORD: ")
output = ""

# First letter (in python, counting starts at 0 not 1)
if guess_word[0] == hidden_word[0]:
    output += "🟩🟩🟩🟩🟩"
elif guess_word[0] in hidden_word:
    output += "🟨🟨🟨🟨🟨"
else:
    output += "⬛⬛⬛⬛⬛"




# Result
print(f"Result: {output}")
if output == "🟩🟩🟩🟩🟩":
    print("You win")
