#Step 5

import random
import hangman_art
import hangman_words
import replit

print(hangman_art.logo)
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"
# Code block for guessig a letter
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    replit.clear()
    if guess in display:
      print(f"You already guessed {guess}")
    

    
    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter

    
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life, current lifes: {lives - 1} ")
        
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(chosen_word)

    
    print(f"{' '.join(display)}")

    
    if "_" not in display:
        end_of_game = True
        print("You win.")

    
    from hangman_art import stages
    print(stages[lives])