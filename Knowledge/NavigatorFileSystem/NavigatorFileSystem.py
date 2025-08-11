import os
from datetime import datetime

def display_cwd():
    cwd = os.getcwd()
    print(f"Current working directory is: {cwd}")

def up_one_directory_level():
    os.chdir("../")

def up_two_directory_level():
    os.chdir("../")
    os.chdir("../")

def format_datetime(timestamp):
    utc_timestamp = datetime.utcfromtimestamp(timestamp)
    formatted_date = utc_timestamp.strftime("%d/%m/%Y %H:%M:%S")
    return formatted_date

def display_entries_in_directory(directory) -> None:
    entries = os.scandir(directory)
    for entry in entries:
        info = entry.stat()
        print(f'{entry.name} Creation date: {format_datetime(info.st_birthtime)}')
        print(f'{entry.name} Access date: {format_datetime(info.st_atime)}')
        print(f'{entry.name} Size: {info.st_size}')

def display_directories(directory):
    entries = os.scandir(directory)
    for entry in entries:
        if entry.is_dir():
            print(f"Directory Name: {entry.name}")

def display_files(directory):
    entries = os.scandir(directory)
    for entry in entries:
        if entry.is_file():
            print(f"File Name: {entry.name}")
# def display_entries_in_directory_using_list(directory):
#         for entry in os.listdir(directory):
#             print(entry)
display_cwd()
os.chdir("./")
display_cwd()
display_entries_in_directory("./")
display_directories("./")
display_files("./")