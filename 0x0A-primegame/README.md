# Project Name
**0x0A. Prime Game**

## Author's Details
Name: *Wendy Munyasi.*

Email: *wendymunyasi@gmail.com*

Tel: *+254707240068.*

##  Requirements

### Python Scripts
*   Allowed editors: `vi`, `vim`, `emacs`.
*   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using gcc, using python3 (version 3.8.5).
*   All your files should end with a new line.
*   The `main.py` files are used to test your functions, but you don’t have to push them to your repo.
*   The first line of all your files should be exactly `#!/usr/bin/python3`.
*   Your code should use the pycodestyle (version `2.8.*`).
*   All your files must be executable.
*   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`).
*   All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)`' and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`).
*   A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified).


## Project Description

### 0. Prime Game

Maria and Ben are playing a game. Given a set of consecutive integers starting from `1` up to and including `n`, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game.

They play `x` rounds of the game, where `n` may be different for each round. Assuming Maria always goes first and both players play optimally, determine who the winner of each game is.

-   Prototype: `def isWinner(x, nums)`
-   where `x` is the number of rounds and `nums` is an array of `n`
-   Return: name of the player that won the most rounds
-   If the winner cannot be determined, return `None`
-   You can assume `n` and `x` will not be larger than 10000
-   You cannot import any packages in this task

Example:

-   `x` = `3`, `nums` = `[4, 5, 1]`

First round: `4`

-   Maria picks 2 and removes 2, 4, leaving 1, 3
-   Ben picks 3 and removes 3, leaving 1
-   Ben wins because there are no prime numbers left for Maria to choose

Second round: `5`

-   Maria picks 2 and removes 2, 4, leaving 1, 3, 5
-   Ben picks 3 and removes 3, leaving 1, 5
-   Maria picks 5 and removes 5, leaving 1
-   Maria wins because there are no prime numbers left for Ben to choose

Third round: `1`

-   Ben wins because there are no prime numbers for Maria to choose

**Result: Ben has the most wins**

```
carrie@ubuntu:~/0x0A-primegame$ ./main_0.py
Winner: Ben
carrie@ubuntu:~/0x0A-primegame$
```

---

## Collaborate

To collaborate, reach me through my email address wendymunyasi@gmail.com.
