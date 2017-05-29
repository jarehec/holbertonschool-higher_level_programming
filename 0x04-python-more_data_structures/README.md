# 0x04. Python - More Data Structures: Set, Dictionary

## 0-square_matrix_simple.py
### Function that computes the square value of all integers of a matrix
<p>Prototype: def square_matrix_simple(matrix=[]):</p>
<p>matrix is a 2 dimensional array</p>
<p>Returns a new matrix with each value of the matrix squared</p>

```
>>> square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

>>> matrix = [
...    [1, 2, 3],
...    [4, 5, 6],
...    [7, 8, 9]
... ]
>>> new_matrix = square_matrix_simple(matrix)
>>> print(new_matrix)
[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
>>> print(matrix)
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

## 1-search_replace.py
### Function that replaces all occurrences of an element by another in a new list
<p>Prototype: def search_replace(my_list, search, replace):</p>
<p>list is the initial list</p>
<p>search is the element to replace in the list</p>
<p>replace is the new element</p>

```
>>> search_replace = __import__('1-search_replace').search_replace

>>> my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
>>> new_list = search_replace(my_list, 2, 89)
>>> print(new_list)
[1, 89, 3, 4, 5, 4, 89, 1, 1, 4, 89]
>>> print(my_list)
[1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
```

## 2-uniq_add.py
### Function that makes the addition of all unique integers in a list
<p>Prototype: def uniq_add(my_list=[]):</p>

```
>>> uniq_add = __import__('2-uniq_add').uniq_add

>>> my_list = [1, 2, 3, 1, 4, 2, 5]
>>> result = uniq_add(my_list)
>>> print("Result: {:d}".format(result))
Result: 15
```

## 3-common_elements.py
### Function that returns a set of common elements in two sets
<p>Prototype: def common_elements(set_1, set_2):</p>

```
>>> common_elements = __import__('3-common_elements').common_elements

>>> set_1 = { "Python", "C", "Javascript" }
>>> set_2 = { "Bash", "C", "Ruby", "Perl" }
>>> c_set = common_elements(set_1, set_2)
>>> print(sorted(list(c_set)))
['C']
```

## 4-only_diff_elements.py
### Function that returns a set of all elements present in only one set
<p>Prototype: def only_diff_elements(set_1, set_2):</p>

```
>>> only_diff_elements = __import__('4-only_diff_elements').only_diff_elements

>>> set_1 = { "Python", "C", "Javascript" }
>>> set_2 = { "Bash", "C", "Ruby", "Perl" }
>>> od_set = only_diff_elements(set_1, set_2)
>>> print(sorted(list(od_set)))
['Bash', 'Javascript', 'Perl', 'Python', 'Ruby']
```

## 5-number_keys.py
### Function that returns the number of keys in a dictionary
<p>Prototype: def number_keys(my_dict):</p>

```
>>> number_keys = __import__('5-number_keys').number_keys

>>> my_dict = { 'language': "C", 'number': 13, 'track': "Low level" }
>>> nb_keys = number_keys(my_dict)
>>> print("Number of keys: {:d}".format(nb_keys))
Number of keys: 3
```

## 6-print_sorted_dictionary.py
### Function that prints a dictionary by ordered keys
<p>Prototype: def print_sorted_dictionary(my_dict):</p>
<p>All keys are string</p>
<p>Dictionary values can have any type</p>

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
### Function that replaces or adds key/value in a dictionary
<p>Prototype: def update_dictionary(my_dict, key, value):</p>
<p>key argument will be always a string</p>
<p>value argument will be any type</p>

```
>>> update_dictionary = __import__('7-update_dictionary').update_dictionary
>>> print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

>>> my_dict = { 'language': "C", 'number': 89, 'track': "Low level" }
>>> new_dict = update_dictionary(my_dict, 'language', "Python")
>>> print_sorted_dictionary(new_dict)
language: Python
number: 89
track: Low level
>>> print_sorted_dictionary(my_dict)
language: Python
number: 89
track: Low level
```

## 8-simple_delete.py
### Function that deletes a key in a dictionary
<p>Prototype: def simple_delete(my_dict, key=""):</p>
<p>key argument will be always a string</p>
<p>If a key doesn't exist, the dictionary won't change</p>

```
>>> simple_delete = __import__('8-simple_delete').simple_delete
>>> print_sorted_dictionary =  __import__('6-print_sorted_dictionary').print_sorted_dictionary

>>> my_dict = { 'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3] }
>>> new_dict = simple_delete(my_dict, 'track')
>>> print_sorted_dictionary(my_dict)
Number: 89
ids: [1, 2, 3]
language: C
>>> print_sorted_dictionary(new_dict)
Number: 89
ids: [1, 2, 3]
language: C
>>> new_dict = simple_delete(my_dict, 'c_is_fun')
>>> print_sorted_dictionary(my_dict)
Number: 89
ids: [1, 2, 3]
language: C
>>> print_sorted_dictionary(new_dict)
Number: 89
ids: [1, 2, 3]
language: C
```

## 9-multiply_by_2.py
### Function that returns a new dictionary with all values multiplied by 2
<p>Prototype: def multiply_by_2(my_dict):</p>
<p>All values should be integers</p>
<p>Returns a new dictionary</p>

```
>>> multiply_by_2 = __import__('9-multiply_by_2').multiply_by_2
>>> print_sorted_dictionary =  __import__('6-print_sorted_dictionary').print_sorted_dictionary

>>> my_dict = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
>>> new_dict = multiply_by_2(my_dict)
>>> print_sorted_dictionary(my_dict)
Alex: 8
Bob: 14
>>> print_sorted_dictionary(new_dict)
Alex: 16
Bob: 28
```

## 10-best_score.py
### Function that returns a key with the biggest integer value
<p>Prototype: def best_score(my_dict):</p>
<p>All values should be integers</p>
<p>If no score found, returns None</p>

```
>>> best_score = __import__('10-best_score').best_score

>>> my_dict = {'John': 12, 'Mike': 14, 'Molly': 16}
>>> best_key = best_score(my_dict)
>>> print("Best score: {}".format(best_key))
Best score: Molly
>>> best_key = best_score(None)
>>> print("Best score: {}".format(best_key))
Best score: None
```

## 11-mutiply_list_map.py
### Function that returns a list with all values multiplied by a number  
<p>Prototype: def mutiply_list_map(my_list=[], number=0):</p>
<p>Returns a new list where each value is multiplied by number

```
>>> mutiply_list_map = __import__('11-mutiply_list_map').mutiply_list_map

>>> my_list = [1, 2, 3, 4, 6]
>>> new_list = mutiply_list_map(my_list, 4)
>>> print(new_list)
[4, 8, 12, 16, 24]
>>> print(my_list)
[1, 2, 3, 4, 6]
```
