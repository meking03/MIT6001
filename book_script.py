# -*- coding: utf-8 -*-
"""
Created on Sun May  3 13:24:34 2020

@author: egultekin
"""

### Lesson 1 : What is computation?

# print('Yankees rule, ', 'but not in Boston!')

# x, y = 2, 3
# x, y = y, x
# print('x = ', x)
# print('y = ', y)

### Lesson 2 : Branching and iteration

# def find_largest_odd(x, y, z):
#     params = [x, y, z]
#     odds = []
#     for i in params:
#         if i % 2 != 0:
#             odds.append(i)
#         else:
#             continue
#     if len(odds) > 0:
#         largest_odd = max(odds)
#         print('Largest odd number is ' + str(largest_odd))
#     else:
#         print('There are no odd numbers.')

# find_largest_odd(13, 15, 18)
# find_largest_odd(12, 14, 16)

# def largest_odd_finder(a, b, c, d, e, f, g, h, i, j):
#     params = [a, b, c, d, e, f, g, h, i, j]
#     odds = []
#     for i in params:
#         if i % 2 != 0:
#             odds.append(i)
#         else:
#             continue
#     if len(odds) > 0:
#         largest_odd = max(odds)
#         print('Largest odd number is ' + str(largest_odd))
#     else:
#         print('There are no odd numbers.')
        
# largest_odd_finder(5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
# largest_odd_finder(16, 6, 18, 8, 20, 10, 22, 12, 24, 14)

# def sum_of_numbers(*arg):
#     sum = 0
#     for i in arg:
#         sum = sum + i
#     print(sum)
# sum_of_numbers(10.5, 20, 5, 6, -1.8, -15, 8.912)

### Lesson 3 : String Manipulation, Guess and Check, Approximations, Bisection

# Find the cube root of a perfect cube
# x = int(input('Enter an integer: '))
# ans = 0
# while ans**3 < abs(x):
#  ans = ans + 1
# if ans**3 != abs(x):
#  print (x, 'is not a perfect cube')
# else:
#  if x < 0:
#      ans = -ans
#  print ('Cube root of', x,'is', ans)

# def Sahari_and_Ekini():
#     x = int(input('Enter an integer: '))
#     root = 0
#     pwr = list(range(5, 0, -1))
    
#     for i in pwr:
#         ans = root ** i
#         while ans < abs(x):
#             root += 1
#             ans = root ** i
#         if ans == abs(x):
#             if x > 0:
#                 print(x, 'is', root, 'to the power of', i)
#             elif x < 0 and i % 2 != 0:
#                 root = -root
#                 print(x, 'is', root, 'to the power of', i)
#         else:
#             continue

# Sahari_and_Ekini()

### Exhaustive enumeration

# x = 25
# epsilon = 0.01
# step = epsilon**2
# numGuesses = 0
# ans = 0.0
# while abs(ans**2 - x) >= epsilon and ans <= x:
#     ans += step
#     numGuesses += 1
# print ('numGuesses =', numGuesses)
# if abs(ans**2 - x) >= epsilon:
#     print('Failed on square root of', x)
# else:
#     print(ans, 'is close to square root of', x)


### Bisection search

# x = 25
# epsilon = 0.01
# numGuesses = 0
# low = 0.0
# high = max(1.0, x)
# ans = (high + low)/2.0
# while abs(ans**2 - x) >= epsilon:
#     print('low =', low, 'high =', high, 'ans =', ans)
#     numGuesses += 1
#     if ans**2 < x:
#         low = ans
#     else:
#         high = ans
#     ans = (high + low)/2.0
# print('numGuesses =', numGuesses)
# print(ans, 'is close to square root of', x)


### Newton-Raphson for square root

# Find x such that x**2 - 24 is within epsilon of 0.01

