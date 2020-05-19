from deck import Deck
from hand import Hand
from chip import Chip

playing = True

def take_bet(chips):
    while True:

        try:
            chips.bet = int(input("You have 100 chips. How much would you like to wager? "))
        except:
            print("Sorry, please provide an integer")
        else:
            if chips.bet > chips.total:
                print("You don't have enough chips to make that wager")
            elif chips.bet <= 0:
                print("You can't make that wager")
            else:
                break

def hit(deck, hand):
    card = deck.deal()
    hand.add_card(card)
    hand.adjust_for_aces()

def hit_or_stand(deck, hand):
    global playing

    while True:
        decision = input("\nType Hit or Stand: ")

        if decision[0].lower() == 'h':
            hit(deck, hand)
        elif decision[0].lower() == 's':
            print("Player stands. Dealer's turn")
            playing = False
        else:
            print("Invalid decision. Please type Hit or Stand")
            continue
        break

def player_busts(player, dealer, chips):
    print("Player BUSTS!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("Player WINS!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("Player WINS! Dealer BUSTS!")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("Dealer WINS!")
    chips.lose_bet()

def push():
    print("Dealer and player tie. PUSH!")

def show_some(player, dealer):
    print("Dealer's hand:")
    print(dealer.cards[0])
    print("???\n")
    print("Player's hand:")
    for card in player.cards:
        print(card)

def show_all(player, dealer):
    print("\nDealer's hand:")
    for card in dealer.cards:
        print(card)
    print('\n')
    print("Player's hand:")
    for card in player.cards:
        print(card)

def replay():
    rematch = ""

    while rematch != "Y" and rematch != "N":
        rematch = input("Play another hand? [Y/N]\n").upper().strip()

    return rematch == "Y"

while True:
    print("\nWelcome to BLACKJACK")
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chip()

    take_bet(player_chips)

    show_some(player_hand, dealer_hand)

    while playing:
        hit_or_stand(deck, player_hand)
        show_some(player_hand, dealer_hand)
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push()

    print("\nPlayer's total chips are at: {}".format(player_chips.total))

    if not replay():
        print("Thank you for playing")
        break
    else:
        playing = True
