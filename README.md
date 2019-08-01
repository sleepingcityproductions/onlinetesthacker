# Online Placement Test Hacker
## A very short Python script for solving online placement equation puzzles

I recently stumpled upon online placement tests of the form

<a href="https://www.codecogs.com/eqnedit.php?latex=3&space;\square&space;5&space;\square&space;7&space;\square&space;6&space;\square&space;9&space;=&space;62" target="_blank"><img src="https://latex.codecogs.com/gif.latex?3&space;\square&space;5&space;\square&space;7&space;\square&space;6&space;\square&space;9&space;=&space;62" title="3 \square 5 \square 7 \square 6 \square 9 = 62" /></a>

where the correct operators (+,-,\*,/) must be placed in the squares to satisfy the equations. The purpose of those tests is, of course, to find the correct combination as fast as possible.

Anyone with a bit of math background will recognize immediately that there a in total 4^4 = 256 combinations for placing the operators. (One needs four operators, and each square can contain four different operators)

My first thought was, wow, that's easy to do in Python. I knew that the the `itertools` exist in Python for creating all combinations of operators.

So the first crucial step is to generate a nested list of all operator combinations. This is done by 

```Python
operators = list(itertools.product(['+','-','*','/'], repeat = len(numbers)-1))
```
Of course, one needs one operator less than the numbers left of the equal sign. Here, `itertools.product` creates all combinations. 

Now comes the fun part!

We now need to assemble the left side of the equation, calculate the value and compare it to the desired result. But I forgot one thing when I first thought about it: One needs to consider operator precendence (i.e. * before +). This would make the whole thing a bit more difficult (and longer) to write down. 

However, I remembered that there is the SymPy package for symbolic calculations. Maybe there is a function that can convert a string to an expression that can be evaluated? Indeed, there is:
```Python
res = sympify(eq)
```
`sympfiy()` takes a string and evaluates it. The result is stored in `res`. Then it is just a matter of assembling the left-hand-side string. Easy peasy.

The whole thing fits together into 18 lines of Python code. 

And just in case you are still puzzled what the correct result is, here it is!

<a href="https://www.codecogs.com/eqnedit.php?latex=3&space;\square&space;5&space;\square&space;7&space;\square&space;6&space;\square&space;9&space;=&space;62" target="_blank"><img src="https://latex.codecogs.com/gif.latex?3&space;*&space;5&space;-&space;7&space;+&space;6&space;*&space;9&space;=&space;62" title="3 \square 5 \square 7 \square 6 \square 9 = 62" /></a>