# epsilon = 0.01
# k = 24.0
# guess = k/2.0
# numGuesses = 0
# while abs(guess*guess - k) >= epsilon:
#     guess = guess - (((guess**2) - k)/(2*guess))
#     numGuesses += 1
# print('Square root of', k, 'is about', guess)
# print('numGuesses =', numGuesses)

### Lesson 4 : Functions, Scoping and Abstraction

# this function checks if either string occurs anywhere in the other and returns True
# def isIn(string1, string2):
#     if string1 in string2:
#         return True
#     elif string2 in string1:
#         return True
#     else:
#         return False
    

# print(isIn('sahari', 'asaharil'))


# def f(x):
#      def g():
#          x = 'abc'
#          print('x =', x)
#      def h():
#          z = x
#          print('z =', z)
#      x = x + 1
#      print('x =', x)
#      h()
#      g()
#      print('x =', x)
#      return g
# x = 3
# z = f(x)
# print('x =', x)
# print('z =', z)
# z()

### Lesson 5 : Tuples, Lists, Aliasing, Mutability and Cloning

# def findExtremeDivisors(n1, n2):
#     """Assumes that n1 and n2 are positive ints
#     Returns a tuple containing the smallest common
#     divisor > 1 and the largest common divisor of n1
#     and n2"""
#     minVal, maxVal = None, None
#     for i in range(2, min(n1, n2) + 1):
#         if n1%i == 0 and n2%i == 0:
#             if minVal == None or i < minVal:
#                 minVal = i
#             if maxVal == None or i > maxVal:
#                 maxVal = i
#     return (minVal, maxVal)

# minDivisor, maxDivisor = findExtremeDivisors(100, 200)
# print(minDivisor, maxDivisor)

# L1 = [1,2,3]
# L2 = [4,5,6]
# L3 = L1 + L2
# print('L3 =', L3)
### extend function adds the values of a list onto another list
# L1.extend(L2)
# print('L1 =', L1)
### append function adds the list itself w/o changing object type onto another list
# L1.append(L2)
# print('L1 =', L1)


### Lesson 6 : Recursion, Dictionaries

# def fib(n):
#     """Assumes n an int >= 0
#     Returns Fibonacci of n"""
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# def testFib(n):
#     for i in range(n+1):
#         print('fib of', i, '=', fib(i))

# testFib(5)

# def isPalindrome(s):
#     """Assumes s is a str
#     Returns True if s is a palindrome; False otherwise.
#     Punctuation marks, blanks, and capitalization are
#     ignored."""
    
#     def toChars(s):
#         s = s.lower()
#         letters = ''
#         for c in s:
#             if c in 'abcdefghijklmnopqrstuvwxyz':
#                 letters = letters + c
#         return letters

#     def isPal(s):
#         print(' isPal called with', s)
#         if len(s) <= 1:
#             print(' About to return True from base case')
#             return True
#         else:
#             answer = s[0] == s[-1] and isPal(s[1:-1])
#             print(' About to return', answer, 'for', s)
#             return answer
    
#     return isPal(toChars(s))

# def testIsPalindrome():
#     print('Try dogGod')
#     print(isPalindrome('dogGod'))
#     print('Try doGood')
#     print(isPalindrome('doGood'))
    
# testIsPalindrome()

### Lesson 7 : 	Testing, Debugging, Exceptions, Assertions

# def sumDigits(s):
#     ''' Assumes s is a string
#     Returns the sum of the decimal digits in s
#     For example, if s is 'a2b3c' it returns 5 '''
#     sum = 0
#     for i in s:
#         try:
#             i = int(i)
#             sum += i
#         except ValueError:
#             print(i + ' is not a numerical digit.')
#     print(sum)
    
# sumDigits('a2b3c')
# sumDigits('$%14.1AbC')


