# ==============================
# 1. IMPORTS
# ==============================
from email.mime.image import MIMEImage
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import webbrowser
import string
import random
from datetime import datetime, timedelta
import time
import sqlite3
from pathlib import Path
import json
import csv
from zipfile import ZipFile
import shutil
from time import ctime

# ==============================
# 2. PATHLIB BASICS
# ==============================

# Create a Path object using an absolute Windows path
Path(r"C:\Program Files\Microsoft")

# Create a Path object using a relative path (Unix-style example)
Path("user/local/bin")

# Create a Path object for the CURRENT working directory
Path()

# Create a Path object pointing to a specific file using a relative path
Path("ecommerce/__init__.py")

# Build a path step by step using the / operator (portable and recommended)
Path() / "ecommerce" / "__init__.py"

# Get the path to the current user's HOME directory
Path.home()

# Create a Path object and store it in a variable
path_1 = Path("ecommerce/__init__.py")

# Check if the path exists on the filesystem (returns True or False)
path_1.exists()

# Check if the path points to a file
path_1.is_file()

# Check if the path points to a directory
path_1.is_dir()

# Print only the file name with extension
print(path_1.name)

# Print the file name without its extension
print(path_1.stem)

# Print the file extension
print(path_1.suffix)

# Print the parent directory of the file
print(path_1.parent)

# Change the file extension to .txt (creates a NEW Path object)
path_1 = path_1.with_suffix(".txt")
print(path_1)

# Change the file name to "file.txt" (creates a NEW Path object)
path_1 = path_1.with_name("file.txt")

# Print the absolute path (full path from the root directory)
print(path_1.absolute())


# ==============================
# 3. DIRECTORY OPERATIONS (commented examples)
# ==============================

# Create a Path object pointing to a directory named "Modules"
path_2 = Path("Modules")

# Create the directory (uncomment to use)
# path_2.mkdir()

# Remove the directory (must be empty) (uncomment to use)
# path_2.rmdir()

# Rename the directory (uncomment to use)
# path_2.rename("ecommerce2")


# ==============================
# 4. ITERATING OVER DIRECTORIES AND FILE SEARCH
# ==============================

# Iterate over all items (files and folders) inside the directory
for p in path_2.iterdir():
    print(p)

# Store all items inside the directory in a list
paths = [p for p in path_2.iterdir()]
print(paths)

# Store only FILES inside the directory
paths = [p for p in path_2.iterdir() if p.is_file()]
print(paths)

# Store only DIRECTORIES inside the directory
paths = [p for p in path_2.iterdir() if p.is_dir()]
print(paths)

# Find all Python files (*.py) in the directory (non‑recursive)
py_file_1 = [p for p in path_2.glob("*.py")]
print(py_file_1)

# Find all Python files (*.py) recursively in the directory and subdirectories
py_file_2 = [p for p in path_2.rglob("*.py")]
print(py_file_2)


# ==============================
# 5. FILE OPERATIONS (copy, read, write, delete)
# ==============================

# Create a Path object pointing to the source file
# This file is located inside the Modules/ecommerce directory
source = Path("Modules/ecommerce/__init__.py")

# Create a Path object for the target file
# This will create (or overwrite) __init__.py in the current working directory
target = Path() / "__init__.py"

# Copy the source file to the target location using shutil
# This copies the file content AND metadata (depending on the OS)
shutil.copy(source, target)

# Copy the file content again using pathlib (this overwrites the target file)
# read_text() reads the source file as text
# write_text() writes that text into the target file
target.write_text(source.read_text())

# -------------------------
# USEFUL FILE OPERATIONS (commented examples)
# -------------------------

# Delete the source file
# source.unlink()

# Print the file creation time in a human-readable format
# print(ctime(source.stat().st_ctime))

# Read and print the entire content of the source file
# print(source.read_text())

# Overwrite the source file with new text
# source.write_text("a = 2 + 1")

# Write binary data to the file (used for images, executables, etc.)
# source.write_bytes(b"...")


# ==============================
# 6. WORKING WITH ZIP ARCHIVES
# ==============================

# Create a new zip file in write mode ("w")
# If the file already exists, it will be overwritten
with ZipFile("files.zip", "w") as zip:

    # rglob("*.*") searches recursively for all files
    # inside the "Modules" directory (including subfolders)
    for path in Path("Modules").rglob("*.*"):

        # Add each file found into the zip archive
        zip.write(path)


