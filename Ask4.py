import sys

sum = 0
x = 0
y = 0

string = input('enter text here:')


firstnumber, action, secondnumber, none = string.split('(')

if action != 'times' and action != 'plus' and action != 'minus':
    print('Error action not found!!')
    sys.exit()
if firstnumber != 'zero' and firstnumber != 'one' and firstnumber != 'two' and firstnumber != 'three' and firstnumber != 'four' and firstnumber != 'five' and firstnumber != 'six' and firstnumber != 'seven' and firstnumber != 'eight' and firstnumber != 'nine':
    print('Error first number not found!!')
    sys.exit()
if secondnumber != 'zero' and secondnumber != 'one' and secondnumber != 'two' and secondnumber != 'three' and secondnumber != 'four' and secondnumber != 'five' and secondnumber != 'six' and secondnumber != 'seven' and secondnumber != 'eight' and secondnumber != 'nine':
    print('Error second number not found!!')
    sys.exit()


def addition(x, y):
    sum = x+y
    print(x, '+', y, '=', sum)
    return sum


def subtraction(x, y):
    sum = x-y
    print(x, '-', y, '=', sum)
    return sum


def multiplication(x, y):
    sum = x*y
    print(x, '*', y, '=', sum)
    return sum


def findsecond(secondnumber):
    global y
    if secondnumber == 'zero':
        y = 0
    elif secondnumber == 'one':
        y = 1
    elif secondnumber == 'two':
        y = 2
    elif secondnumber == 'three':
        y = 3
    elif secondnumber == 'four':
        y = 4
    elif secondnumber == 'five':
        y = 5
    elif secondnumber == 'six':
        y = 6
    elif secondnumber == 'seven':
        y = 7
    elif secondnumber == 'eight':
        y = 8
    elif secondnumber == 'nine':
        y = 9
    return y


def zero(action,y):

    if action == 'times':
        x = 0
        multiplication(x, y)
    elif action == 'plus':
        x = 0
        addition(x, y)
    elif action == 'minus':
        x = 0
        subtraction(x, y)


def one(action,y):

    if action == 'times':
        x = 1
        multiplication(x, y)
    elif action == 'plus':
        x = 1
        addition(x, y)
    elif action == 'minus':
        x = 1
        subtraction(x, y)


def two(action,y):

    if action == 'times':
        x = 2
        multiplication(x, y)
    elif action == 'plus':
        x = 2
        addition(x, y)
    elif action == 'minus':
        x = 2
        subtraction(x, y)


def three(action,y):

    if action == 'times':
        x = 3
        multiplication(x, y)
    elif action == 'plus':
        x = 3
        addition(x, y)
    elif action == 'minus':
        x = 3
        subtraction(x, y)


def four(action,y):

    if action == 'times':
        x = 4
        multiplication(x, y)
    elif action == 'plus':
        x = 4
        addition(x, y)
    elif action == 'minus':
        x = 4
        subtraction(x, y)


def five(action,y):

    if action == 'times':
        x = 5
        multiplication(x, y)
    elif action == 'plus':
        x = 5
        addition(x, y)
    elif action == 'minus':
        x = 5
        subtraction(x, y)


def six(action,y):

    if action == 'times':
        x = 6
        multiplication(x, y)
    elif action == 'plus':
        x = 6
        addition(x, y)
    elif action == 'minus':
        x = 6
        subtraction(x, y)


def seven(action,y):

    if action == 'times':
        x = 7
        multiplication(x, y)
    elif action == 'plus':
        x = 7
        addition(x, y)
    elif action == 'minus':
        x = 7
        subtraction(x, y)


def eight(action,y):

    if action == 'times':
        x = 8
        multiplication(x, y)
    elif action == 'plus':
        x = 8
        addition(x, y)
    elif action == 'minus':
        x = 8
        subtraction(x, y)


def nine(action,y):

    if action == 'times':
        x = 9
        multiplication(x, y)
    elif action == 'plus':
        x = 9
        addition(x, y)
    elif action == 'minus':
        x = 9
        subtraction(x, y)


def main(firstnumber, action, secondnumber):


    if firstnumber == 'zero':
        findsecond(secondnumber)
        zero(action, y)

    if firstnumber == 'one':
        findsecond(secondnumber)
        one(action, y)

    if firstnumber == 'two':
        findsecond(secondnumber)
        two(action, y)

    if firstnumber == 'three':
        findsecond(secondnumber)
        three(action, y)

    if firstnumber == 'four':
        findsecond(secondnumber)
        four(action, y)

    if firstnumber == 'five':
        findsecond(secondnumber)
        five(action, y)

    if firstnumber == 'six':
        findsecond(secondnumber)
        six(action, y)

    if firstnumber == 'seven':
        findsecond(secondnumber)
        seven(action, y)

    if firstnumber == 'eight':
        findsecond(secondnumber)
        eight(action, y)

    if firstnumber == 'nine':
        findsecond(secondnumber)
        nine(action, y)


main(firstnumber, action, secondnumber)

