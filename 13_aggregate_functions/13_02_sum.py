'''
Write a simple aggregate function, sum(), that takes a list a returns the sum.

'''

def sum(*args):
    result = 1
    for x in args:
        result += x
    return result

print(sum(1, 5, 2))