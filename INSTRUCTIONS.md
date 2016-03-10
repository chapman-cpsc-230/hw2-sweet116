# Instructions

This assignement is due on Friday March 4 at 8:00AM. I will start grading on Friday morning. I suggest you plan to submit the work no later than Thursday evening.

## This Assignment

### Sum of Powers

Write a program that does the following

* Queries the user for a floating point number, which we will call `b` (should not be equal to `1.0`),
 and a natural number, which we will call `n`.
* Compute the sum `1 + b + b^2 + ... + b^n`.
* Print the result of this computation
* Print the value `b^(n+1)/(b-1)`.

Submit this program as `sum_powers.py`

### Cooling

Isaac Newton (as an application of his new invention of Calculus) considered the question of how quickly a cup of hot tea will cool to room temperature. He observed that the _rate_ of cooling is proportional to the difference between the temperature of the tea and the ambient (room) temperature. If we indicate the temperature of the tea as `T` and the ambient air temperature as `T_a`, then this means that at any instance, the rate of cooling will be `-k(T - T_a)` -- the negative sign is because we think of cooler temperatures as going in the negative direction.
The number `k` depends on material science (the specific composition of the tea) and on units (I'll use minutes for time and degrees Celsius for temperatures). The constant `k` could be estimated by conducting experiments. We will take it to be 0.055, a decent estimate based on actual experiments.

In principle, if `T` starts at 100 (degrees I'm calculating in Celsius -- so this is boiling water) and `T_a` is 20 degrees (a comfortable room temperature), we know that the tea will start out cooling at a rate of `0.055*(100-20)` degrees per minute. But as the tea cools, `T` gets smaller but `T_a` remains (very nearly) constant, so the tea cools at a slower rate.

We can model this somewhat crudely, using a while loop. If at a particular time, the tea temperature is $T$, then a minute later it should be approximately `T - k(T-T_a)`.

Write a program that does the following:

* Query the user for an initial tea temperature `T_tea`, an ambient temperature `T_air` and a number of hours minutes `num_minutes`
* Print a table of the approximate temperature of the tea at each minute $m$ from 0 up to but not including `num_minutes`.

Your results should look exactly like this (use formetted strings):

```
Temperature of the air: 20
Number of minutes: 20
Minute Temperature
  0      100.0
  1      95.6
  2      91.4
  3      87.5
  4      83.8
  5      80.3
  6      77.0
  7      73.8
  8      70.9
  9      68.1
 10      65.4
 11      62.9
 12      60.6
 13      58.3
 14      56.2
 15      54.2
 16      52.4
 17      50.6
 18      48.9
 19      47.3
```

Submit a program named `cooling.py`.

This, however, is _not_ a fully accurate model of cooling. It assumes that the rate of cooling does not change between the minutes we are reporting. A more accurate (but still not completely correct) model would be to change the rate $k$ which is denominated in 1/minutes to 1/seconds, then implement an inner loop to update the temperature for ever second. For extra credit, submit a second version, `cooling2.py` that calculates cooling on a second-by-second basis, but still reports the results once for every minute. The result will differ from the previous version as follows:

```
Temperature of the air: 20
Number of minutes: 20
Minute Temperature
  0      100.0
  1      95.7
  2      91.7
  3      87.8
  4      84.2
  5      80.8
  6      77.5
  7      74.4
  8      71.5
  9      68.8
 10      66.1
 11      63.7
 12      61.3
 13      59.1
 14      57.0
 15      55.0
 16      53.2
 17      51.4
 18      49.7
 19      48.1
```
Now ask yourself what would happen if we changed our program to calculate a new temperature one every 0.1 second, or once every 0.01 second, and so on.

## General Instructions

* Complete the README file with your name, date description of the project, etc.
* Be sure to "sign" the honor pledge in the README file.
* Correctly document each source file.
    At the top of each source file (```.py``` file), include a docstring in the following format

```
"""
File: <filename>

Copyright (c) 2016 <your name>

License: MIT

<brief description of the code>

"""    
```

* Ensure that what you push to the github repo is correct.
