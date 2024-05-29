from Consumers.Consumer import Consumer
from Producers.CardScanner import CardScanner

class CardHandler(Consumer):
    """
    This is subscribed to the card_scanned event
    """
    subscribers = []

    def update(self, producer, *args):
        if isinstance(producer, CardScanner):
            card_number = producer.card_number
            print(card_number, "scanned")