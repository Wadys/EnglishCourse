import os
def top_down_walk():
    """Recursive run through folders printing: 
    subfolders and files names. From Top to Bottom"""
    print(os.walk("../.."))
    for dirpath, dirnames, files in os.walk('C:/Users/wadyp/OneDrive/Documents/Python/EnglishCourse/Knowledge'):
        print("Directory: ",dirpath)
        print("----Includes these directories----")
        for dirname in dirnames:
            print(dirname)
        print("----Includes these files----")
        for file in files:
            print(file)
        print()

def down_top_walk():
    """Recursive run through folders printing: 
    subfolders and files names. From Bottom to Top"""
    for dirpath, dirnames, files in os.walk('../Files', topdown=False):
        print("Directory: ",dirpath)
        print("----Includes these directories----")
        for dirname in dirnames:
            print(dirname)
        print("----Includes these files----")
        for file in files:
            print(file)
        print()
top_down_walk()
down_top_walk()