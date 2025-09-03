# Find Last Modified

## Instruction

Implement a Python function which takes a string path as a parameter and return the last modified file or folder in the given path.


### Example Input 
```
directory = pathlib.Path.cwd()
find_last_modified(directory)
```
### Example Output 

```
Date modified: 2022-02-18 06:48:00.781468, Filename: main.py
```


# Hint

- Use pathlib module.
- Use datetime.fromtimestamp for converting to the date


# Solution

[https://replit.com/@AppMillers/Find-Last-Modified-Solution](https://replit.com/@AppMillers/Find-Last-Modified-Solution)