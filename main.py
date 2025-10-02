#1
class StringClass:
    def __init__(self):
        self.text = ""

    def getString(self):
        self.text = input("Enter a string: ")

    def printString(self):
        print(self.text.upper())

#2
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

#3
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

#4
import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

#5
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit: {amount}. Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw: {amount}. Balance: {self.balance}")
        else:
            print("Insufficient funds")

#6
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [1, 2, 3, 4, 5, 6, 7, 11, 13, 15, 17, 20]
primes = list(filter(lambda x: is_prime(x), numbers))
print(primes)

#1
def grams_to_ounces(grams):
    return 28.3495231 * grams

#2
def fahrenheit_to_celsius(f):
    return (5 / 9) * (f - 32)

#3
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2 * chickens + 4 * rabbits == numlegs:
            return chickens, rabbits

#4
def filter_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    return list(filter(is_prime, numbers))

#5
import itertools

def string_permutations(s):
    perms = itertools.permutations(s)
    for p in perms:
        print(''.join(p))

#6
def reverse_words(sentence):
    words = sentence.split()
    return ' '.join(words[::-1])

#7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

#8
def spy_game(nums):
    code = [0, 0, 7]
    for n in nums:
        if n == code[0]:
            code.pop(0)
        if not code:
            return True
    return False

#9
import math

def sphere_volume(r):
    return (4/3) * math.pi * (r**3)

#10
def unique_list(lst):
    new_list = []
    for i in lst:
        if i not in new_list:
            new_list.append(i)
    return new_list

#11
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

#12
def histogram(items):
    for n in items:
        print('*' * n)

#13
import random

def guess_game():
    print("Hello! What is your name?")
    name = input()

    number = random.randint(1, 20)
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    guesses = 0
    while True:
        guess = int(input("Take a guess: "))
        guesses += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break


