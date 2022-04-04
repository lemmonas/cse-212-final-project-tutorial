# Sets

## Introduction

Next up is sets. Sets don't keep track of the order data is added like stacks do, but they do have a function that's just as useful: sets don't allow duplicate data to be added.

## How it works

Sets use something called hashing to assign each piece of data a location within the set. Because everything has an assigned location, data that has already been inserted can't be inserted a second time. When initializing a set, you use curly braces if you're already filling the set 

```python
my_set = {2, 4, 6, 8}
```

and parenthesis with `set` in front of them for an empty set, like so:

```python
my_set = set()
```

## Applicable Functions

**Add**: The add function inserts the given data to the set. Python code example:

```python
ex_set.add(data)
```

**Remove**: The remove function deletes the given data from the set. Python code example:

```python
ex_set.remove(data)
```

**Member**: The member function tells you whether the given data is present in the set. Python code example:

```python
if data in ex_set:
    return true
```

**Size**: The size function tells you how many pieces of data are in the set. Python code example:

```python
size = len(ex_set)
```

**Intersection**: The intersection function takes two different sets and finds all of the data that the sets have in common. Python code example:

```python
intersection = ex_set_1 & ex_set_2
```

**Union**: The union function takes two different sets and combines them, returning a set that only has one of each value that was present in the original sets. Python code example:

```python
union = ex_set_1 | ex_set_2
```

Intersections and unions can also be written as a function with multiple lines of code and applying the properties of a set instead of using the set operators, as seen above.

## Big O Notation

The big O notation for each individual function is O(1). In a program with multiple set manipulation functions, the performance will still be O(1). 

## Example code

For this example, say you have a sign up page for a project, but you only want each person to be able to sign up once. Here's how you could write a program to prevent someone from signing up twice:

```python
signed_up = set()
def single_sign_up(name):
    length = len(signed_up)
    signed_up.add(name)
    if length == len(signed_up):
        print("Sorry! You've already signed up.")
    else:
        print("Sign up successful!")
```

The `length` variable holds the original length of the set containing who's signed up. Then, the next person to sign up is added to the set. The `if` statement compares the original length to the new length to determine whether the person currently trying to sign up has already signed up.

## Example problem

Suppose you have been assigned to write a program that keeps track of what letters a player has guessed in an online hangman game, and also gives the appropriate responses to each letter guessed.

Sample responses:

* Letter has already been guessed.

* You've guessed a correct letter!

* Sorry, that letter isn't in the word.

[Example solution file](set-ex-solution.py)

[**Next section**](3-trees.md)

[Back to start](0-welcome.md)

[Previous section](1-stacks.md)