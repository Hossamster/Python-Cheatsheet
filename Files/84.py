'''
calculate(make_float=False, operation='add', message='You just added', first=2, second=4) # "You just added 6"
calculate(make_float=True, operation='divide', first=3.5, second=5) # "The result is 0.7"
'''

def calculate(make_float,operation,message=None,first=1,second=1):
    total = 0
    if make_float:
        first = float(first)
        second = float(second)
    if operation == 'add':
        total = first + second
    elif operation == 'divide':
        total = first / second
    elif operation == 'multiply':
        total = first * second
    elif operation == 'subtract':
        total = first - second
    if message == None:
        return f"The result is {total}"
    return f"{message} {total}"
print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4))
print(calculate(make_float=True, operation='divide', first=3.5, second=5))

"""
def calculate(**kwargs):
    operation_lookup = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
    }
    is_float = kwargs.get('make_float', False)
    operation_value = operation_lookup[kwargs.get('operation', '')]
    if is_float:
        final = "{} {}".format(kwargs.get('message','The result is'), float(operation_value))
    else:
        final = "{} {}".format(kwargs.get('message','The result is'), int(operation_value))
    return final
    """