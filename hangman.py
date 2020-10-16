import time

 #welcoming the user
name = input('What is your name ? ')
print('Hello, ' + name +' Time to play HANGMAN ! ')
print('')

#create while loop
#check if the turns are still more than zero

def game():
   
    time.sleep(1)  #wait for 1 second
    
    a = 0
    word = 'bench' #set the word
    guesses = ''   #creating variable with empty value
    
    #determine number of terms
    turns =  int(input('Enter the number of times you want to guess : '))
    print('\n')
    print('Start Guessing ....')
    time.sleep(0.5)
   
    while turns > 0 :
        
      failed = 0   # setting counter variable
      if a == 0:
          guess = input('Guess a character : ') #ask user to guess a character
          guesses += guess                      #set players guess to guesses

          for char in word:        
            if char in guesses :  # see if character in the word is in players list
                print(char)       # then print out the character
                
            else :
                print('_')
                failed += 1       #increase failed counter by one

                        
          if guess not in word :
               turns -= 1
               print('wrong')
               print('You have ' + str(turns) + ' more guesses')   # print turns left
            

          if failed == 0 :
            a = 1
            print('---- You Won !! ---\n')            

          if turns == 0 :    # if turns = 0 print 'you loose'
             print('---- You loose ----')
             
game()



        
        