# def findAnEven(l):
#     ''' Assumes l is a list of integers
#     Returns the first even number in l
#     Raises ValueError if l does not contain an even number'''
#     evenNumbers = []
#     for i in l:
#         try:
#             if i % 2 == 0:
#                 evenNumbers.append(i)
#         except TypeError:
#             # print(i + ' is non-integer.')
#             pass
#     if len(evenNumbers) > 0:
#         return evenNumbers[0]
#     else:
#         raise ValueError(l, 'The list does not contain an even number.')
        
# print(findAnEven([3,5,7,'l',2]))
# print(findAnEven([3,5,7,'l']))


### Lesson 8 : Object Oriented Programming

## 8.4 Mortgages Example

# def findPayment(loan, r, m):
#     """Assumes: loan and r are floats, m an int
#     Returns the monthly payment for a mortgage of size
#     loan at a monthly rate of r for m months"""
#     return loan*((r*(1+r)**m)/((1+r)**m - 1))

# class Mortgage(object):
#     """Abstract class for building different kinds of mortgages"""
#     def __init__(self, loan, annRate, months):
#         """Create a new mortgage"""
#         self.loan = loan
#         self.rate = annRate/12.0
#         self.months = months
#         self.paid = [0.0]
#         self.owed = [loan]
#         self.payment = findPayment(loan, self.rate, months)
#         self.legend = None #description of mortgage
#     def makePayment(self):
#         """Make a payment"""
#         self.paid.append(self.payment)
#         reduction = self.payment - self.owed[-1]*self.rate
#         self.owed.append(self.owed[-1] - reduction)
#     def getTotalPaid(self):
#         """Return the total amount paid so far"""
#         return sum(self.paid)
#     def __str__(self):
#         return self.legend
    
# class Fixed(Mortgage):
#     def __init__(self, loan, r, months):
#         Mortgage.__init__(self, loan, r, months)
#         self.legend = 'Fixed, ' + str(r*100) + '%'

# class FixedWithPts(Mortgage):
#     def __init__(self, loan, r, months, pts):
#         Mortgage.__init__(self, loan, r, months)
#         self.pts = pts
#         self.paid = [loan*(pts/100.0)]
#         self.legend = 'Fixed, ' + str(r*100) + '%, ' + str(pts) + ' points'
        
# class TwoRate(Mortgage):
#     def __init__(self, loan, r, months, teaserRate, teaserMonths):
#         Mortgage.__init__(self, loan, teaserRate, months)
#         self.teaserMonths = teaserMonths
#         self.teaserRate = teaserRate
#         self.nextRate = r/12.0
#         self.legend = str(teaserRate*100) + '% for ' + str(self.teaserMonths) + ' months, then ' + str(r*100) + '%'
#     def makePayment(self):
#         if len(self.paid) == self.teaserMonths + 1:
#             self.rate = self.nextRate
#             self.payment = findPayment(self.owed[-1], self.rate, self.months - self.teaserMonths)
#         Mortgage.makePayment(self)


# def compareMortgages(amt, years, fixedRate, pts, ptsRate, varRate1, varRate2, varMonths):
#     totMonths = years*12
#     fixed1 = Fixed(amt, fixedRate, totMonths)
#     fixed2 = FixedWithPts(amt, ptsRate, totMonths, pts)
#     twoRate = TwoRate(amt, varRate2, totMonths, varRate1, varMonths)
#     morts = [fixed1, fixed2, twoRate]
#     for m in range(totMonths):
#         for mort in morts:
#             mort.makePayment()
#     for m in morts:
#         print(m)
#         print(' Total payments = $' + str(int(m.getTotalPaid())))
        
# compareMortgages(amt=200000, years=30, fixedRate=0.07, pts = 3.25, ptsRate=0.05,
#                  varRate1=0.045, varRate2=0.095, varMonths=48)

### Lesson 9: Python Classes and Inheritance

### Lesson 10 : Understanding Program Efficiency, Part 1

### Lesson 11 : Understanding Program Efficiency, Part 2

### Lesson 12 : Searching and Sorting Algorithms






              
            
            
