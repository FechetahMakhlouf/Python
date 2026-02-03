# Import Path class to work with filesystem paths in a clean, object-oriented way
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

# Print only the file name (with extension)
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

# 4
