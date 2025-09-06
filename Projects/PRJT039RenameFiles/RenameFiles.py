## Instruction

# Implement a Python function which takes three parameters - file name, new 
# name and file type. If the file exists in the directory it renames it to the 
# new name, otherwise prints message the file does not exist. If we pass All 
# as a file name, it renames all file names using sequence. filename1, filename2....

import pathlib

# TODO 1 - Rename one file name
def rename_file(file_name, new_name, file_type):
    directory = pathlib.Path.cwd()
    seq_num = 0
    for item in directory.iterdir():
        if item.is_file() and item.suffix == file_type:
            if item.stem == file_name:
                update_name = new_name + file_type
                item.rename(update_name)
                print(f"File name was successfully changed from {file_name+file_type} to {update_name}")
                return
            elif file_name == "All":
                update_name = new_name+str(seq_num) + file_type
                item.rename(update_name)
                seq_num+=1
                print(f"File name was successfully changed from {item.name} to {update_name}")
    if file_name != "All":
        print(f"The file {file_name+file_type} does not exist!")
#- If exists rename it do new name

    
# TODO 2 - Rename all files' names
#     - Create sequence 
#     - Create new name based on sequence
#     - Update file name
#     - Increase sequence

rename_file("All","sample",".txt")
