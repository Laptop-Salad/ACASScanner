import requests
import random
from dotenv import load_dotenv
import os
from datetime import datetime
from datetime import timedelta

load_dotenv()

school_id = os.getenv("SCHOOL_ID")
token = os.getenv("TOKEN")
url = "https://asms.amandawallis.com/api/school/" + school_id

headers = {"Authorization": "Bearer " + token}
students = (requests.get(url + "/students", headers = headers).json())

card_numbers = []

students = students['0']

for student in range (len(students)):
	#putting card numbers into array
	card_numbers.append(students[student]["card_number"])



print(card_numbers)

def format_time(time):
	if time < 10:
		time = "0" + str(time)
	return time

def generate_day(date):
	for x in card_numbers:
	#generate random time
		random_hour = random.randrange(8,9)
		random_minute = random.randrange(0,59)
		random_second = random.randrange(0,59)
	
	#formating the time
		random_minute = format_time(random_minute)
		random_second = format_time(random_second)
		time = "0" + str(random_hour)+str(random_minute)+ str(random_second)
	
		url = "https://asms.amandawallis.com/api/school/" + school_id + "/students/" + x + "/card_entries"
		print(x)
		print(time)
		print(date)
		myobj = {"date": date + " " + time}

		response = requests.post(url, headers = headers , json = myobj)
		print(response)

def generate_more_days(start_date, days_add):
	"""Generate card entries for days_add amount of days
	
	Keyword arguments:
	start_date -- the day to start generating entries from (format ddmmyyyy)
	days_add -- how many days to generate card entries for
	"""
	start_date = str(start_date)
	begindate = datetime.strptime(start_date, "%d%m%Y")
	print(start_date)
	end_date = begindate + timedelta(days = days_add)
	print(end_date)
	end_date = end_date.strftime ("%d%m%Y")
	print(end_date)
	
generate_more_days(28052024,10)
		







#function generate for a day (date)
#random student number that is selected
#change scanned to true
#set time to random time that has been generated
#record card number that has been used
#do for each student (leaving out students that have been done before)
#save for that day
#repeat for the week
#generate statistics
#extra generate if they showes up - generate 1-100 if 90 or above mia bellow showed up
