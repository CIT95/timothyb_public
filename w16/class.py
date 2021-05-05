class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, card):
        self.hand.append(card)


class HandLimitPlayer(Player):
    def __init__(self, name, limit):
        super().__init__(name)
        self.limit = limit

    def draw(self, card):
        if len(self.hand) < self.limit:
            self.hand.append(card)
            return True
        return False


class ScoreLimitPlayer(Player):
    def __init__(self, name, limit):
        super().__init__(name)
        self.limit = limit

    def draw(self, card):
        global valueHand
        if valueHand(self.hand) < self.limit:
            self.hand.append(card)
            return True
        return False


# Placeholder of valueHand function in actual dev
def valueHand(hand):
    return 10


theo = HandLimitPlayer("Theodore", 3)
ronald = ScoreLimitPlayer("Ronald", 18)

if theo.draw("Ace of Spades"):
    print("Theodore drew a card.")
if theo.draw("Ace of Clubs"):
    print("Theodore drew a card.")
if theo.draw("Ace of Diamonds"):
    print("Theodore drew a card.")
if theo.draw("Ace of Hearts"):
    print("Theodore drew a card.")
print(theo.hand)

if ronald.draw("Ten of Clubs"):
    print("Ronald drew a card.")
ronald.limit = 9
if ronald.draw("Ten of Spades"):
    print("Ronald drew a card.")
print(ronald.hand)
