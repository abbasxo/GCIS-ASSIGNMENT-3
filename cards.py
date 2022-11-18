import random as rand
def make_card(rank, suit):
    names = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"] # A list of all the names of the cards available
    shn = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]# A list for numbering of cards, and letters for Queen, King, Jack.
    list = ['S', 'H', 'C', 'D']# this is a list made that includes the first letters of the names of cards, ex: S = Spades, so on.
    suits = ["of Spades", "of Hearts", "of Clubz", "of Diamonds"] # Here we creat a list that lists the names of suits of all the cards
 
    no = rank
    num = names[no]
    nsh = shn[no]

    if suit == 0:
        name = num + " " + suits[0]
        short = nsh + list[suit]
        clr = "noir"
    elif suit == 1:
        name = num + " " + suits[1]
        short = nsh + list[suit]
        clr = "rouge"
    elif suit == 2:
        name = num + " " + suits[2]
        short = nsh + list[suit]
        clr = "noir"
    elif suit == 3:
        name = num + " " + suits[3]
        short = nsh + list[suit]
        clr = "rouge"
    if clr == "rouge":
        finalshort =  "\033[31m" + short + "\033[37m"
    elif clr == "noir":
        finalshort = "\033[34m" + short + "\033[37m"
        #adding the colors 
    finaltup = (rank + 1, list[suit], name, finalshort)
    #Here we create a tuple that contains all the 4 required informations.
    return finaltup


def create_deck(deck = []):
    # A function in which we create a deck using a for loop, and append fucntion to add the card
    for i in range(4):
        for j in range(13):
            deck.append(make_card(j, i))
    
    return(deck) 
def shuffle(deck = []):
    # A function made in order to shuffle the cards, by firstly making the deck then using for loop for shuffling 
    deck = create_deck(deck)
    for i in range(0, len(deck) - 1):
        j = rand.randint(1, len(deck)-1)
        if i != j:
            deck[i], deck[j] = deck[j], deck[i]
    return(deck)
def draw(deck, hand):
    # A function made in order to draw cards
    if len(deck) > 0:
        hand.append(deck[0])
        deck.pop(0)
        return hand[len(hand) - 1]
    else: 
        print(" The deck is empty")

def deal(deck, h1 = [], h2 = [], number = 4):
    # The dealing function 
    for i in range(number*2):
        if deck > 0:
            if i%2 == 0: draw(deck, h1)
            else: draw(deck, h2)

    player1 =h1
    player2 =h2
    return(player1, player2)
