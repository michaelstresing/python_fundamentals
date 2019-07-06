'''
1 - Write and execute a script that prints "hello world" to the console.

2 - Using the interpreter, print "hello world!" to the console.

3 - Explore the interpreter.
	- Execute lines with syntax error and see what the response is.
        * What happens if you leave out a quotation or parentheses?
        * How helpful are the error messages?
	- Use the help() function to explore what you can do with the interpreter.
        For example execute help('print').
        press q to exit.
	- Use the interpreter to perform simple math.
	- Calculate how many seconds are in a year.

'''
#1 + 2
print("hello world!")

#3
''' print(hello oops) in Python Console in Pycharm, this gave me: 

  File "<input>", line 1
    print(hello oops)
                   ^
SyntaxError: invalid syntax

The pointer is super helpful!
'''

'''entered "help(print) into Python Console in Pycharm, this gave me:
Help on built-in function print in module builtins:
print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
'''

''' In interpreter ran 2 + 5 -> 7, and 45 // 20 -> 2
'''

#seconds in a year

minute = 60
hour = 60 * minute
day = 24 * hour
year = 365 * day
print(year)