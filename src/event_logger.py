import csv

class EventLogger:
    def __init__(self, filepath):
        self.file = open(filepath, "w", newline="")
        self.writer = csv.writer(self.file)
        self.writer.writerow(["step", "event_type", "details"])

    def log(self, step, event_type, details):
        self.writer.writerow([step, event_type, details])

    def close(self):
        self.file.close()