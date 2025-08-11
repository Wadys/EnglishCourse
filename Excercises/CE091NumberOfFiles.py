# Number of Files in Current Directory
# Implement a python program which counts number of files in current directory.

# Hint : Use OS Module
import os
entries = os.scandir('.')
count = 0
for entry in entries:
    if os.path.isfile(entry):
        count += 1
print(count)
