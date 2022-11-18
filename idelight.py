import cards

def deal_hand(deck, h1 = [], h2 = [],):
    all = cards.deal(deck, h1, h2, 4)
    return all
def discard(hand, number):
    if number != 4 or number != 2:
        if len(hand) < 4:
            return hand
    if number == 4:
        hand.clear()
        return hand
    if number == 2:
        hand.remove(hand[len(hand)-2])
        hand.remove(hand[len(hand)-3])
        return hand
def play_round(deck, hand):
    while len(hand) < 4:
        cards.draw(deck, hand)
        if hand[len(hand) - 1][0] == hand[len(hand) - 4][0]:
            discard(hand, 4)
        elif hand[len(hand) - 2][1] == hand[len(hand) - 3][1]:
            discard(hand, 2)
    return hand, deck

def main():
    deck = cards.shuffle()
    player1 = []
    player2 = []
    deal_hand(deck, player1), player2
    i = 0
    
    while len(deck) != 0:
        if i%2 == 0:
            play_round(deck, player1)
        else: play_round(deck, player2)

    # If statement made in order to display the results of the game based on the condition of the code

    if len(player1) == 0 and len(player2) != 0:
        print("P1 wins")
    elif len(player1) != 0 and len(player2) == 0: 
        print("P2 wins")
    elif len(player1) and len (player2) != 0: 
        (print("Nobody won, try again"))
    elif len(player1) == len(player2) == 0:
        print("tie, try again")
    i += 1

a = [1, 2, 3, 4]
print(discard(a, 3))

