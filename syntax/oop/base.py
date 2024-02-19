class Foo:

    """
    Public modifiers allow the class members to be accessed 
    from anywhere in the program. 
    Protected modifiers allow the class members 
    to be accessed only from within 
    the class or its subclasses.
    A private class in Python is a class 
    that is not meant to be instantiated 
    or accessed from outside the module where it is defined.
    """
    x = 10 # public attribute
    _y = 20 # protected attribute
    __z = 30 # private attribute
