from Producers.CardScanner import CardScanner
from Consumers.CardHandler import CardHandler
from Services.APIService import APIService

card_scanner = CardScanner()
card_handler = CardHandler()
api_service = APIService()

# The card handler subscribes to the card scanner and will be notify when a card has been scanned
card_scanner.add_subscriber(card_handler)

# Scan card
card_scanner.scan_card("1982736")

# Get all card numbers
print(api_service.get_card_numbers())
