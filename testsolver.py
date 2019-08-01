from sympy import sympify
import itertools

numbers = [3,5,7,6,9]
result = 62 

operators = list(itertools.product(['+','-','*','/'], repeat = len(numbers)-1))

for op in operators:
    eq = ''
    for n in range(len(numbers)-1):
        eq += '%d%s' %(numbers[n],op[n])
    eq += '%d' % numbers[-1]
    res = sympify(eq)
    if res == result:
        print "success!"
        print "%s = %d" % (eq,result)
        break
