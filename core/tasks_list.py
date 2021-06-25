import sqlite3

conn = sqlite3.connect("organizer.db")


class TaskList:
    def __init__(self, title, exp_date, task, complete):
        self.title = title
        self.exp_date = exp_date
        self.task = task
        self.complete = complete

    def add_tasks_list(self):
        pass
