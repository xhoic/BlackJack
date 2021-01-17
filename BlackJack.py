#Name: Xhoi Caveli
#Date: 11/09/2020
#Class: CIS-2531 NET02
#Desc: This program stimulates a simplified version of Blackjack.

import random as r

# Create deck of cards
def deckOfCards():
    deck = {'Ace of Spades' : 1, '2 of Spades': 2, '3 of Spades': 3, '4 of Spades': 4,
            '5 of Spades': 5, '6 of Spades': 6, '7 of Spades': 7, '8 of Spades': 8,
            '9 of Spades': 9, '10 of Spades': 10, 'Jack of Spades': 10,
            'Queen of Spades': 10, 'King of Spades': 10,

            'Ace of Hearts': 1, '2 of Hearts': 2, '3 of Hearts': 3, '4 of Hearts': 4,
            '5 of Hearts': 5, '6 of Hearts': 6, '7 of Hearts': 7, '8 of Hearts': 8,
            '9 of Hearts': 9, '10 of Hearts': 10, 'Jack of Hearts': 10,
            'Queen of Hearts': 10, 'King of Hearts': 10,

            'Ace of Clubs': 1, '2 of Clubs': 2, '3 of Clubs': 3, '4 of Clubs': 4,
            '5 of Clubs': 5, '6 of Clubs': 6, '7 of Clubs': 7, '8 of Clubs': 8,
            '9 of Clubs': 9, '10 of Clubs': 10, 'Jack of Clubs': 10,
            'Queen of Clubs': 10, 'King of Clubs': 10,

            'Ace of Diamonds': 1, '2 of Diamonds': 2, '3 of Diamonds': 3, '4 of Diamonds': 4,
            '5 of Diamonds': 5, '6 of Diamonds': 6, '7 of Diamonds': 7, '8 of Diamonds': 8,
            '9 of Diamonds': 9, '10 of Diamonds': 10, 'Jack of Diamonds': 10,
            'Queen of Diamonds': 10, 'King of Diamonds': 10,
            }

    listDeck = list(deck.items())
    r.shuffle(listDeck)
    shuffledDeck = dict(listDeck)

    return shuffledDeck

# Check in case of ace to add 1 or 11
def isAce(player):
    player += 11
    if player > 21:
        return False
    return True

# Checks who wins
# In case of no win return 'NOT'
def win(player1, player2):
    if player1 <= 21 and player2 <= 21:
        if player1 > player2:
            return 'PLAYER1'
        else:
            return 'PLAYER2'
    if player2 <= 21:
        return 'PLAYER2'
    if player1 <= 21:
        return 'PLAYER1'
    return 'NOT'


def play():

    deck = deckOfCards()
    player1 = 0
    player2 = 0
    deal = 0
    rounds = 0
    player1wins = 0
    player2wins = 0
    cards = len(deck)

    for i in range(cards):
        print('-->**NEW ROUND**')
        print(' '.rjust(10), format("Deal", '21s'), format('Player1', '24s'), 'Player2')
        print(' '.rjust(10), format("----", '21s'), format('-------', '24s'), '-------')

        while player1 < 21 and player2 < 21 and len(deck) != 0:
            deal += 1
            print('{:>15}'.format(deal), end='')
            card, value = deck.popitem()
            print('{:>25}'.format(card), end='')
            if value == 1 and isAce(player1):
                player1 += 11
            elif value == 1 and not isAce(player1):
                player1 += value
            else:
                player1 += value

            card, value = deck.popitem()
            print('{:>25}'.format(card))
            if value == 1 and isAce(player2) == True:
                player2 += 11
            elif value == 1 and isAce(player2) == False:
                player2 += value
            else:
                player2 += value

        else:
            rounds += 1
            print(format('==========').rjust(15),
                  format('==========').rjust(24), format('==========').rjust(24) )
            print(format('Hand Value').rjust(15), '{:20}'.format(player1), '{:>25}'.format(player2))
            print()
            if win(player1, player2) == 'PLAYER1':
                player1wins +=1
                print('Player 1 wins.')
                print()
                print()
            elif win(player1, player2) == 'PLAYER2':
                player2wins += 1
                print('Player 2 wins.')
                print()
                print()
            else:
                print('No winner.')
                print()
                print()
            player1 = 0
            player2 = 0
            deal = 0
        cards = len(deck)
        if cards == 0:
            break;
    print('**SUMMARY GAME STATISTICS**')
    print('Rounds played:', rounds)
    print('Carsd played: 52')
    print('Player 1 wins:', player1wins)
    print('Player 2 wins:', player2wins)


