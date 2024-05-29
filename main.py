from Producers.CardScanner import CardScanner
from Consumers.CardHandler import CardHandler
from Services.APIService import APIService
import random
from datetime import datetime
from datetime import timedelta

card_scanner = CardScanner()
card_handler = CardHandler()
api_service = APIService()

def format_time(time):
	if time < 10:
		time = "0" + str(time)
	return time

# The card handler subscribes to the card scanner and will be notify when a card has been scanned
card_scanner.add_subscriber(card_handler)



# Get all card numbers
card_numbers = api_service.get_card_numbers()


def generate_day(date):
	for card_number in card_numbers:
	#generate random time
		random_hour = random.randrange(8,10)
		random_minute = random.randrange(0,60)
		random_second = random.randrange(0,60)

	#formating the time
		random_minute = format_time(random_minute)
		random_second = format_time(random_second)
		time = "0" + str(random_hour)+str(random_minute)+ str(random_second)

		api_service.add_card_entry (card_number, date, time)
		print(card_number)

def generate_more_days(start_date, days_add):
	"""Generate card entries for days_add amount of days

	Keyword arguments:
	start_date -- the day to start generating entries from (format ddmmyyyy)
	days_add -- how many days to generate card entries for
	"""
	start_date = str(start_date)
	begin_date = datetime.strptime(start_date, "%d%m%Y")
	
	for i in range (0, days_add):
		begin_date = begin_date + timedelta(days = 1)
		formatted_date = begin_date.strftime ("%d%m%Y")
		generate_day(formatted_date)


generate_more_days(28052024,4)
