import requests
import random

school_id = "<school_id>"

headers = {"Authorization": "Bearer <token>"}
students = (requests.get("https://asms.amandawallis.com/api/school/<school_id>/students", headers = headers).json())

card_numbers = {
}

students = students['0']

for student in students:
	card_numbers[student ["card_number"]] = False
	card_numbers["time"] = ""

# print(card_numbers)

random_card = random.choice(list(card_numbers.keys()))
random_hour = random.randrange(8,9)
random_minute = random.randrange(0,59)
random_second = random.randrange(0,59)
random_card = str(random_card)

# print(random_card)

date = "17052024"
if random_minute < 10:
	random_minute = "0" + str(random_minute)
if random_second < 10:
	random_second = "0" + str(random_second)
time = "0" + str(random_hour)+str(random_minute)+ str(random_second)

url = "https://asms.amandawallis.com/api/school/<school_id>/students/" + random_card + "/card_entries"
print(random_card)
myobj = {"date": date + " " + time}

response = requests.post(url, headers = headers , json = myobj)
print(response)
