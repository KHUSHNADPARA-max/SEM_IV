import random

# Define the suits and ranks in a deck of cards
suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

# Keep track of the cards picked and the number of picks needed
cards_picked = set()
picks_needed = 0

# Loop until a card from each suit has been picked
while len(cards_picked) < 4:
    # Pick a random card from the deck
    suit = random.choice(suits)
    rank = random.choice(ranks)
    card = f"{rank} of {suit}"
    
    # Increment the number of picks needed
    picks_needed += 1
    
    # Add the picked card to the set of cards picked so far
    cards_picked.add(suit)
    
    # Print the current card picked
    print(card)

# Print the total number of picks needed
print(f"Number of picks: {picks_needed}")

# import random

# suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
# cards_picked = set()

# while len(cards_picked) < 4:
#     card = random.choice(suits) + " " + str(random.randint(1, 13))
#     cards_picked.add(card.split()[0])
#     print(card)

# print("Number of picks:", len(cards_picked) * 13)
