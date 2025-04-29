# Handles saving and loading of records (Feature 3)
import json
import os

class DataManager:
    def __init__(self, filename="records.json"): # stores records in a file namedd records.json
        self.filename = filename
        self.records = []
        self.load_records()

    def load_records(self): # loads records from the file if it exists, otherwise returns an empty list
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as f:
                    self.records = json.load(f)
            except json.JSONDecodeError:
        else:
            self.records = [
                {"artist": "The Beatles",
                "album": "Abbey Road",
                "year": 1969,
                "genre": "Rock",
                "condition": "Excellent"
            },
            {
                "artist": "Pink Floyd",
                "album": "Dark Side of the Moon",
                "year": 1973,
                "genre": "Rock",
                "condition": "Good"
            },
            {
                "artist": "Miles Davis",
                "album": "Kind of Blue",
                "year": 1959,
                "genre": "Jazz",
                "condition": "Mint"
            },
            {
                "artist": "Nirvana",
                "album": "Nevermind",
                "year": 1991,
                "genre": "Grunge",
                "condition": "Fair"
            },
            {
                "artist": "Fleetwood Mac",
                "album": "Rumours",
                "year": 1977,
                "genre": "Rock",
                "condition": "Excellent"
            },
            {
                "artist": "Bob Dylan",
                "album": "Highway 61 Revisited",
                "year": 1965,
                "genre": "Folk Rock",
                "condition": "Good"
            },
            {
                "artist": "The Rolling Stones",
                "album": "Sticky Fingers",
                "year": 1971,
                "genre": "Rock",
                "condition": "Poor"
            },
            {
                "artist": "Aretha Franklin",
                "album": "I Never Loved a Man the Way I Love You",
                "year": 1967,
                "genre": "Soul",
                "condition": "Mint"
            },
            {
                "artist": "Radiohead",
                "album": "OK Computer",
                "year": 1997,
                "genre": "Alternative",
                "condition": "Excellent"
            },
            {
                "artist": "Joni Mitchell",
                "album": "Blue",
                "year": 1971,
                "genre": "Folk",
                "condition": "Good"
            },
            {
                "artist": "testrecord1",
                "album": "testalbum1",
                "year": 2025,
                "genre": "Hip Hop",
                "condition": "ExcellentTEST"
            }
            ]
            self.save_records(self.records)
        return self.records

    def save_records(self, records): # saves the provided records to the file, overwriting previous
        self.records = records
        try:
            with open(self.filename, "w") as f:
                json.dump(self.records, f, indent=4)
        except Exception as e:
            raise Exception(f"Error saving records: {e}")
