import random
given_word=['war','makkhi','dhoom','ready','wanted','bhaagi','vivah','toilet']
live=6
chosen_word=random.choice(given_word)
#print(chosen_word)
display=[]
for i in chosen_word:
    display+='_'
print(display)
game=True
while game:
    guess_word=input("Guess a word").lower(


    )
    for position in range(len(chosen_word)):
        letter=guess_word
        if letter==chosen_word[position]:
            display[position]=guess_word
    print(display)

    if guess_word not in chosen_word:
        live-=1
        if live==0:
            game=False
            print("Soory u lose the game")
    if '_' not in display:
        game=False
        print("Hurray u won the gamee")



