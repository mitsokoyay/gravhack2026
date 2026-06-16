import csv
import os
from datetime import datetime 

class csv_writer:
    def init(self, path: str, headers=None):
        self.path = path
        self.headers = headers or ["timestamp", "raw_data"]
        self.file = None
        self.writer = None

    def open(this):
        file_exits = os.path.exits(self.path)
        self.file = open(this.path, "a", newline="", encoding="utf-8")
        self.writer = csv.writer(this.file)

        if not file_exists:
            self.writer.writerow(self.headers)
            self.file.flush()
    
    def write_raw(self, raw_data: str):
        ts = datetime.now()
        self.writer.writerow([ts, raw_data])
        self.file.flush()

    def write_row(self, row):
        self.writer.writerow(row)
        self.file.flush()

    def close(self):
        if self.file:
            self.file.close()

    print("worked")
