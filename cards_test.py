import cards
import idelight
import random as rand
# A testing file made in order to test the functions

def test_make_card():
    o1 = cards.make_card(0, 0)
    o2 = cards.make_card(9, 1)
    o3 = cards.make_card(10, 2)
    o4 = cards.make_card(11, 3)
    o5 = cards.make_card(12, 0)
    assert o1 == (1, 'S', 'Ace of Spades', '\x1b[34mAS\x1b[37m')
    assert o2 == (10, 'H', 'Ten of Hearts', '\x1b[31m10H\x1b[37m')
    assert o3 == (11, 'C', 'Jack of Clubz', '\x1b[34mJC\x1b[37m')
    assert o4 == (12, 'D', 'Queen of Diamonds', '\x1b[31mQD\x1b[37m')
    assert o5 == (13, 'S', 'King of Spades', '\x1b[34mKS\x1b[37m')

def test_make_deck():
    o = cards.make_deck()
    assert o[0][1] == 'S'
    assert o[13][1] == 'H'
    assert o[26][1] == 'C'
    assert o[39][1] == 'D'

def test_shuffle():
    rand.seed = 1
    o1 = cards.make_deck()
    o2 = cards.shuffle()
    assert o1[1] != o2[1]
def test_deal(): 
    output = cards.deal(cards.make_deck())
    assert len(output[0]) == len(output[1]) == 4

def test_discard():
    input = [1, 2, 3, 4]
    o1 = idelight.discard(input, 4)
    o2 = idelight.discard(input, 2)
    o3 = idelight.discard(input, 3)
    assert o1 == []
    assert o2 == [1, 4]
    assert o3 == [1, 2, 3, 4]