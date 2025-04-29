# Rules:
# Try to get as close to 21 without going over.
# Kings, Queens, and Jacks are worth 10 points.
# Aces are worth 1 or 11 points.
# Cards 2 through 10 are worth their face value.
# (H)it to take another card.
# (S)tand to stop taking cards.
# On your first play, you can (D)ouble down to increase your bet but must hit exactly one more time before standing.
# In case of a draw, the bet is returned to the player.
# The dealer stops hitting at 17.
import os, sys, random

# Step 1 - Set Constants and Ask for bet
HEARTS = chr(9829)  # ♥ 
CLUBS = chr(9827)   # ♣
SPADES = chr(9824)  # ♠
DIMONDS = chr(9830) # ♦
BACKSIDE = 'backside'

money = 5000
os.system('cls')
print(f"{SPADES}{CLUBS}{DIMONDS}{HEARTS}  Welcome to Black Jack  {HEARTS}{DIMONDS}{CLUBS}{SPADES}")

# Step 2 - Get Bet
def get_bet(maxBet):
    """Asl the player how much money they want to ber for the round"""
    while True:
        print("How much do you want to bet? (1-{}, or (Q)UIT)".format(maxBet))
        bet = input('> ').upper()
        bet.split()
        if bet == 'Q':
            print("Thank you for playing{}".format(HEARTS))
            sys.exit()
        if not bet.isdecimal():
            continue
        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet

# Step 3 - Get Deck
def get_deck():
    """Return a list of tuples (rank, suit) for all 52 cards"""
    deck = []
    for suit in (HEARTS,CLUBS,DIMONDS,SPADES):
        for rank in range(2, 11): #It ends in eleven becuse last number is not taken into accountso range actually is 2-10
            deck.append((str(rank), suit)) #Here we add the numbered cards
        for rank in ('J','Q','K','A'):
            deck.append((rank,suit)) #Here we add the face and ace cards
    random.shuffle(deck)
    return deck

# Step 4 - Display Cards
def display_cards(cards):
    """Display all the cards in the card list"""
    rows = ['','','','','']
    for card in cards:
        rows[0] += " ___ "
        if card == BACKSIDE:
            rows[1] += "|## | "
            rows[2] += "|###| "
            rows[3] += "|_##| "
        else:
            rank, suit = card
            rows[1] += '|{} |'.format(rank.ljust(2))
            rows[2] += '| {} |'.format(suit)
            rows[3] += '|_{}|'.format(rank.rjust(2, '_'))
    for row in rows:
        print(row)

# Step 5 - Get Hand Values
def get_hand_value(cards):
    """Return value of cards"""
    value = 0
    number_aces = 0
    for card in cards:
        rank = card[0]
        if rank == "A":
            number_aces += 1
        elif rank in ('K','J',"Q"):
            value += 10
        else:
            value += int(rank)
    value += number_aces
    for i in range(number_aces): #Determines if to play Ace as 1 or 11 without going over
        if value + 10 <= 21:
            value += 10
    return value

# Step 6 - Display Hands
def display_hands(player_hand,dealer_hand,show_dealer_hand):
    """Show player's and dealer's hand"""
    print()
    if show_dealer_hand:
        print("DEALER", get_hand_value(dealer_hand))
        display_cards(dealer_hand)
    else:
        print("DEALER: ???")  
        display_cards([BACKSIDE]+dealer_hand[1:]) #Hide Dealer's first card
    print("PLAYER:",get_hand_value(player_hand))
    display_cards(player_hand) #Show the player's cards

# Step 7 - Get Move
def get_move(player_hand, money):
    """Asks player for their move, return H,S,D"""
    while True:
        # Determine what move the player can make
        moves = ["(H)it", "(S)tay"]
        if player_hand == 2 and money > 0:
            moves.append("(D)ouble Down")
        #Asks from player the move, by showing options
        move_prompt = ", ".join(moves)+ ">"
        move = input(move_prompt).upper()
        if move in ("H","S"):
            return move
        if move == ("D") and "(D)ouble Down" in moves:
            return move


#main progream
while True:       
        if money <= 0: #Checking if player still has money to play
                print("It is good that you weren't playing with real money!")
                print(f"{HEARTS} Thank you for playing {HEARTS}")
                sys.exit()
        #Ask Player for bet
        print("Your Money:" , money)
        bet = get_bet(money) #Get bet
        deck = get_deck()  #get Deck
        dealer_hand = [deck.pop(), deck.pop()] #Give the dealer and player two cards from the deck
        player_hand = [deck.pop(), deck.pop()]
        #Handle player's actions
        print("Bet:", bet)
        while True:
            display_hands(player_hand,dealer_hand,False)
            print()
            #Check if player has gone over 21
            if get_hand_value(player_hand) > 21:
                break
            #Get player's move
            move = get_move(player_hand, money - bet)
            #Handles playe move
            if move == 'D':
                #Increase the Bet
                additional_bet = get_bet(min(bet,(money-bet)))
                bet += additional_bet
                print(f"Bet Invrese to {bet}")
                print('Bet:', bet)
            if move in ('H','D'):
                #Get another card
                new_card = deck.pop()
                rank, suit = new_card
                print(f"You draw a {rank} of {suit}.")
                player_hand.append(new_card)
                #Check if player has bust
                if get_hand_value(player_hand) > 21:
                    continue
            if move == "S":
                #Stops player's turn
                break
        #Handle dealer's action
        if get_hand_value(player_hand) <= 21:
            while get_hand_value(dealer_hand) < 17:
                #Dealer gets a new card
                print("The dealer drew a card")
                dealer_hand.append(deck.pop())
                display_hands(player_hand, dealer_hand, True)
                if get_hand_value(dealer_hand) > 21:
                    #The dealer has gone over
                    break
                input("Press enter to continue..")
                print("\n\n")
        display_hands(player_hand, dealer_hand, True)
        player_value = get_hand_value(player_hand)
        dealer_value = get_hand_value(dealer_hand)
        #Handle whether the player won, lost or draw
        if dealer_value > 21: #Dealer Bust
            print(f"Dealer busts! You win ${bet}!")
            money += bet
        elif player_value > 21 or player_value < dealer_value: #Player Bust
            print("You Loose!")
            money -= bet
        elif player_value > dealer_value: #Player Won
            print(f"Dealer busts! You win ${bet}!")
            display_hands(player_hand, dealer_hand, True)
            money += bet
        elif player_value == dealer_value: #Player and Dealer draw
            print("It's a draw and the money will be retruned to you!")
        input("Press enter to continue..")
        print("\n\n")
        os.system('cls')