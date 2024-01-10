# 0x02. Python - import & modules
Tasks
-----
### 0\. Import a simple function from a simple file
Write a program that imports the function def add(a, b): from the file add_0.py and prints the result of the addition 1 + 2 = 3

- You have to use print function with string format to display integers
- You have to assign:
  - the value 1 to a variable called a
  - the value 2 to a variable called b
  - and use those two variables as arguments when calling the functions add and print
- a and b must be defined in 2 different lines: a = 1 and another b = 2
- Your program should print: <a value> + <b value> = <add(a, b) value> followed with a new line
- You can only use the word add_0 once in your code
- You are not allowed to use * for importing or __import__
- Your code should not be executed when imported - by using __import__, like the example below

```
guillaume@ubuntu:~/0x03$ cat 0-main.py
#!/usr/bin/python3
print_list_integer = __import__('0-print_list_integer').print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)

guillaume@ubuntu:~/0x03$ ./0-main.py
1
2
3
4
5
guillaume@ubuntu:~/0x03$ 

```
Repo:
-----
- GitHub repository: alx-higher_level_programming
- Directory: 0x02-python-import_modules
- File: 0-add.py
