#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

def getCardValue():                    #function return a random number between 2-14.
    num = random.randint(2,14)
    return num
# #function convert the integer to a string between 2 to 9 and convert rest of card values to string as follows-

def getCardStr(cardValue):            
    if cardValue>=2 and cardValue<=9:
        return str(cardValue)
    elif cardValue== 10:   
        return "T"
    elif cardValue== 11:
        return "J"
    elif cardValue== 12:
        return "Q"
    elif cardValue== 13:
        return "K"
    elif cardValue== 14:
        return "A"
    #function will repeatedly ask the player High or Low until either a "H", "h", "L" or "l" is entered

def getHLGuess():        
    bet = ""
    while bet not in ["H","L","h","l"]:
        bet = input("High or Low (H/L)?: ")
    if bet in ["H","h"]:
        return "HIGH"           #return the string "HIGH" depending on player choice
    elif bet in ["L","l"]:
        return "LOW"             #return the string "LOW"
def getBetAmount(maximum):   #maximum is the integer represent the maximum points a player can bet.
    amount = 0 
    while amount<1 or amount>maximum:   #while loop will will repeatedly ask the player to enter amount if its not between 1 and maximum.
        amount = int(input("Input bet amount: "))
    return amount 
#depending on the betType (high or low), this function see if the player was correct

def playerGuessCorrect(card1, card2, betType):   
    if (card1>card2 and betType=="LOW") or (card1<card2 and betType=="HIGH"): # all the cases when player is correct
        return True 
    else:
        return False
print("--- Welcome to High-Low ---\nStart with 100 points. Each round a card will be drawn and shown.\nSelect whether you think the 2nd card will be Higher or Lower than the 1st card.\nThen enter the amount you want to bet.\nIf you are right, you win the amount you bet, otherwise you lose.\nTry to make it to 500 points within 10 tries.")


initial_points = 100
current_points = initial_points
gameplay = True 
current_round= 1
maximum_rounds = 10 
won_round = 0


while gameplay:                   #gameplay is valid 
    
    print("-------------------------------------")   #print current points and round 
    print(f"OVERALL POINTS: {current_points} ROUND {current_round}/{maximum_rounds}")
    
    
    first_card= getCardValue()                      # call function getCardValue() to generate random number
    first_card_value= getCardStr(first_card)        #call function getCardStr(cardValue) to convert it to string 
    print(f"First card is a [{first_card_value}]")  # print string value
    
     
    choice = getHLGuess()                           #call function  getHLGuess() for guessing next card
    bet_amount= getBetAmount(current_points)        # call function getBetAmount(maximum) with parameter current points as player can bet maximum current points
    
    second_card= getCardValue()                     # call function getCardValue() to generate random number for second card
    second_card_value= getCardStr(second_card)      # #call function getCardStr(cardValue) to convert it to string 
    print(f"Second card is a [{second_card_value}]")
    
    correct_guess = playerGuessCorrect(first_card_value,second_card_value,choice) # call function to see if players guess was correct (either True or False)
    
    if correct_guess == True:                       #if guess is correct, the bet amount is added to the overall points
            current_points = bet_amount+current_points
            won_round= won_round+1
            result= "WON"
    else:
            current_points=current_points-bet_amount #the bet amount is deducted from the overall points;
            result = "LOST"
    print(f"Card1 [{first_card_value}] Card 2 [{second_card_value}] - You bet '{choice}' for {bet_amount} - YOU {result}")  # Printout the round result
    
    
    
    
# stopping Criteria 

    if current_points>=500:                          # If the player reaches 500 or more points
        print("\n-------------------WIN----------------------")
        print(f"YOU MADE IT TO *{current_points}* POINTS IN {current_round} ROUNDS!")
        print("---------------------------------------------")
        gameplay = False                    #stop the play
        
        
           
    elif current_points==0:                          #If the player runs out of points  
        print("\n-------------------Lose----------------------")
        print(f"YOU HAVE *{current_points}* POINTS AFTER {current_round} ROUNDS")

        if won_round==1:                            #If they won only one round
            print(f"YOU COULD WIN ONLY *1* ROUND AFTER {current_round} ROUNDS!")
            
        elif won_round>1:                           #If they won more than one round,
            print(f"BUT COULD WIN *{won_round}* ROUND AFTER {current_round} ROUNDS!")
            
        else:                                       # If they could not win at least one round
            print(f"YOU COULD NOT WIN AT LEAST A ROUND AFTER {current_round} ROUNDS!")
        print("---------------------------------------------")
            
        gameplay = False                           #stop the play
        
        
        
    elif maximum_rounds==current_round:             #If they have not reached 500 or more points after ten rounds
        print("\n-------------------Lose----------------------")
        print(f"ONLY *{current_points}* POINTS IN {current_round} ROUNDS!")
        
        
        if won_round==1:                           #If they won only one round
            print(f"YOU COULD WIN ONLY *1* ROUND AFTER {current_round} ROUNDS!")
            
        elif won_round>1:                          #If they won more than one round,
            print(f"YOU COULD WIN ONLY *{won_round}* ROUND AFTER {current_round} ROUNDS!")
            
        else:                                     # If they could not win at least one round
            print(f"YOU COULD NOT WIN AT LEAST A ROUND AFTER {current_round} ROUNDS!")
            
        print("---------------------------------------------")    
        gameplay = False                          # stop the play
    
    
    else:                                        # updating current round 
        current_round += 1
                  
        


