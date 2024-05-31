import random
from datetime import datetime
from datetime import timedelta

class CardScannerFaker:
    def __init__(self, card_numbers, producer):
        self.scanner = producer
        self.card_numbers = card_numbers

    def format_time(self, time):
        if time < 10:
            time = "0" + str(time)
        return time

    def generate_day(self, date):
        print()
        print("New day", date)
        for card_number in self.card_numbers:
            #generate random time
            random_hour = random.randrange(8,10)
            random_minute = random.randrange(0,60)
            random_second = random.randrange(0,60)

            #formating the time
            random_minute = self.format_time(random_minute)
            random_second = self.format_time(random_second)
            time = "0" + str(random_hour)+str(random_minute)+ str(random_second)

            self.scanner.scan_card(card_number, date, time)


    def generate(self, start_date, days_add):
        """Generate card entries for days_add amount of days

        Keyword arguments:
        start_date -- the day to start generating entries from (format "ddmmyyyy")
        days_add -- how many days to generate card entries for
        """
        start_date = start_date
        begin_date = datetime.strptime(start_date, "%d%m%Y")

        for i in range (0, days_add):
            begin_date = begin_date + timedelta(days = 1)
            formatted_date = begin_date.strftime ("%d%m%Y")
            self.generate_day(formatted_date)
