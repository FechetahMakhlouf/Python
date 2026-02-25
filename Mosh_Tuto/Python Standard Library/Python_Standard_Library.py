# ==============================
# 1. IMPORTS
# ==============================
import sqlite3
from pathlib import Path          # For object-oriented filesystem paths
import json                        # For JSON serialization/deserialization
import json                        # Duplicate import – kept as per instruction
import csv                         # For reading/writing CSV files
import csv                         # Duplicate import – kept as per instruction
from zipfile import ZipFile        # For creating/reading zip archives
# For high-level file operations (copy, move, etc.)
import shutil
from time import ctime              # For human-readable timestamps
from pathlib import Path            # Duplicate import – kept as per instruction


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
with sqlite3.connect("DB.sqlite3") as connection:
    # Insert each film from the previously loaded JSON data
    command = "INSERT INTO Films VALUES(?,?,?)"
    for film in films:
        connection.execute(command, tuple(film.values()))
    connection.commit()

# Query the database and fetch all results
with sqlite3.connect("DB.sqlite3") as connection:
    command = "SELECT * FROM Films"
    cursor = connection.execute(command)
    # for row in cursor:
    #     print(row)
    films_1 = cursor.fetchall()
    print(films_1)


# 9
