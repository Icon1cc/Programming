"""
Create a log writer function that appends time + message to a file
"""

from datetime import datetime

def write_log(message):
    timestamp = datetime.now()
    with open("logfile.txt", "a") as f:
        f.write(f"[{timestamp}] {message}\n")

write_log("User logged in.")
write_log("Something went wrong.")
write_log("New file inserted")
