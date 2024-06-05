import random
from datetime import datetime
from datetime import timedelta

class CardScannerFaker:
    def __init__(self, card_numbers, producer, api_service, generate_report):
        self.scanner = producer
        self.card_numbers = card_numbers
        self.api_service = api_service
        self.generate_report = generate_report

    def format_time(self, time):
        if time < 10:
            time = "0" + str(time)
        return time

    def generate_day(self, date):
        for card_number in self.card_numbers:
            points = self.api_service.get_student_points(card_number)
            print("New day", date)
            
            #generate random time
            if points <= 100 and points > 75:
                 random_hour = 8
                 random_minute = random.randrange(0,60)
            elif points <= 75 and points > 50:
                 random_hour = random.randrange(8,10)
                 if random_hour == 8:
                     random_minute = random.randrange(10,60)
                 else:
                    random_minute = random.randrange(0,6)
            elif points <= 50 and points > 25:
                random_hour = random.randrange(8,10)
                if random_hour == 8:
                    random_minute = random.randrange(20,60)
                else:
                    random_minute = random.randrange(0,11)
            elif points <= 25 and points > 0:
                random_hour = random.randrange(8,10)
                if random_hour == 8:
                    random_minute = random.randrange(30,60)
                else:
                    random_minute = random.randrange(0,16)
            elif points <= 0 and points > -25:
                random_hour = random.randrange(8,10)
                if random_hour == 8:
                    random_minute = random.randrange(40,60)
                else:
                    random_minute = random.randrange(0,26)
            elif points <= -25 and points > -50:
                random_hour = random.randrange(8,10)
                if random_hour == 8:
                    random_minute = random.randrange(45,60)
                else:
                    random_minute = random.randrange(0,41)
            elif points <= -50 and points > -75:
                random_hour = random.randrange(8,10)
                if random_hour == 8:
                    random_minute = random.randrange(50,60)
                else:
                    random_minute = random.randrange(0,51)
            elif points <= -75 and points >= -100:
                random_hour = random.randrange(8,10)
                if random_hour == 8:
                    random_minute = random.randrange(55,60)
                else:
                    random_minute = random.randrange(0,60)
            
            random_second = random.randrange(0,60)

            #formating the time
            random_minute = self.format_time(random_minute)
            random_second = self.format_time(random_second)
            date = str(date)
            time = "0" + str(random_hour)+str(random_minute)+ str(random_second)
            
            self.scanner.scan_card(card_number, date, time)
            
            print(self.api_service.get_student_entry_by_date(card_number, date))

    def generate(self, start_date, days_add = 0):
        """Generate card entries for days_add amount of days

        Keyword arguments:
        start_date -- the day to start generating entries from (format "ddmmyyyy")
        days_add -- how many days to generate card entries for (optional)
        """
        start_date = start_date
        begin_date = datetime.strptime(start_date, "%d%m%Y")

        # generate for first day
        self.generate_day(begin_date)
        
        for i in range (0, days_add):
            begin_date = begin_date + timedelta(days = 1)
            formatted_date = begin_date.strftime ("%d%m%Y")
            self.generate_day(formatted_date)                
                
        #self.generate_report.click_generate(students)
            


