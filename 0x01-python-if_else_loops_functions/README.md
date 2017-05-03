## 0x01. Python - if/else, loops, functions

0-positive_or_negative.py - Prints a random number between -10 and 10
```
jarehec@ubuntu:~/0x01$ ./0-positive_or_negative.py
-4 is negative
jarehec@ubuntu:~/0x01$ ./0-positive_or_negative.py
0 is zero
```
1-last_digit.py - Prints the last digit of a random number
```
jarehec@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 4205 is 5 and is less than 6 and not 0
jarehec@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -626 is -6 and is less than 6 and not 0
jarehec@ubuntu:~/0x01$ ./1-last_digit.py
```
2-print_alphabet.py - Prints the alphabet without a newline
```
jarehec@ubuntu:~/0x01$ ./2-print_alphabet.py
abcdefghijklmnopqrstuvwxyzjarehec@ubuntu:~/0x01$
```
3-print_alphabt.py - Prints the alphabet without 'q' and 'e'
```
jarehec@ubuntu:~/0x01$ ./3-print_alphabt.py
abcdfghijklmnoprstuvwxyzjarehec@ubuntu:~/0x01$
```
4-print_hexa.py - Prints all numbers from 0 to 98 in decimal and in hexadecimal
```
jarehec@ubuntu:~/0x01$ ./4-print_hexa.py
0 = 0x0
1 = 0x1
...
97 = 0x61
98 = 0x62
jarehec@ubuntu:~/0x01$
```
5-print_comb2.py - Prints numbers from 00 to 99
```
jarehec@ubuntu:~/0x01$ ./5-print_comb2.py
00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99
jarehec@ubuntu:~/0x01$
```
6-print_comb3.py - Prints all possible different combinations of two digits
```
jarehec@ubuntu:~/0x01$ ./6-print_comb3.py
01, 02, 03, 04, 05, 06, 07, 08, 09, 12, 13, 14, 15, 16, 17, 18, 19, 23, 24, 25, 26, 27, 28, 29, 34, 35, 36, 37, 38, 39, 45, 46, 47, 48, 49, 56, 57, 58, 59, 67, 68, 69, 78, 79, 89
jarehec@ubuntu:~/0x01$
```
7-islower.py - Function that checks for lowercase character
```
jarehec@ubuntu:~/0x01$ cat 7-main.py
#!/usr/bin/env python3
islower = __import__('7-islower').islower

print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else "upper"))

jarehec@ubuntu:~/0x01$ ./7-main.py
a is lower
H is upper
jarehec@ubuntu:~/0x01$
```
8-uppercase.py - Function that print a string in uppercase followed by a new line.
```
jarehec@ubuntu:~/0x01$ cat 8-main.py
#!/usr/bin/env python3
uppercase = __import__('8-uppercase').uppercase

uppercase("hello")

jarehec@ubuntu:~/0x01$ ./8-main.py
HELLO
jarehec@ubuntu:~/0x01$
```
9-print_last_digit.py - Function that prints the last digit of a number
```
jarehec@ubuntu:~/0x01$ cat 9-main.py
#!/usr/bin/env python3
print_last_digit = __import__('9-print_last_digit').print_last_digit

print_last_digit(98)
r = print_last_digit(-1024)
print(r)

jarehec@ubuntu:~/0x01$ ./9-main.py
844
jarehec@ubuntu:~/0x01$
```
10-add.py - Function that adds two integers and returns the result
```
jarehec@ubuntu:~/0x01$ cat 10-main.py
#!/usr/bin/env python3
add = __import__('10-add').add

print(add(1, 2))

jarehec@ubuntu:~/0x01$ ./10-main.py
3
jarehec@ubuntu:~/0x01$
```
11-pow.py - Function that computes a to the power of b and return the value
```
jarehec@ubuntu:~/0x01$ cat 11-main.py
#!/usr/bin/env python3
pow = __import__('11-pow').pow

print(pow(2, 2))
print(pow(-4, 5))

jarehec@ubuntu:~/0x01$ ./11-main.py
4
-1024
jarehec@ubuntu:~/0x01$
```
12-fizzbuzz.py - Function that prints FizzBuzz from 1-100
```
jarehec@ubuntu:~/0x01$ cat 12-main.py
#!/usr/bin/env python3
fizzbuzz = __import__('12-fizzbuzz').fizzbuzz

fizzbuzz()
print("")

jarehec@ubuntu:~/0x01$ ./12-main.py | cat -e
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 FizzBuzz 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 56 Fizz 58 59 FizzBuzz 61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 FizzBuzz 76 77 Fizz 79 Buzz Fizz 82 83 Fizz Buzz 86 Fizz 88 89 FizzBuzz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz Buzz $
jarehec@ubuntu:~/0x01$
```
100-print_tebahpla.py - Prints the alphabet in reverse orde alternating lowercase and uppercase
```
jarehec@ubuntu:~/0x01$ ./100-print_tebahpla.py
zYxWvUtSrQpOnMlKjIhGfEdCbAjarehec@ubuntu:~/0x01$
```
101-remove_char_at.py - Function that creates a copy of the string, removing the character at the position n
```
jarehec@ubuntu:~/0x01$ cat 101-main.py
#!/usr/bin/env python3
remove_char_at = __import__('101-remove_char_at').remove_char_at

print(remove_char_at("Chicago", 2))
print(remove_char_at("C is fun!", 0))

jarehec@ubuntu:~/0x01$ ./101-main.py
Chcago
 is fun!
jarehec@ubuntu:~/0x01$
```
