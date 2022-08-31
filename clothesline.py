
def main():
    secret_word="apple"
    message="The secret word is:"
    # print(message,secret_word)
    print("Welcome to Clothesline!")
    secret_word_length=len(secret_word)
    # print(secret_word_length,secret_word)
    guess=  "-"  *len(secret_word)
    print("word:    "   +str(guess))
    letter=input(">")
    letters_guessed=[]
    letters_guessed.append(letter)
    print("Guesses:" + str(letters_guessed))
    
    
    incorrect_count= 8
    while incorrect_count > 0:
        clear_screen()
        print("Guess a letter... if you dare?")
        print("word:    "    +str(guess))
        print("You have" + str(incorrect_count))
        letter=input(">")
        letters_guessed=[]
        letters_guessed.append(letter)
        print("Guesses:" + str(letters_guessed))
        print(incorrect_count, guess, letters_guessed)
        print("The word was:" + str(secret_word))

    
        print()
        is_correct = is_letter_in_word(letter,secret_word)
        if is_correct == True:
            print("Good Guess")
        else:
            incorrect_count = incorrect_count -1
            print("You're terrible at guessing")
        print_clothesline(incorrect_count)
        
        
              
#Functions
   
   
def clear_screen():
    print("\033[H\033[J", end="")

def is_letter_in_word(letter,secret_word):
    if letter in secret_word:
        return True
    else:
        return False
      

    
def print_clothesline(incorrect_count):
    print("You have:" + str(incorrect_count) + "left")
    

def update_guess(old_guess, letter,  word):
    new_guess = ""
    for index in range(len(old_guess)):
        if word[index] == letter:
            new_guess = new_guess + letter
        else:
            new_guess = new_guess + old_guess[index]

    return new_guess




main()



r"""
=====!=====!=======!=====!=======!=====!=======!=====!=====
    /'''V'''\     /'''V'''\     /'''V'''\     /'''V'''\
   /         \   /         \   /         \   /         \
  '-"|     |"-' '-"|     |"-' '-"|     |"-' '-"|     |"-'
     |     |       |     |       |     |       |     |
     |     |       |     |       |     |       |     |
     ```````       ```````       ```````       ```````


"""

r"""
=====!=====!=======!=====!=======!=====!=======!===========
    /'''V'''\     /'''V'''\     /'''V'''\     /'\
   /         \   /         \   /         \   /   .\
  '-"|     |"-' '-"|     |"-' '-"|     |"-'  '|  ='
     |     |       |     |       |     |      |   |
     |     |       |     |       |     |      |   |
     ```````       ```````       ```````      `-._|


"""

r"""
=====!=====!=======!=====!=======!=====!===================
    /'''V'''\     /'''V'''\     /'''V'''\
   /         \   /         \   /         \
  '-"|     |"-' '-"|     |"-' '-"|     |"-'
     |     |       |     |       |     |
     |     |       |     |       |     |
     ```````       ```````       ```````
                                            _.~.,_.._
                                             ```````

"""

r"""
=====!=====!=======!=====!=======!=========================
    /'''V'''\     /'''V'''\     /'\
   /         \   /         \   /   .\
  '-"|     |"-' '-"|     |"-'  '|  ='
     |     |       |     |      |   |
     |     |       |     |      |   |
     ```````       ```````      `-._|
                                            _.~.,_.._
                                             ```````
"""

r"""
=====!=====!=======!=====!=================================
    /'''V'''\     /'''V'''\
   /         \   /         \
  '-"|     |"-' '-"|     |"-'
     |     |       |     |
     |     |       |     |
     ```````       ```````
                              _.~.,_.._     _.~.,_.._
                               ```````       ```````
"""

r"""
=====!=====!=======!=======================================
    /'''V'''\     /'\
   /         \   /   .\
  '-"|     |"-'  '|  ='
     |     |      |   |
     |     |      |   |
     ```````      `-._|
                              _.~.,_.._     _.~.,_.._
                               ```````       ```````
"""

r"""
=====!=====!===============================================
    /'''V'''\
   /         \
  '-"|     |"-'
     |     |
     |     |
     ```````
                _.~.,_.._     _.~.,_.._     _.~.,_.._
                 ```````       ```````       ```````
"""

r"""
=====!=====================================================
    /'\
   /   .\
   '|  ='
    |   |
    |   |
    `-._|
                _.~.,_.._     _.~.,_.._     _.~.,_.._
                 ```````       ```````       ```````
"""

r"""
===========================================================






  _.~.,_.._     _.~.,_.._     _.~.,_.._     _.~.,_.._
   ```````       ```````       ```````       ```````
"""