from project.card.card import Card


class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards = []

    def add(self, card: Card):
        if card in self.cards:
            raise ValueError(f"Card {card.name} already exists!")

        self.cards.append(card)
        self.count += 1

    def remove(self, card: str):
        if not card:
            raise ValueError("Card cannot be an empty string!")

        card_to_remove = self.find(card)
        self.cards.remove(card_to_remove)
        self.count -= 1

    def find(self, name):
        return [card for card in self.cards if card.name == name][0]
