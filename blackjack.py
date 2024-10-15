import random

# Loop for the entire game.

while True:
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A']
    player_hand = []
    dealer_hand = []

    player_plays = True
    dealer_plays = True

# Deals the card from the deck.

    def dealing_cards(turn):
        card = random.choice(deck)
        turn.append(card)
        deck.remove(card)

    for _ in range(2):
        dealing_cards(dealer_hand)
        dealing_cards(player_hand)

# Calculates the total of each hand.

    def total(turn):
        total = 0
        ace_11s = 0
        for card in turn:
            if card in range(11):
                total += card
            elif card in ['J', 'K', 'Q']:
                total += 10
            else: # For the ace card.
                total += 11
                ace_11s += 1
        while ace_11s and total > 21:
            total -= 10
            ace_11s -= 1
        return total

    def reveal_dealer_hand(full_reveal=False):
        if full_reveal:
            return f"{dealer_hand} (Total: {total(dealer_hand)})"
        else:
            return f"[{dealer_hand[0]}, 'X']"

# Game loop for when the player decides to stay or hit. Also tells the dealer when it should hit or stand.

    while player_plays or dealer_plays:
        print(f"Dealer has {reveal_dealer_hand()}")
        print(f"You have {player_hand} for a total of {total(player_hand)}.")

        if player_plays:
            Stay_or_hit = int(input("1: Stay \n2: Hit \n"))
        if total(dealer_hand) > 16:
            dealer_plays = False
        else:
            dealing_cards(dealer_hand)
        if Stay_or_hit == 1:
           player_plays = False
        if Stay_or_hit == 2:
            dealing_cards(player_hand)
        if total(player_hand) >= 21:
            break
        elif total(dealer_hand) >= 21:
            break

    print(f"\nDealer reveals: {reveal_dealer_hand(full_reveal=True)}")
    print(f"You have {player_hand} for a total of {total(player_hand)}.")

# Calculates each hand and checks for the winner.

    if total(player_hand) == 21:
        player_plays = False
        print(f"\nYou have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
        print("Blackjack! You win!")
    elif total(dealer_hand) == 21:
        dealer_plays = False
        print(f"\nYou have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
        print("Blackjack! Dealer wins!")
    elif total(player_hand) > 21:
        print(f"\nYou have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
        print("You bust! Dealer wins!")
    elif total(dealer_hand) > 21:
        print(f"\nYou have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
        print("Dealer bust! You win!")
    elif 21 - total(dealer_hand) < 21 - total(player_hand):
        print(f"\nYou have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
        print("Dealer wins!")
    elif 21 - total(dealer_hand) > 21 - total(player_hand):
        print(f"\nYou have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
        print("You win!")
    elif total(dealer_hand) == total(player_hand):
        print(f"\nYou have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
        print("It's a push!")

# Replay-ability.

    replay = input("Would you like to play again?? (Yes/No):").lower()
    if replay not in ['yes', 'y']:
        print("Thanks for playing, see you soon!")
        break