""" Doctest """
# python -m doctest -v filename.py

def add(a,b):
    """ 
    >>> add(2,3)
    5
    >>> add(8,2)
    10
    """
    return a + b

def double(values):
    # new feature 
    # first write the tests 
    """ 
    double the values in a list

    >>> double([1,2,3,4])
    [2, 4, 6, 8]

    >>> double([])
    []

    >>> double(['a', 'b','c'])
    ['aa', 'bb', 'cc']

    >>> double([True,None])
    Traceback (most recent call last): 
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    # Write the minimal amount of code necessary to make the test pass
    return([2*val for val in values]) # refactor if necessary

if __name__ == "__main__":
    import doctest
    # doctest.testmod()
    doctest.testmod(verbose=True)