# Open the existing zip file in read mode (default mode)
with ZipFile("files.zip") as zip:

    # Print the list of all file names stored in the zip file
    print(zip.namelist())

    # Get information about a specific file inside the zip
    info = zip.getinfo("Modules/ecommerce/__init__.py")

    # Print the original size of the file (before compression)
    print(info.file_size)

    # Print the compressed size of the file (after compression)
    print(info.compress_size)

    # Extract all files from the zip into the "extracte" folder
    # The folder will be created if it does not exist
    zip.extractall("extracte")


# ==============================
# 7. CSV FILE HANDLING
# ==============================

# -------------------------
# WRITING TO data_1.csv
# -------------------------

# Open the file in write mode ("w")
# If the file does not exist, it will be created
# If it exists, it will be overwritten
with open("data_1.csv", "w", newline="") as file_1:
    writer_1 = csv.writer(file_1)  # Create a CSV writer object

    # Write a single row (header)
    writer_1.writerow(["transaction_id", "product_id", "price"])

    # Write individual rows
    writer_1.writerow([1000, 12, 33])
    writer_1.writerow([1025, 52, 42])
    writer_1.writerow([1425, 12, 46])
    writer_1.writerow([1656, 11, 83])


# -------------------------
# WRITING TO data_2.csv
# -------------------------

with open("data_2.csv", "w", newline="") as file_2:
    writer_2 = csv.writer(file_2)

    # writerows() writes multiple rows at once (list of lists)
    writer_2.writerows([
        ["Name", "Email", "Phone"],          # Header row
        ["P1", "P1@email.com", "+213 ..."],
        ["P2", "P2@email.com", "+213 ..."],
        ["P3", "P3@email.com", "+213 ..."],
        ["P4", "P4@email.com", "+213 ..."]
    ])


# -------------------------
# READING data_1.csv
# -------------------------

with open("data_1.csv") as file_1:
    reader_1 = csv.reader(file_1)  # Create a CSV reader object

    # Loop through each row in the file
    for row in reader_1:
        print(row)  # Each row is returned as a list


# -------------------------
# READING data_2.csv
# -------------------------

with open("data_2.csv") as file_2:
    reader_2 = csv.reader(file_2)

    for row in reader_2:
        print(row)


# ==============================
# 8. JSON SERIALIZATION / DESERIALIZATION
# ==============================

# Create a list of dictionaries (Python objects)
movies = [
    {"id": 1, "title": "Terminator", "year": 1985},
    {"id": 2, "title": "Mr.bean", "year": 1970}
]

# Convert Python object (list) to a JSON-formatted string
data_1 = json.dumps(movies)

# Print the JSON string
print(data_1)

# Write the JSON string to a file
Path("movies.json").write_text(data_1)

# Read the JSON string back from the file
data_2 = Path("movies.json").read_text()

# Convert the JSON string back to a Python object
movies = json.loads(data_2)

# Print the full Python object (list of dictionaries)
print(movies)

# Print the first dictionary in the list
print(movies[0])

# Print the value of the "title" key from the first dictionary
print(movies[0]["title"])


# One‑liner: read JSON file and parse it directly
films = json.loads(Path("movies.json").read_text())

print(films)


# ==============================
# 9. SQLITE3 DATABASE OPERATIONS
# ==============================

# Connect to (or create) an SQLite database file
# with sqlite3.connect("DB.sqlite3") as connection:
#     # Insert each film from the previously loaded JSON data
#     command = "INSERT INTO Films VALUES(?,?,?)"
#     for film in films:
#         connection.execute(command, tuple(film.values()))
#     connection.commit()

# Query the database and fetch all results
with sqlite3.connect("DB.sqlite3") as connection:
    command = "SELECT * FROM Films"
    cursor = connection.execute(command)
    # for row in cursor:
    #     print(row)
    films_1 = cursor.fetchall()
    print(films_1)


# ==============================
# 10. MEASURING EXECUTION TIME
# ==============================

# Define a simple function named send_email
# This function simulates a task by running a loop 1000 times
def send_email():

    # Loop from 0 to 999
    # "pass" means "do nothing"
    # Used here only to simulate some processing time
    for i in range(1000):
        pass


# Store the current time BEFORE running the function
# time.time() returns the current timestamp in seconds
start = time.time()

# Call the function
send_email()

# Store the current time AFTER the function finishes
end = time.time()

# Calculate the total execution time
# (ending time - starting time)
duration_1 = end - start

# Print the execution duration in seconds
print(duration_1)


# ==============================
# 11. DATETIME OPERATIONS
# ==============================

# Create a datetime object manually
# Format: datetime(year, month, day)
dt1 = datetime(2025, 1, 1)

# Get the current date and time from the system
dt2 = datetime.now()


