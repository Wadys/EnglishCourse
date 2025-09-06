# Rename Files
## Instruction

Implement a Python function which takes three parameters - file name, new name and file type. If the file exists in the directory it renames it to the new name, otherwise prints message the file does not exist. If we pass All as a file name, it renames all file names using sequence. filename1, filename2....


TODOs:
```
TODO 1 - Rename one file name
    - Get current directory
    - List all files
    - Condition for onlye files and selected types
    - Check if the file exists in cwd
    - If exists rename it do new name

    
TODO 2 - Rename all files' names
    - Create sequence 
    - Create new name based on sequence
    - Update file name
    - Increase sequence


```


### Example Input 1
```
rename_file('test1', 'test3', '.txt')
```

### Example Output 1

```
File name is successfully changed from test1.txt to test3.txt
```

### Example Input 2
```
rename_file('All', 'test', '.txt')
```

### Example Output 2

```
File name is successfully changed from file2.txt to test0.txt
File name is successfully changed from file1.txt to test1.txt
```



# Solution

[https://replit.com/@AppMillers/Project-39-Rename-Files-Solution](https://replit.com/@AppMillers/Project-39-Rename-Files-Solution)