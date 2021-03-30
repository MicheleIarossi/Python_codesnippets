##    Python codesnippets - Decorator for a method of a class
##    Copyright (C) 2021  Michele Iarossi (micheleiarossi@gmail.com)
##
##    This program is free software: you can redistribute it and/or modify
##    it under the terms of the GNU General Public License as published by
##    the Free Software Foundation, either version 3 of the License, or
##    (at your option) any later version.
##
##    This program is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##    GNU General Public License for more details.
##
##    You should have received a copy of the GNU General Public License
##    along with this program.  If not, see <https://www.gnu.org/licenses/>.

#
# Feature 100
#

"""
Decorator for a method of a ``class``
=====================================

:py:mod:`codesnippets.feature100`
---------------------------------

This is best done with a function decorator that uses a wrapper:

.. code-block:: Python

    def decorator(a_func):
        \"""decorator function for a method of a class\"""
        print(f"	-> inside decorator of function {repr(a_func.__name__)}")
        calls = 0
        def wrapper(*args):
            \"""wrapper function inside the decorator\"""
            nonlocal calls
            calls += 1
            print(f"	-> inside the wrapper calling method {repr(a_func.__name__)}"
                  f" for the {repr(calls)} time")
            a_func(args[0],*args[1,:])
        return wrapper

>>> class MyClass:
        \"""a class\"""
        def __init__(self):
            print("	-> inside constructor of 'MyClass'...")
        @decorator
        def a_method(self,param_1,param_2):
            \"""a method\"""
            print(f"	-> inside a_method({param_1},{param_2}) of "
                  f"instance {repr(self._name)}...")
	-> inside decorator of function 'a_method'

Creation of an instance:

>>> obj = MyClass('John')
	-> inside constructor of MyClass('John')...

Method call:

>>> obj.a_method(7,8)
	-> inside the wrapper calling method 'a_method' for the 1 time
	-> inside a_method(7,8) of instance 'John'...

>>> obj.a_method(7,8)
	-> inside the wrapper calling method 'a_method' for the 2 time
	-> inside a_method(7,8) of instance 'John'...

This DOESN'T work on different instances of the same class, because
the decorator function is always the same and called once on class definition!

>>> obj_2 = MyClass('Mike')
	-> inside constructor of MyClass('Mike')...

Method call:

>>> obj_2.a_method(3,4)
	-> inside the wrapper calling method 'a_method' for the 3 time
	-> inside a_method(3,4) of instance 'Mike'...

>>> obj_2.a_method(3,4)
	-> inside the wrapper calling method 'a_method' for the 4 time
	-> inside a_method(3,4) of instance 'Mike'...

.. seealso:: :doc:`Wrapper/proxy pattern with function decorator<feature98>`
"""

def feature100():
    """Decorator for a method of a class"""
    print('Decorator for a method of a ``class``')
    print('=====================================\n')
    print(':py:mod:`codesnippets.feature100`')
    print('---------------------------------\n')
    print("This is best done with a function decorator that uses a wrapper:\n")
    print('.. code-block:: Python\n')
    print("""    def decorator(a_func):
        \\\"""decorator function for a method of a class\\\"""
        print(f"\t-> inside decorator of function {repr(a_func.__name__)}")
        calls = 0
        def wrapper(*args):
            \\\"""wrapper function inside the decorator\\\"""
            nonlocal calls
            calls += 1
            print(f"\t-> inside the wrapper calling method {repr(a_func.__name__)}"
                  f" for the {repr(calls)} time")
            a_func(args[0],*args[1,:])
        return wrapper
          """)
    def decorator(a_func):
        """decorator function for a method of a class"""
        print(f"\t-> inside decorator of function {repr(a_func.__name__)}")
        calls = 0
        def wrapper(*args):
            """wrapper function inside the decorator"""
            nonlocal calls
            calls += 1
            print(f"\t-> inside the wrapper calling method {repr(a_func.__name__)}"
                  f" for the {repr(calls)} time")
            a_func(args[0],*args[1:])
        return wrapper
    print(""">>> class MyClass:
        \\\"""a class\\\"""
        def __init__(self):
            print("\t-> inside constructor of 'MyClass'...")
        @decorator
        def a_method(self,param_1,param_2):
            \\\"""a method\\\"""
            print(f"\t-> inside a_method({param_1},{param_2}) of "
                  f"instance {repr(self._name)}...") """)
    class MyClass:
        """a class"""
        def __init__(self,name):
            self._name = name
            print(f"\t-> inside constructor of MyClass({repr(name)})...")
        @decorator
        def a_method(self,param_1,param_2):
            """a method"""
            print(f"\t-> inside a_method({repr(param_1)},{repr(param_2)}) of "
                  f"instance {repr(self._name)}...")
    print("\nCreation of an instance:\n")
    print(">>> obj = MyClass('John')")
    obj = MyClass("John")
    print()
    print("Method call:\n")
    print(">>> obj.a_method(7,8)")
    obj.a_method(7,8)
    print()
    print(">>> obj.a_method(7,8)")
    obj.a_method(7,8)
    print()
    print("This DOESN'T work on different instances of the same class, because")
    print("the decorator function is always the same and called once on class definition!\n")
    print(">>> obj_2 = MyClass('Mike')")
    obj_2 = MyClass("Mike")
    print()
    print("Method call:\n")
    print(">>> obj_2.a_method(3,4)")
    obj_2.a_method(3,4)
    print()
    print(">>> obj_2.a_method(3,4)")
    obj_2.a_method(3,4)
    print('\n.. seealso:: :doc:`Wrapper/proxy pattern with function decorator<feature101>`\n')
    print(80*'-')
