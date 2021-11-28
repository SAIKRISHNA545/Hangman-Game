# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
print("Hello world")

word_list = ["ardvark", "baboon", "camel"]
l=[]
lifes=6
chose_word=random.choice(word_list)
print(chose_word)
for i in range(0,len(chose_word)):
    l.append("_")
print(l)
while "_" in l:
    guess=input("enter a letter to guess:")
    for j in range(0,len(chose_word)):
        if guess==chose_word[j]:
            l[j]=guess
        if l[j]==guess or guess not in word_list:
            lifes-=1
    print(stages[lifes])
    print(l)
if lifes==0:
    print("you lose")
else:
    print("you win")
