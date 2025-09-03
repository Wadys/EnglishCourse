from pathlib import Path
# These are all commands in the pathlib library
path_test = Path.cwd() / "archive" / "test.txt"
print(f"File name: {path_test.name}")
print(f"File directory: {path_test.parent}")
print(f"Parent file directory: {path_test.parent.parent}")
print(f"File name without extension: {path_test.stem}")
print(f"File extension: {path_test.suffix}")

def display_directory_contents():
    entries = Path.cwd()
    for entry in entries.iterdir():
        print(f"File name: {entry.name}")
        print(f"File folder: {entry.parent}")
        print(f"File name without extension: {entry.stem}")
        print(f"File extension: {entry.suffix}")
        print()
display_directory_contents()

path = Path.cwd()
# Here we print all the files that have a .py extension
file_names = path.glob("*.py")
for file_name in file_names:
    print(f"File name: {file_name.name}")

print()
# Here we print all the files that have a .txt extension
file_names = path.glob("*.txt")
for file_name in file_names:
    print(f"File name: {file_name.name}")

print()
# These lines print all text files in parent directory
file_names = path.glob("**/*.txt")
for file_name in file_names:
    print(file_name.stem)
    print(file_name.parent)

print()
# These lines do the same as the file before but uses the rglob method
file_names = path.rglob("*.txt")
for file_name in file_names:
    print(file_name.stem)
    print(file_name.parent)