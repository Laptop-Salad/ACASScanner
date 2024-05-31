## Connect to our local db which allows for caching
import sqlite3

class LocalDBService:
    def __init__(self):
        self.con = sqlite3.connect("local_data.db")
        self.cur = self.con.cursor()

    def verify_card(self, card_number):
        res = self.cur.execute("SELECT id FROM known_cards WHERE card_number == '" + card_number + "'")
        return res.fetchone()

    def add_known_card(self, card_number):
       res = self.cur.execute("INSERT INTO known_cards (card_number) VALUES ( '" + card_number + "')")
       print("Added", card_number, "to local db")
       self.con.commit()
