# Services/APIService
import requests
from dotenv import load_dotenv
import os

class APIService:
    def __init__(self):
        load_dotenv()

        self.school_id = os.getenv("SCHOOL_ID")
        self.token = os.getenv("TOKEN")
        self.url = "https://asms.amandawallis.com/api/schools/" + self.school_id
        self.headers = {"Authorization": "Bearer " + self.token}

    def get_card_numbers(self):
        student_request = requests.get(self.url + "/students?sort=-performance", headers = self.headers).json()

        card_numbers = []

        students = student_request['items']

        for student in range (len(students)):
        	card_numbers.append(students[student]["card_number"])

        return card_numbers
        
    def post_card_entry (self, card_number, date, time):
        url = self.url + "/students/" + card_number + "/card-entries"
        myobj = {"date": date + " " + time}

        response = requests.post(url, headers = self.headers , json = myobj)
        print(response)

    def post_report(self, data):
        print("Uploading report...")
        url = self.url + "/reports"
        response = requests.post(url, headers = self.headers , json = data)
        print(response)

    def get_student_from_card(self, card_number):
        url = self.url + "/students/" + card_number

        response = requests.get(url, headers = self.headers).json()

        return response['status'] == 200

    def check_service(self):
        pass


