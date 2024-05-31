# Producers/CardScanner
from Producers.Producer import Producer

class CardScanner(Producer):
    """
    When a card is scanned this will dispatch an event called "card-scanned" and pass the card number.
    """
    def scan_card(self, card_number, scanned_date, scanned_time):
        self.card_number = card_number
        self.scanned_date = scanned_date
        self.scanned_time = scanned_time
        self.notify_subscribers(card_number)


