## Producers
from Producers.CardScanner import CardScanner
from Producers.GenerateReport import GenerateReport

## Consumers
from Consumers.CardHandler import CardHandler
from Consumers.ReportGenerator import ReportGenerator

## Services
from Services.APIService import APIService
from Services.LocalDBService import LocalDBService

## Fakers
from Fakers.CardScannerFaker import CardScannerFaker

## Instantiating producers
card_scanner = CardScanner()
generate_report = GenerateReport()

## Instantiating services
api_service = APIService()
local_db_service = LocalDBService()

# Get all card numbers
card_numbers = api_service.get_card_numbers() # This would not be required in the real app

## Instantiating consumers
card_handler = CardHandler(api_service, local_db_service)
report_generator = ReportGenerator(api_service, card_numbers)

## Instantiating fakers
scanner_faker = CardScannerFaker(card_numbers, card_scanner, api_service, generate_report)

## Wiring up consumers -> producers
card_scanner.add_subscriber(card_handler)
generate_report.add_subscriber(report_generator)

## Running faker for 4 days
# In practice this would be wiring up our hardware listeners to the card producer
scanner_faker.generate("31052024",7)

# Generate the report
generate_report.click_generate("31052024")
