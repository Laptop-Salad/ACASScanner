from Consumers.Consumer import Consumer
from Producers.CardScanner import CardScanner

class CardHandler(Consumer):
    """
    This is subscribed to the CardScanner producer
    """
    subscribers = []

    def __init__(self, api_service):
        self.api_service = api_service

    def update(self, producer, *args):
        if isinstance(producer, CardScanner):
            card_number = producer.card_number
            scanned_time = producer.scanned_time
            scanned_date = producer.scanned_date

            self.api_service.post_card_entry (card_number, scanned_date, scanned_time)
            print(card_number, "scanned at", scanned_time)
