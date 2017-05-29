# 0x03. Python - Data Structures: Lists, Tuples

## 0-print_list_integer.py
### Function that prints all integers if a list
<p>Prototype: def print_list_integer(my_list=[]):</p>
<p>Format: one integer per line. See below</p>

```
>>> print_list_integer = __import__('0-print_list_integer').print_list_integer
>>> my_list = [1, 2, 3]
>>> print_list_integer(my_list)
1
2
3
```

## 1-element_at.py
### Function that retrieves an element from a list
<p>Prototype: def element_at(my_list, idx):</p>
<p>If idx is out of range, the function should return None</p>

```
>>> element_at = __import__('1-element_at').element_at
>>> my_list = [1, 2, 3]
>>> idx = 1
>>> print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
Element at index 1 is 2
```

## 2-replace_in_list.py
### Function that replaces an element of a list at a specific position
<p>Prototype: def replace_in_list(my_list, idx, element):</p>
<p>If idx is out of range, the function should not modify anything, and returns the original list</p>

```
>>> replace_in_list = __import__('2-replace_in_list').replace_in_list
>>> my_list = [1, 2, 3, 4, 5]
>>> idx = 3
>>> new_element = 9
>>> new_list = replace_in_list(my_list, idx, new_element)
>>> print(new_list)
[1, 2, 3, 9, 5]
>>> print(my_list)
[1, 2, 3, 9, 5]
```

## 3-print_reversed_list_integer.py
### Function that prints all integers if a list, in reverse order
<p>Prototype: def print_reversed_list_integer(my_list=[]):</p>
<p>Format: one integer per line. See below</p>

```
>>> print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer

>>> my_list = [1, 2, 3, 4, 5]
>>> print_reversed_list_integer(my_list)
5
4
3
2
1
```

## 4-new_in_list.py
### Function that replaces an element in a list at a specific position without modifying the original list
<p>Prototype: def print_list_integer(my_list=[]):</p>
<p>Format: one integer per line. See below</p>

```
>>> my_list = [1, 2, 3]
>>> print_list_integer(my_list)
1
2
3
```

## 5-no_c.py
### Function that removes all characters c and C from a string
<p>Prototype: def no_c(my_string):</p>
<p>The function shoud return the new string</p>

```
>>> no_c = __import__('5-no_c').no_c
>>> print(no_c("Holberton School"))
Holberton Shool
>>> print(no_c("Chicago"))
hiago
>>> print(no_c("C is fun!"))
 is fun!
```

## 6-print_list_integer.py
### Function that prints a matrix of integers 
<p>Prototype: def print_matrix_integer(matrix=[[]]):</p>
<p>Format: See below</p>

```
>>> print_matrix_integer = __import__('6-print_matrix_integer').print_matrix_integer
>>> matrix = [
...    [1, 2, 3],
...    [4, 5, 6],
...    [7, 8, 9]
... ]
>>> print_matrix_integer(matrix)
1 2 3
4 5 6
7 8 9
>>> print("--")
--
>>> print_matrix_integer()

```

## 7-add_tuple.py
### Function that adds 2 tuples
<p>Prototype: def add_tuple(tuple_a=(), tuple_b=()):</p>
<p>Returns a tuple with 2 integers:</p>

```
>>> add_tuple = __import__('7-add_tuple').add_tuple
>>> tuple_a = (1, 89)
>>> tuple_b = (88, 11)
>>> new_tuple = add_tuple(tuple_a, tuple_b)
>>> print(new_tuple)
(89, 100)
>>> print(add_tuple(tuple_a, (1, )))
(2, 89)
>>> print(add_tuple(tuple_a, ()))
(1, 89)
```

## 8-multiple_returns.py
### Function that returns a tuple with the length of a string and its first character
<p>Prototype: def multiple_returns(sentence):</p>
<p>If the sentence is empty, the first character should be equal to None</p>

```
>>> multiple_returns = __import__('8-multiple_returns').multiple_returns
>>> sentence = "At Holberton school, I learnt C!"
>>> length, first = multiple_returns(sentence)
>>> print("Length: {:d} - First character: {}".format(length, first))
Length: 32 - First character: A
```

## 9-max_integer.py
### Function that finds the biggest integer of a list
<p>Prototype: def max_integer(my_list=[]):</p>
<p>If the list is empty, returns None:</p>

```
>>> max_integer = __import__('9-max_integer').max_integer
>>> my_list = [1, 90, 2, 13, 34, 5, -13, 3]
>>> max_value = max_integer(my_list)
>>> print("Max: {}".format(max_value))
Max: 90
```

## 10-divisible_by_2.py
### Function that finds all multiples of 2 in a list
<p>Prototype: def divisible_by_2(my_list=[]):</p>
<p>Return a new list with True or False, depending on wether the integer at the same position in the original list is a multiple of 2</p>

```
>>> divisible_by_2 = __import__('10-divisible_by_2').divisible_by_2

>>> my_list = [0, 1, 2, 3, 4]
>>> list_result = divisible_by_2(my_list)

>>> i = 0
>>> while i < len(list_result):
...    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
...    i += 1
0 is divisible by 2
1 is not divisible by 2
2 is divisible by 2
3 is not divisible by 2
4 is divisible by 2
```

## 11-delete_at.py
### Function that deletes the item at a specific position in a list 
<p>Prototype: def delete_at(my_list=[], idx=0):</p>

```
>>> delete_at = __import__('11-delete_at').delete_at

>>> my_list = [1, 2, 3, 4, 5]
>>> idx = 3
>>> new_list = delete_at(my_list, idx)
>>> print(new_list)
[1, 2, 3, 5]
>>> print(my_list)
[1, 2, 3, 5]
```

## 12-switch.py
### Switches the value of 2 variables
