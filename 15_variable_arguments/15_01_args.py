'''
Write a script with a function that demonstrates the use of *args.

'''


def greeter(*args):
    print("Hello!", args)


names = ["Michael"]

greeter(*names)

#removing comma syntax around on the output?
# f"Hello! {args}" returns the same

#adding *names (vs just 'names') removes the []... likewise interesting to note that the args seems to function
# with or without * but calling kwargs without the ** fails...