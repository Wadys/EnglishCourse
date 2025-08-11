import os

path = os.path.join("folder1", "folder2", "folder3", "logo.png")
print(path)
print(os.sep) #Prints a backlash(/)
print(os.getcwd()) #Prints the current path the file is located at
abs_path = os.path.abspath("OSModule.py")
print(abs_path) #Prints the absolute path for the specified file
abs_path = os.path.abspath("../")
print(abs_path) #Prints the absolute path for the parent directory
abs_path = os.path.abspath("OSModule.py")
print(os.path.isabs("OSModule.py")) #Prints false because it's not an absolute path
print(os.path.isabs("C://Users//wadyp//OneDrive//Documents//Python//EnglishCourse//Knowledge//OSModule.py"))
#Prints true because it's not an absolute path
rel_path = os.path.relpath("C://Users//wadyp//OneDrive//Documents//Python//EnglishCourse//Knowledge//NavigateFileSystem//OSModule.py", "C://Users//wadyp" )
print(rel_path) #Prints the relative path removing the second portion(C://Users//wadyp//)
rel_path = os.path.relpath("C://Users//wadyp//OneDrive//Documents//Python//EnglishCourse//Knowledge//NavigateFileSystem//OSModule.py", "OSModule.py" )
print(rel_path) #Prints the current folder
rel_path = os.path.relpath("C://Users//wadyp//OneDrive//Documents//Python//EnglishCourse//Knowledge//NavigateFileSystem//OSModule.py", "NavigateFileSystem//OSModule.py" )
print(rel_path) #Prints the relative path
directory_name = os.path.dirname("C://Users//wadyp//OneDrive//Documents//Python//EnglishCourse//Knowledge//OSModule.py")
print(directory_name)#Prints the directory omitting the file portion of it
filename = os.path.basename("C://Users//wadyp//OneDrive//Documents//Python//EnglishCourse//Knowledge//OSModule.py")
print(filename)#Prints the last element or base of the path provided
print(f"Path Exists? {os.path.exists("C://Users//wadyp//OneDrive//Documents//Python//EnglishCourse//Knowledge//OSModule.py")}")
#Prints False because path doesn't exist
print(f"Path Exists? {os.path.exists("C:/Users/wadyp/OneDrive/Documents/Python/EnglishCourse/Knowledge/NavigatorFileSystem")}")
#Prints True because path does exist
print(f"Is this a directory? {os.path.isdir("C:/Users/wadyp/OneDrive/Documents/Python/EnglishCourse/Knowledge/NavigateFileSystem/OSModule.py")}")
#Prints false because path is for a file
print(f"Is this a directory? {os.path.isdir("C:/Users/wadyp/OneDrive/Documents/Python/EnglishCourse/Knowledge/NavigatorFileSystem")}")
#Prints true because path is for a folder
print(os.getcwd())
print(os.path.getsize("C:/Users/wadyp/OneDrive/Documents/Python/EnglishCourse/Knowledge/NavigatorFileSystem")) 
#Prints folder size
print(os.path.getsize("C:/Users/wadyp/OneDrive/Documents/Python/EnglishCourse/Knowledge/NavigatorFileSystem/OSModule.py"))
#Prints file size