from Consumers.Consumer import Consumer
from Producers.CardScanner import CardScanner

class CardHandler(Consumer):
    """
    This is subscribed to the CardScanner producer
    """
    subscribers = []

    def __init__(self, api_service, local_db_service):
        self.api_service = api_service
        self.local_db_service = local_db_service

    def update(self, producer, *args):
        if isinstance(producer, CardScanner):
            card_number = producer.card_number
            scanned_time = producer.scanned_time
            scanned_date = producer.scanned_date

            # Verify card number is real through local db
            known_card = self.local_db_service.verify_card(card_number)

            if (known_card == None):
                # If not in known_cards verify through API
                if (self.api_service.get_student_from_card(card_number) == False):
                    print("Card number invalid. Verified through API")
                    return
                else:
                    print("Verified card number as valid through API")
                    self.local_db_service.add_known_card(card_number)
            else:
                print("Verified card number as valid through local db")


            self.api_service.post_card_entry (card_number, scanned_date, scanned_time)
            print(card_number, "scanned at", scanned_time)
