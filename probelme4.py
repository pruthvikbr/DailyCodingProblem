'''
In this exercise, you’ll implement a functional representation of a pair. This problem was originally asked by Jane Street and is a classic example of using closures to simulate data structures.

You are given the following implementation of cons in Python:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

The cons function returns a closure that, when called with a function f, applies f to the two elements a and b. Your task is to implement the functions car and cdr, which retrieve the first and second elements of the pair, respectively.

'''

def cons(a,b):
    def pair(f):
        return f(a,b)
    return pair

def car(pair):
    def return_first_element(a,b):
        return a
    return pair(return_first_element)

def cdr(pair):
    def return_last_element(a,b):
        return b
    return pair(return_last_element)


car(cons(5,1))

#Test Cases
assert car(cons(3, 4)) == 3
assert cdr(cons(3, 4)) == 4

assert car(cons("apple", "banana")) == "apple"
assert cdr(cons("apple", "banana")) == "banana"

nested = cons(cons(1, 2), cons(3, 4))
assert car(car(nested)) == 1  # First element of first pair
assert cdr(car(nested)) == 2  # Second element of first pair
assert car(cdr(nested)) == 3  # First element of second pair
assert cdr(cdr(nested)) == 4  # Second element of second pair

assert car(cons(True, False)) is True
assert cdr(cons(True, False)) is False