'''
Write a script with a function that demonstrates the use of **kwargs.

'''


def order_dish(**kwargs):
    for k, v in kwargs.items():
        print("{} {}".format(k, v))

menu = {
    'Dominos' : "Pizza",
    'McDonalds' : "BigMac",
    'KFC' : "Chicken"
}

order_dish(**menu)
