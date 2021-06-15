import sqlite3
import os

conn = sqlite3.connect("organizer.db")


class Tasks:
    def __init__(self, task, exp_date):
        self.task = task
        self.exp_date = exp_date

    def test(self):
        print("Zadania działają")
