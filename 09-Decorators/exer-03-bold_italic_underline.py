def make_bold(obj):
    def message_printer(*args):
        return f"<b>{obj(*args)}</b>"
    return message_printer

def make_italic(obj):
    def message_printer(*args):
        return f"<b>{obj(*args)}</b>"
    return message_printer

def make_underline(obj):
    def message_printer(*args):
        return f"<u>{obj(*args)}</u>"
    return message_printer
#
@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"

print(greet("Peter"))
