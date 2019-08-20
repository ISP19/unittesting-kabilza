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
| nested lists without "," |  SyntaxError      |
| what other test case?  |  what result?       |


## Test Cases for Fraction
