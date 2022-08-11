# Perfect numbers script

## Contents
- [Keywords](#keywords)
- [Introduction](#introduction)
  - [Description](#description)
  - [Context](#context)
  - [Proposal](#proposition)
- [Installation](#installation)
- [Use](#use)
- [Helpful links](#links)

## Keywords <a class="anchor" id="keywords"></a>
- Perfect numbers.
- Prime numbers.
- Algorithms.
- Euclid-Euler theorem.
- Big O notation.

## Introduction <a class="anchor" id="introduction"></a>

### Description <a class="anchor" id="description"></a>

"Perfect numbers script" aims to get perfect numbers in a number range.

A **perfect number** is a positive integer that is equal to the sum of its positive divisors, 
excluding the number itself. For instance, 6 has divisors 1, 2 and 3 (excluding itself).
Because of 1 + 2 + 3 is equal to 6, number 6 is a perfect number.

### Context <a class="anchor" id="context"></a>

Among the comments on a YT video about technical interviews, someone mentioned
a technical test that consisted of getting perfect numbers given a range of a number.
This test had a challenge : to discard unnecessary loops.

Some solutions proposed by YT users were to implement double loop or recursion on scripts, 
but they concluded that these suggestions were not optimal solutions, and this is absolutely 
true because of their complexities: for a double loop we have O(n^2) and for recursion O(2^n).

### Proposal <a class="anchor" id="proposition"></a>

Given that, I thought there could be a **solution based on algorithms**, without 
having to iterate a big list of numbers... and there is one: **Euclid-Euler theorem**.

Euclid-Euler theorem states that an even number is perfect if, and only if, it has 
the form: <p align="center"> [ 2^(p-1) ] * [ 2^(p) - 1 ] </p>
where " [ 2^(p) - 1 ] " and " p " must be prime numbers.

To implement this theorem, we need firstly **to verify if numbers are prime numbers**. 
To determine it, I implemented:

    for iterated_number in range(2, int(square_root_number) + 1):
        if (number % iterated_number) == 0:

If condition is True, that means there is another number between 1 and the number that
we are evaluating, and which divides our number. If not, the number that we are evaluating 
is a prime number.

This part of script implies a square root complexity O(n^1/2), that is a complexity 
smaller than a linear O(n).

Concerning calcul of perfect number, it implies a O(n) complexity due to iteration of 
" p " number. Nevertheless, this iteration has low values. For exemple, if we want to 
know how many perfect numbers are in a range of 10000, " p " is equal to 10.

In conclusion, with this script we have a global complexity of O(n).

NB : After reflexion, and given that loops of prime number condition are inside of while 
loop, I think global complexity could be O(n^3/2) (if that is allowed as notation). 
In any case, **complexity of script is between quadratic complexity O(n^2) and linear 
complexity O(n)**. 

## Installation <a class="anchor" id="installation"></a>

Python version : 3.9.4

To get project, launch :
```
git clone https://github.com/edaucohe/perfect_numbers.git
```

To create virtual environment, go into the folder `../perfect_numbers/` and launch :
```
python -m venv env  
```

To activate virtual environment, launch :

- In windows
```
source env/Scripts/activate
```
- In Linux
```
source env/bin/activate
```

There is no dependencies.

## Use <a class="anchor" id="use"></a>

To start script, go into the terminal and launch:
```
python main.py
```

There is not yet a navigation menu in order to input a number to evaluate. 
So, it is needed to modify `NUMBER` constant to test others numbers.

## Helpful links <a class="anchor" id="links"></a>

Euclid-Euler theorem (english) : https://en.wikipedia.org/wiki/Euclid%E2%80%93Euler_theorem

Prime number checking (spanish): https://geekflare.com/es/prime-number-in-python/#geekflare-toc-o-n-algorithm-to-check-for-prime-number-in-python
