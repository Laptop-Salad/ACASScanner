import random
from datetime import datetime, timedelta

class CardScannerFaker:
    def __init__(self, card_numbers, producer, api_service, generate_report):
        self.scanner = producer
        self.card_numbers = card_numbers
        self.api_service = api_service
        self.generate_report = generate_report

    def format_time(self, time):
        return f"{time:02}"

    def generate_random_time(self, points):
        if points <= 100 and points > 75:
            random_hour = 8
            random_minute = random.randrange(0, 60)
        elif points <= 75 and points > 50:
            random_hour = random.randrange(8, 10)
            random_minute = random.randrange(10, 60) if random_hour == 8 else random.randrange(0, 6)
        elif points <= 50 and points > 25:
            random_hour = random.randrange(8, 10)
            random_minute = random.randrange(20, 60) if random_hour == 8 else random.randrange(0, 11)
        elif points <= 25 and points > 0:
            random_hour = random.randrange(8, 10)
            random_minute = random.randrange(30, 60) if random_hour == 8 else random.randrange(0, 16)
        elif points <= 0 and points > -25:
            random_hour = random.randrange(8, 10)
            random_minute = random.randrange(40, 60) if random_hour == 8 else random.randrange(0, 26)
        elif points <= -25 and points > -50:
            random_hour = random.randrange(8, 10)
            random_minute = random.randrange(45, 60) if random_hour == 8 else random.randrange(0, 41)
        elif points <= -50 and points > -75:
            random_hour = random.randrange(8, 10)
            random_minute = random.randrange(50, 60) if random_hour == 8 else random.randrange(0, 51)
        else:  # points <= -75 and points >= -100
            random_hour = random.randrange(8, 10)
            random_minute = random.randrange(55, 60) if random_hour == 8 else random.randrange(0, 60)

        random_second = random.randrange(0, 60)
        return random_hour, random_minute, random_second

    def generate_day(self, date):
        for card_number in self.card_numbers:
            points = self.api_service.get_student_points(card_number)
            print("New day", date)

            random_hour, random_minute, random_second = self.generate_random_time(points)

            # Formatting the time
            formatted_time = f"{random_hour:02}{random_minute:02}{random_second:02}"
            self.scanner.scan_card(card_number, date, formatted_time)

    def generate(self, start_date, days_add=0):
        """Generate card entries for days_add amount of days

        Keyword arguments:
        start_date -- the day to start generating entries from (format "ddmmyyyy")
        days_add -- how many days to generate card entries for (optional)
        """
        begin_date = datetime.strptime(start_date, "%d%m%Y")
        self.generate_day(begin_date.strftime("%d%m%Y"))

        for _ in range(days_add):
            begin_date += timedelta(days=1)
            self.generate_day(begin_date.strftime("%d%m%Y"))