'''
Write a decorator function that wraps text passed to it in a specified html tag.
The user should be able to decide which tag to use.

'''

def tag(tag_name):
    def tags_decorator(func):
        def func_wrapper(name):
            return f"<{tag_name}>{func(name)}</{tag_name}>"
        return func_wrapper
    return tags_decorator

tagtype = input("please enter html tag: ")

@tag(tagtype)
def get_text(text):
    return text

print(get_text(input("please enter text to wrap: ")))