def main():

    play()

main()

'''**SAMPLE OUTPUT**
-->**NEW ROUND**
           Deal                  Player1                  Player2
           ----                  -------                  -------
              1            3 of Diamonds              10 of Clubs
              2              7 of Hearts           King of Hearts
              3            2 of Diamonds               4 of Clubs
     ==========               ==========               ==========
     Hand Value                   12                        24

Player 1 wins.


-->**NEW ROUND**
           Deal                  Player1                  Player2
           ----                  -------                  -------
              1             10 of Spades              5 of Hearts
              2         King of Diamonds            4 of Diamonds
              3           Jack of Spades            King of Clubs
     ==========               ==========               ==========
     Hand Value                   30                        19

Player 2 wins.


-->**NEW ROUND**
           Deal                  Player1                  Player2
           ----                  -------                  -------
              1            Ace of Hearts               6 of Clubs
              2           Queen of Clubs              9 of Hearts
     ==========               ==========               ==========
     Hand Value                   21                        15

Player 1 wins.


-->**NEW ROUND**
           Deal                  Player1                  Player2
           ----                  -------                  -------
              1              6 of Hearts            9 of Diamonds
              2              4 of Hearts               7 of Clubs
              3          Queen of Spades               2 of Clubs
              4            5 of Diamonds              3 of Spades
     ==========               ==========               ==========
     Hand Value                   25                        21

Player 2 wins.


-->**NEW ROUND**
           Deal                  Player1                  Player2
           ----                  -------                  -------
              1               5 of Clubs            6 of Diamonds
              2            Jack of Clubs              6 of Spades
              3             10 of Hearts            Ace of Spades
     ==========               ==========               ==========
     Hand Value                   25                        13

Player 2 wins.


-->**NEW ROUND**
           Deal                  Player1                  Player2
           ----                  -------                  -------
              1             Ace of Clubs        Queen of Diamonds
              2           King of Spades              2 of Hearts
     ==========               ==========               ==========
     Hand Value                   21                        12

Player 1 wins.


-->**NEW ROUND**
           Deal                  Player1                  Player2
           ----                  -------                  -------
              1               8 of Clubs               3 of Clubs
              2         Jack of Diamonds              3 of Hearts
              3              8 of Spades          Queen of Hearts
     ==========               ==========               ==========
     Hand Value                   26                        16

Player 2 wins.


-->**NEW ROUND**
           Deal                  Player1                  Player2
           ----                  -------                  -------
              1           10 of Diamonds              4 of Spades
              2            7 of Diamonds              8 of Hearts
              3               9 of Clubs              2 of Spades
     ==========               ==========               ==========
     Hand Value                   26                        14

Player 2 wins.


-->**NEW ROUND**
           Deal                  Player1                  Player2
           ----                  -------                  -------
              1          Ace of Diamonds              7 of Spades
              2            8 of Diamonds              9 of Spades
              3           Jack of Hearts              5 of Spades
     ==========               ==========               ==========
     Hand Value                   29                        21

Player 2 wins.


**SUMMARY GAME STATISTICS**
Rounds played: 9
Carsd played: 52
Player 1 wins: 3
Player 2 wins: 6
'''