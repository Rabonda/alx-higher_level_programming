# 0x08. Python - More Classes and Objects
Tasks
-----
### 0. Simple rectangle

Write an empty class Rectangle that defines

- You are not allowed to import any module

```
guillaume@ubuntu:~/0x08$ cat 0-main.py
#!/usr/bin/python3
Rectangle = __import__('0-rectangle').Rectangle

my_rectangle = Rectangle()
print(type(my_rectangle))
print(my_rectangle.__dict__)

guillaume@ubuntu:~/0x08$ ./0-main.py
<class '0-rectangle.Rectangle'>
{}
guillaume@ubuntu:~/0x08$
```
Repo:
-----
- GitHub repository: alx-higher_level_programming
- Directory: 0x08-python-more_classes
- File: 0-rectangle.py
