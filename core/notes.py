import sqlite3
import os

conn = sqlite3.connect("organizer.db")


class Notes:
    def __init__(self,note):
        self.note = note

    def test(self):
        print("Notatki działają")
