import os, glob, shutil

# This is an older way using glob, os and shutil to move a file to a new directory
for file_name in glob.glob("*.txt"):
    new_path = os.path.join("archive", file_name)
    shutil.move(file_name, new_path)
