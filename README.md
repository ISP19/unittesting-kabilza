## Unit Testing Assignment

by Bill Gates.


## Test Cases for unique

>>> unique([5])
    [5]
>>> unique([1,2,3,3,4])
    [1,2,3,4]
>>> unique([[][][]]])
    File "", line 1
    print(unique([[][][]]]))
                     ^
SyntaxError: invalid syntax

>>> unique([1,2,3,4,5,4,23,132,432,5354,65,34,23,645,65,76,87,94,342,65,778,343,34,12])
    [1, 2, 3, 4, 5, 23, 132, 432, 5354, 65, 34, 645, 76, 87, 94, 342, 778, 343, 12]

Write a table describing your test cases.

| Test case              |  Expected Result    |
|------------------------|---------------------|
| empty list             |  empty list         |
| one item               |  list with 1 item   |
| one item many times    |  list with 1 item   |
| 2 items, many times, many orders | 2 item list, items in same order  |
| integers and string mixed between |  all duplicates were deleted at the outcome       |
| many integers with some duplicates  | all duplicates were deleted at the outcome   |
| nested lists without "," |  raise SyntaxError      |
| input a word in string (not in a list with []) |  returns individuals of the string eg. 'r' 'a'   |
| input a word in string (in a list with []) |  returns the string that are unique |
| input an integer |  raise TypeError     |


## Test Cases for Fraction

>>> print(Fraction(60, 90))
    2/3

>>> print(Fraction(3, -1))
    -3

>>> print(Fraction(36, -60))
    -3/5

>>> print(Fraction('ab', 'ac'))
        TypeError                                 Traceback (most recent call last)
    in 
    ----> 1 print(Fraction('ab','ac'))

    in __init__(self, numerator, denominator)
        15            and denominator (default 1).
        16         """
    ---> 17         gcd1 = math.gcd(numerator, denominator)
        18 
        19         if denominator < 0:

    TypeError: 'str' object cannot be interpreted as an integer

| Test case              |  Expected Result    |
|------------------------|---------------------|
| regular fraction         | return fraction with the smallest numerator/denominator in string format   |
| fraction with out denominator       | return fraction with denominator set default to 1   |
| input string such 'a' into Fraction class      |  NameError   |
| fraction with negative(-) denominator    |  return answer with negative value  |
| input integer with 0/0 both numerator and denominator |  return zero |