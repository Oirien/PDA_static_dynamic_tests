import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    card1 = Card("Heart", 5)
    card2 = Card("Diamond", 1)
    cards = [card1, card2]
    cardgame = CardGame()

    #testing for class suit
    def test_card_has_suit(self):
        self.assertEqual("Heart", self.card1.suit)

    #testing for class value
    def test_card_has_value(self):
        self.assertEqual(5, self.card1.value)

    #testing cardgame check_for_ace function
    def test_check_for_ace(self):
        self.assertEqual(self.cardgame.check_for_ace(self.card1), False)

    #testing cardgame highest_card function
    def test_highest_card(self):
        self.assertEqual(self.cardgame.highest_card(self.card1, self.card2), self.card1)

    #testing cardgame cards_total function
    def test_cards_total(self):
        self.assertEqual(self.cardgame.cards_total(self.cards), "You have a total of 6.")