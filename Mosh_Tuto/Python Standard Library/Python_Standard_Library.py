# Import Path class to work with filesystem paths in a clean, object-oriented way
import shutil
from time import ctime
from pathlib import Path

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


# Create a Path object pointing to a directory named "Modules"
path_2 = Path("Modules")

# Create the directory (uncomment to use)
# path_2.mkdir()

# Remove the directory (must be empty) (uncomment to use)
# path_2.rmdir()

# Rename the directory (uncomment to use)
# path_2.rename("ecommerce2")

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

# Find all Python files (*.py) in the directory (non-recursive)
py_file_1 = [p for p in path_2.glob("*.py")]
print(py_file_1)

# Find all Python files (*.py) recursively in the directory and subdirectories
py_file_2 = [p for p in path_2.rglob("*.py")]
print(py_file_2)


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

# 5