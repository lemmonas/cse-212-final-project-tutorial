# Stacks

## Introduction

The first topic we'll cover is stacks. Stacks keep track of the order data is added to a list. They use an organization system called LIFO, or Last In, First Out. 

## How it Works

Because stacks keep track of the order data is added, the order in which it is removed from the stack is the reverse of how it was added. When initializing a stack, you use brackets whether you're starting with an empty stack or not.

Say you're writing and essay on your computer and you accidentally delete the last few sentences you wrote, so you hit the undo button to get your work back. The undo button only works because the word processor uses a stack to keep track of all of the edits you make. Everything you type is added to the stack, and the undo button pulls the last letters you typed off the stack and puts them back in your document.

## Applicable Functions

**Push**: The push function adds data to the end of the stack. Python code example: 

```python
ex_stack.append(data)
```

**Pop**: The pop function removes the last piece of data that was added to the stack. Python code example: 

```python
data = ex_stack.pop()
```

**Size**: the size function prints the number of items the stack contains. Python code example: 

```python
size = len(ex_stack)
```

**Empty**: The empty function tells you whether the stack contains any data. Python code example: 

```python
if len(ex_stack) == 0:

    return true
```
This function can also be modified to have the program check for other lengths and do whatever you need it to do.

## Big O Notation

The big O notation for each individual function is O(1). The performance of a program with multiple stack manipulation functions would also be O(1) because in O notation we only take the highest order present. A program with multiple functions of O(1) would just have all of those ones added together and because O notation removes constants, the end result would still be O(1). However, if you have a program that uses a loop on the stack, the O notation would change to O(n).

## Example Code

As an example, say you have a list of assignments that you want to reverse. Here's how you could go about implementing a program to do that:

```python
def reverse_list(my_list):
    stack = []
    rev_stack = []
    for item in my_list:
        stack.append(item)
    while len(stack) != 0:
        temp = stack.pop()
        rev_stack.append(temp)
    return rev_stack
```

The first variable, `stack`, contains an empty stack to hold the original list and `rev_stack` will hold the reversed list. The `for` loop will take every item in the list and add it to the stack. The `while` loop will take each item off the original stack and add it to the new stack.

## Example Problem

As practice, try to write a program for what happens when you visit a new website, and then click the back button.

[Example solution file](stack-ex-solution.py)

[**Next section**](2-sets.md)

[Back to start](0-welcome.md)