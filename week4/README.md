# Week 3 Python Lists / Arrays

## Prework

Lets do some codeacademy.

1. Do as much of the [codacademy python lesson](https://www.codecademy.com/learn/learn-python) as possible. Feel free to skip lessons if they are boring.
2. Write notes/questions to discuss next week/we can talk about it over the week.
3. Write a python function in `functions.py` that accepts a string `name` and prints and returns `hello <name>`
4. Write a function that takes an array/list and sums the all numbers
5. Write a function that takes an array list and creates a string where each item of the list is seperated by a space (like making a sentence)

## Notes about Lists

Python really only has lists, arrays, sets, the basic, and a few others.

### Lists
Lists are like arrays, excpet a LOT more flexible, you can:
- ARE ordered
- CAN be sorted
- Append/push things to them `[1, 2].append(3) == [1, 2, 3]`
- cut them 
    ```python
    a = [1, 2, 3, 4]
    b = a[1:]
    b == [2, 3, 4]
    ```
- merge two `[1, 2, 3, 4, 5] + [6,7] == [1, 2, 3, 4, 5, 6, 7]`
- create new ones on the fly `[x for x in range(4)]` => `[0, 1, 2, 3]`
- access them by their indexs `array[0]`
- revese them `[1, 2, 3, 4, 5].reverse() == [5, 4, 3, 2, 1]`

```
array = ['A', 'B', 'C']
array[0] = 'F'
print array
# [ 'F', 'B', 'C'] couldnt add another item
array.append('D') # can do this
print array
[ 'F', 'B', 'C', 'D']
``` 

### Dictionaries
Dictionaries are python's version of objects/hashes/maps/key-values
- NOT ordered
- CANOT be sorted
- key value pairs
```
d = {
   'A': 'Apple',
   'B': 'Banana' 
}
d['A'] 
```
