## Riddle Game

import random

def riddle():
    play = True
    
    while play:
    
        answers = ('y', 'n')
        alreadyAnswered = False
        winnerNumber = random.randint(1,100)
    #    print(winnerNumber)
        isChoiceInvalid = True
    
        ## Input has to be number
            
        while isChoiceInvalid:
            
           isChoiceInvalid = False
           choice = float(input('Please insert a whole number between 1 and 100'))

           #Input has to be between 1 and 100 
           if choice < 0 or choice > 100:
               isChoiceInvalid = True
           else:
                if choice == winnerNumber :
                    
                    isChoiceInvalid = False
                    print('WOOP WOOP ! You win !')
                else :
                    # Try again until we win
                    isChoiceInvalid = True
                    
                    if winnerNumber < choice :
                        print('It is lower than that !')
                    else :
                        print('It is higher than that !')
                
        ## Retry Logic
        answer = input('Do you want to try again (y/n)? ')
    
        ## Only y or n
        while (answer not in answers ):
            print("Please answer only by 'y' or 'n'")
            answer = input('Do you want to try again (y/n)? ')
    
        while (alreadyAnswered == False):
            
            alreadyAnswered = True
    
            if answer == 'y':
                endChat = 'Here we go again !'
                play = True
            
            else :
                endChat = 'See you next time !'
                play = False
    
            print(endChat)

riddle()