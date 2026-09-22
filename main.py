import random
guesses_list = ["russia","elephant","apple","sleep","jazz"]

word = random.choice(guesses_list)

wrong_guesses = 0

hidden_word = ["*"] * len(word)
while wrong_guesses < 6:
    user_input = input(f"Guess word!....")

    if len(user_input) > 1:
        wrong_guesses += 1
        print(f"Error: PLease Enter 1 latter only")
        print(f"Remaining guesses: {6 - wrong_guesses}")
        print("".join(hidden_word))
        
        if wrong_guesses >= 6:
            break
            
        continue
        
    found = False
    if user_input in word:
        for i in range(len(word)):
            if word[i] == user_input:
                hidden_word[i] = user_input
                found = True
    if found == False:
        wrong_guesses += 1
        print(f"Remaining guesses: {6 - wrong_guesses}")
    print("".join(hidden_word))
    if "*" not in hidden_word:
        print("You win")
        break
else:
    print(f"You lose! The word was: {word}")
