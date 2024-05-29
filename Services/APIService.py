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
        student_request = requests.get(self.url + "/students", headers = self.headers).json()

        card_numbers = []

        students = student_request['items']

        for student in range (len(students)):
        	card_numbers.append(students[student]["card_number"])

        return card_numbers

