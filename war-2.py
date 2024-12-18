# Import necessary modules
import random
import time

# Define the ranks and suits
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
suits = ("hearts", "diamonds", "clubs", "spades")

deck = []
# Create a deck of cards
for rank in ranks:
    for suit in suits:
        deck.append((rank, suit))

# Shuffle the deck 
random.shuffle(deck)



#function to compare the 2 cards that are currently put down
def card_comparison(p1_card, p2_card):
    """This is the logic that compares two cards to find the stronger card
		Return 1 if player 1's card is strong, 2 for player 2
		if the cards are equal, return 0.

		Hint, using the index function will make this very simple (one liner)"""

    # if p1's card is better, return 1, if p2 better, return 2. If tie return 0 (war)
    if ranks.index(p1_card[0]) > ranks.index(p2_card[0]):
        return 1
    elif ranks.index(p1_card[0]) < ranks.index(p2_card[0]):
        return 2
    else:
        return 0




#every round
def play_round(p1_hand, p2_hand, p1_pile, p2_pile):

    """Play a single round of the game.
		That is, each player flips a card, and the winner is determined using the card_comparison function
		if both players flip the same value card, call the war function
	"""


    # a count goes up by 1 every round to compare hand indexes. 
    # however if count > length of a hand, error
    # therefore check if count > length, then count = 0
    # if a hand is empty it means someone has won
    
    if p1_hand == []:
        if p1_pile == []:
            return "P2 Win"
        else:

            p1_pile.shuffle()

            p1_hand = p1_pile

            p1_pile = []
            
            changeCount1ToZero = True
            
            
    if p2_hand == []:
        if p2_pile == []:
            return "P1 Win"
        else:
            
            p2_pile.shuffle()
    
            p2_hand = p2_pile

            p2_pile = []
            
            changeCount2ToZero = True

    # for bugtesting
            
    #print("Count 1:", count1, "Count 2:", count2)
    #print("Len 1:", len(p1_hand), "Len 2:", len(p2_hand))

    
    
    currentCard1 = p1_hand.pop(0)
    currentCard2 = p2_hand.pop(0)

	
    print(currentCard1, "vs.", currentCard2)

    time.sleep(.1)

    print(" ")


    # whoWonRound will either be 1, 2, or 0	
    whoWonRound = card_comparison(currentCard1, currentCard2)


    
    if whoWonRound == 1:
        print("Player 1 wins the round.")

        
        p1_pile.append(currentCard1)
        p1_pile.append(currentCard2)  
        
    elif whoWonRound == 2:
        print("Player 2 wins the round.")
        
        p2_pile.append(currentCard1)
        p2_pile.append(currentCard2) 
    
    else:
        print("War!\n")

        #pot is for the war scenario
        pot = []

        p1_pile, p2_pile = war(p1_hand, p2_hand, currentCard1, currentCard2, pot)

    time.sleep(.1)


            

    input("Enter to continue.")
    print(" ")
    


def war(p1_hand, p2_hand, card1, card2, pot):
    """Handle the 'war' scenario when cards are equal.
		recall the rules of war, both players put 3 cards face down, 
		then both players flip face up a 4th card. The player with the stronger
		card takes all the cards.		
	"""
    
    input("Each player puts down 3 cards.")
    print(" ")

    # pot is all the cards that will be given to the player that wins the "war"

    # only append from a hand if not empty, otherwise error
    
    if len(p1_hand) >= 1:
        pot.append(p1_hand.pop(0))

    if len(p2_hand) >= 1:
        pot.append(p2_hand.pop(0))


    # range 3 because each put down 3 cards
    for i in range(3):

        # again we cannot append from an empty list


        if p1_hand == []:

            
            
            break
        else:
            
            pot.append(p1_hand.pop(0))

        if p2_hand == []:
            
            break
        else:
            
            pot.append(p2_hand.pop(0))


    if 

    card1 = p1_hand.pop(0)
    card2 = p2_hand.pop(0)

    pot.append(card1)
    pot.append(card2)

    # warWinner has same function as whoWonRound

    warWinner = card_comparison(card1, card2)

    print(card1, "vs.", card2, "\n")

    time.sleep(.5)


    if warWinner == 1:
        print("Player 1 wins the war!")

        for card in pot:
            p1_hand.append(card)
        
    elif warWinner == 2:
        print("Player 2 wins the war!")

        for card in pot:
            p2_hand.append(card)
    
    else:
        print("War again!\n")

        war(p1_hand, p2_hand, card1, card2, pot)

    return p1_hand, p2_hand
    


def play_game():

    
    # Split the deck into two hands

    hand1 = deck[:len(deck)//2]
    hand2 = deck[len(deck)//2:]

    # win piles for each player

    pile1 = []
    pile2 = []

    winner = "Idk"

    input("To begin the game, press enter. ")
    print(" ")

    # while there is no winner (winner is not returned)
    while winner != "P2 Win" and winner != "P1 Win":
        
                
        winner = play_round(hand1, hand2, pile1, pile2)
        
    
    print("The winner is " + winner[:2]+"!!")

# Call the main function to start the game
play_game()
