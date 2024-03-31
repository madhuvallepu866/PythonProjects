import random
import Hangman_stages
import words_file
#word_list=["apple","beautiful","potato"]
lives=6
chosen_word=random.choice(words_file.words)
print(chosen_word)
display=[]
for i in range(len(chosen_word)):
    display += '_'
print(display)
game_over=False
while not game_over:
    guess_letter=input("guess a letter: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess_letter:
            display[position] = guess_letter
    print(display)
    if guess_letter not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You Lose!!!")
    if '_' not in display:
        game_over=True
        print("You Win!!!")
    print(Hangman_stages.stages[lives])
