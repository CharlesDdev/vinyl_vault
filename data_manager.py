# Handles saving and loading of records (Feature 3)
import json
import os

class DataManager:
    def __init__(self, filename="records.json"):
        self.filename = filename
        self.records = []
        self.load_records()

    def load_records(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                self.records = json.load(f)
        return self.records

    def save_records(self, records):
        self.records = records
        with open(self.filename, "w") as f:
            json.dump(self.records, f, indent=4)
