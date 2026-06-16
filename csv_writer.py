import csv
import os
from datetime import datetime


class csv_writer:
    def __init__(self, path: str, headers=None):
        self.path = path
        self.headers = headers or ["timestamp", "raw_data"]
        self.file = None
        self.writer = None

    def open(self):
        file_exists = os.path.exists(self.path)
        self.file = open(self.path, "a", newline="", encoding="utf-8")
        self.writer = csv.writer(self.file)

        if not file_exists:
            self.writer.writerow(self.headers)
            self.file.flush()

    def write_raw(self, raw_data: str):
        if self.writer is None or self.file is None:
            raise RuntimeError("writer is not open, call open() first")

        ts = datetime.now()
        self.writer.writerow([ts, raw_data])
        self.file.flush()

    def write_row(self, row):
        if self.writer is None or self.file is None:
            raise RuntimeError("writer is not open, call open() first")
        self.writer.writerow(row)
        self.file.flush()

    def close(self):
        if self.file:
            self.file.close()
            self.file = None
            self.writer = None