# Convert a STRING into a datetime object
# strptime = string parse time
# "2025/01/01" → input string
# "%Y/%m/%d" → format of the string
# %Y = full year
# %m = month
# %d = day
dt = datetime.strptime("2025/01/01", "%Y/%m/%d")

# Print the datetime object
print(dt)


# Create a datetime object from a Unix timestamp
# time.time() returns the current timestamp in seconds
# fromtimestamp() converts it into a readable datetime object
dt = datetime.fromtimestamp(time.time())

# Print the full current date and time
print(dt)

# Print only the year and month using an f-string
print(f"{dt.year}/{dt.month}")


# Convert the datetime object into a formatted STRING
# strftime = string format time
# "%Y/%m" → format output as year/month
print(dt.strftime("%Y/%m"))


# Compare two datetime objects
# Returns True if dt1 is later than dt2
# Since dt2 is the current date/time,
# this will usually print False
print(dt1 > dt2)

# ==============================
# 12. TIMEDELTA AND DATE DIFFERENCE
# ==============================


# Create a datetime object for January 1st, 2025
# Then add:
# - 1 day
# - 1000 seconds
#
# timedelta() is used to represent a duration of time
dt3 = datetime(2025, 1, 1) + timedelta(days=1, seconds=1000)

# Print the new calculated date and time
print(dt3)


# Get the current date and time from the system
dt4 = datetime.now()

# Print the current datetime
print(dt4)


# Subtract two datetime objects
# Result = timedelta object (difference between dates)
duration_2 = dt4 - dt3

# Print the full duration difference
# Example: 120 days, 5:30:10
print(duration_2)


# Print ONLY the number of days in the duration
print("days", duration_2.days)

# Print ONLY the remaining seconds
# (seconds left after removing full days)
print("seconds", duration_2.seconds)

# Print the TOTAL duration in seconds
# Includes days + hours + minutes + seconds
print("total_seconds", duration_2.total_seconds())

# ==============================
# 13. RANDOM MODULE OPERATIONS
# ==============================


# Generate a random floating-point number
# Range: 0.0 <= number < 1.0
print(random.random())


# Generate a random INTEGER between 1 and 10
# Both 1 and 10 are INCLUDED
print(random.randint(1, 10))


# Select ONE random element from a list
print(random.choice([1, 2, 3, 4]))


# Select MULTIPLE random elements from a list
# k=2 means choose 2 elements
# choices() allows repeated values
print(random.choices([1, 2, 3, 4], k=2))


# Generate a random string of 4 characters
#
# string.ascii_letters → all uppercase and lowercase letters
# string.digits → numbers from 0 to 9
#
# random.choices(..., k=4)
# selects 4 random characters
#
# "".join(...)
# joins the characters into a single string
print("".join(random.choices(
    string.ascii_letters + string.digits,
    k=4
)))


# Create a list of numbers
numbers = [1, 2, 3, 4]

# Shuffle the list randomly (modifies the original list)
random.shuffle(numbers)

# Print the shuffled list
print(numbers)

# ==============================
# 14. OPENING A WEBSITE WITH WEBBROWSER
# ==============================


# Print a deployment success message
print("Deployment completed")


# Open the Google website in the default browser
#
# webbrowser.open(url)
# - url → the website address to open
#
# When executed, the browser will automatically launch
# and navigate to the specified URL
# webbrowser.open("http://google.com")

# ==============================
# 15. SENDING EMAILS WITH PYTHON
# ==============================


# Create a multipart email object
# This allows the email to contain:
# - text
# - images
# - files
message = MIMEMultipart()


# Set the sender name/email
message["from"] = "Fechetah Makhlouf"

# Set the receiver email address
message["to"] = "email@gmail.com"

# Set the email subject
message["subject"] = "this is a test"


# Attach a text body to the email
message.attach(MIMEText("Body"))


# Read an image file as binary data
# then attach it to the email
# message.attach(
# MIMEImage(
# Path("test.jpg").read_bytes()
# )
# )


# Create a connection to Gmail's SMTP server
#
# host="smtp.gmail.com"
# → Gmail SMTP server
#
# port=587
# → Port used for TLS encryption
with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:

    # Identify ourselves to the SMTP server
    smtp.ehlo()

    # Start TLS encryption for secure communication
    smtp.starttls()

    # Login to the Gmail account
    #
    # Replace:
    # - email@gmail.com
    # - PassWord
    #
    # with real credentials
    # smtp.login("email@gmail.com", "PassWord")

    # Send the email message
    # smtp.send_message(message)

    # Print confirmation message
    print("sent...")
