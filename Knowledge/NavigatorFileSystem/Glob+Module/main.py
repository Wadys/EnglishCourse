import glob

def display_png():
    pngfile = glob.glob("*.png")
    print(pngfile)

def display_flowchart():
    flowchart_file = glob.glob("*flowchart*")
    print(flowchart_file)

def display_flowchart_subdir():
    flowchart_file = glob.iglob("**/*flowchart*", recursive=True)
    for file in flowchart_file:
        print(file)


# display_flowchart()
# display_png()
display_flowchart_subdir()