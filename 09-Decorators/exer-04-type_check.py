# def type_check(exp_type):
#     def decorator(func):
#         def wrapper(arg):
#             if not isinstance(arg, exp_type):
#                 return "Bad Type"
#             return func(arg)
#         return wrapper
#     return decorator
#
#
# @type_check(int)
# def times2(num):
#     return num * 2
#
#
# print(times2(2))
# print(times2('Not A Number'))
#
# @type_check(str)
# def first_letter(word):
#     return word[0]
#
# print(first_letter('Hello World'))
# print(first_letter(['Not', 'A', 'String']))


# Notes: I use arg instead of *args, because there i expect one argument if the there are more arguments then the code should look something like this:

def type_check(exp_type):
    def decorator(func):
        def wrapper(*args):
            for arg in args:
                if not isinstance(arg, exp_type):
                    return "Bad Type"
            return func(args)
        return wrapper
    return decorator


@type_check(int)
def sum_of_list(*nums):
    return sum(*nums)

print(sum_of_list(1,2,3))

@type_check(str)
def some_text(*args):
    return "\n".join(*args)

print(some_text("Person", "Cat", "Car", "Dog"))