import os
from datetime import datetime

class Logger:
    def __init__(self):
        os.makedirs("outputs/logs", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.log_file = f"outputs/logs/run_{timestamp}.log"

    def log(self, message: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] {message}"
        print(f"  LOG: {message}")
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(entry + "\n")