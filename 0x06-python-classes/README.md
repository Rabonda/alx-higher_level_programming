# 0x06. Python - Classes and Objects
Tasks
-----
### 0. My first square

Write an empty class Square that defines
-  You are not allowed to import any module
```
guillaume@ubuntu:~/0x06$ cat 0-main.py
#!/usr/bin/python3
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)

guillaume@ubuntu:~/0x06$ ./0-main.py
<class '0-square.Square'>
{}
guillaume@ubuntu:~/0x06$
```
Repo:
-----
- GitHub repository: alx-higher_level_programming
- Directory: 0x06-python-classes
- File: 0-square.py
