## 0x00. Python - Hello, World

0-run - Shell script that runs a Python script
```
guillaume@ubuntu:~/py/0x00$ cat main.py
#!/usr/bin/python3
print("Holberton School")
guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
guillaume@ubuntu:~/py/0x00$ ./0-run
Holberton School
guillaume@ubuntu:~/py/0x00$
```
1-run_inline - Shell script that runs Python code
```
guillaume@ubuntu:~/py/0x00$ export PYCODE='print("Hello, World: {}".format(88+10))'
guillaume@ubuntu:~/py/0x00$ ./1-run_inline
Hello, World: 98
guillaume@ubuntu:~/py/0x00$
```
2-print.py - Python script that prints "Programming is like building a multilingual puzzle
```
guillaume@ubuntu:~/py/0x00$ ./2-print.py
"Programming is like building a multilingual puzzle
guillaume@ubuntu:~/py/0x00$
```
3-print_number.py - Prints a number
```
guillaume@ubuntu:~/py/0x00$ ./3-print_number.py
98 Battery street
guillaume@ubuntu:~/py/0x00$
```
4-print_float.py Prints a float
```
guillaume@ubuntu:~/py/0x00$ ./4-print_float.py
Float: 3.14
guillaume@ubuntu:~/py/0x00$
```
5-print_string.py Prints a string
```
guillaume@ubuntu:~/py/0x00$ ./5-print_string.py 
Holberton SchoolHolberton SchoolHolberton School
Holberton
guillaume@ubuntu:~/py/0x00$
```
6-concat.py - Prints "Welcome to Holberton School!"
```
guillaume@ubuntu:~/py/0x00$ ./6-concat.py
Welcome to Holberton School!
guillaume@ubuntu:~/py/0x00$ wc -l 6-concat.py
5 6-concat.py
guillaume@ubuntu:~/py/0x00$
```
7-edges.py - solution for https://github.com/holbertonschool/0x00.py/blob/master/7-edges.py
```
guillaume@ubuntu:~/py/0x00$ ./7-edges.py
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
guillaume@ubuntu:~/py/0x00$ wc -l 7-edges.py
8 7-edges.py
guillaume@ubuntu:~/py/0x00$
```
8-concat_edges.py - Prints "object-oriented programming with Python"	
```
guillaume@ubuntu:~/py/0x00$ ./8-concat_edges.py
object-oriented programming with Python
guillaume@ubuntu:~/py/0x00$ wc -l 8-concat_edges.py
5 8-concat_edges.py
guillaume@ubuntu:~/py/0x00$
```
9-easter_egg.py - Prints "The Zen of Python", by  Tim Peters
```
guillaume@ubuntu:~/py/0x00$ ./9-easter_egg.py
```'
100-write - Prints "and that piece of art is useful - Dora Korpar, 2015-10-19" to stderr using write
guillaume@ubuntu:~/py/0x00$ ./100-write.py
and that piece of art is useful - Dora Korpar, 2015-10-19
guillaume@ubuntu:~/py/0x00$ echo $?
1
guillaume@ubuntu:~/py/0x00$ ./100-write.py 2> q
guillaume@ubuntu:~/py/0x00$ cat q
and that piece of art is useful - Dora Korpar, 2015-10-19
guillaume@ubuntu:~/py/0x00$
```
