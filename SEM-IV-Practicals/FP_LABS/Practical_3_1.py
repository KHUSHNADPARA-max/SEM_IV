import random

# Define the deck of cards
ranks = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

# Pick a random card from the deck
picked_rank = random.choice(ranks)
picked_suit = random.choice(suits)

# Announce the picked card
print("The card you picked is the", picked_rank, "of", picked_suit + ".")
