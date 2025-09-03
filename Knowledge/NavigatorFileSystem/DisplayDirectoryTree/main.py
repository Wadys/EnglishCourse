# # Display a Directory Tree
# ## Instruction
# Implement a Python function which displays all files and folders
# from current direcroty in TREE (hierarchical) format.
#Input:
# display_tree()
 #Output:
#/Users/elshad/Desktop/Python For Everyone/Projects/DisplayTreeDirectory
#     + .idea
#         + .gitignore
#         + DisplayTreeDirectory.iml
#         + inspectionProfiles
#             + profiles_settings.xml
#         + misc.xml
#         + modules.xml
#         + workspace.xml
#     + main.py
#     + venv
#         + .gitignore
#         + bin
#             + activate
#             + activate.csh

from pathlib import Path

def display_tree():
    directory =Path().cwd()
    print(f"{directory}"  )
    entries = sorted(directory.rglob("*"))
    for entry in entries:
        depth = len(entry.relative_to(directory).parts)
        spacer = "    " * depth
        print(f"{spacer}+ {entry.name}")

display_tree()
