##    Python codesnippets - Wrapper/proxy pattern with function decorator
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
# Feature 97
#

"""
Wrapper/proxy pattern with function decorator
=============================================

:py:mod:`codesnippets.feature97`
--------------------------------

The decorator adds a wrapper around the real function call which happens inside the wrapper itself:

.. code-block:: Python

    def decorator(func):
        \"""decorator function\"""
        print(f"	-> inside decorator function...")
        calls = 0
        print(f"	-> inside decorator of function {a_func.__name__}()")
        def wrapper(*args):
            \"""wrapper function inside the decorator\"""
            nonlocal calls
            calls += 1
            print(f"	-> inside the wrapper function calling {a_func.__name__}()"
                  f" for the {calls} time")
            a_func(*args)
        return wrapper

>>> @decorator
    def my_func(param_a,param_b):
        \"""my decorated function\"""
        print(f"	-> inside my function...")
	-> inside decorator of function my_func()

When ``my_func(a,b)`` is called, it is the ``wrapper()`` that is actually called!

>>> my_func(1,2)
	-> inside the wrapper function calling my_func() for the 1 time
	-> inside my function...

>>> my_func(1,2)
	-> inside the wrapper function calling my_func() for the 2 time
	-> inside my function...

Works for different functions too:

>>> @decorator
    def your_func(param_a,param_b):
        \"""my decorated function\"""
        print(f"	-> inside your function...")
	-> inside decorator of function your_func()

>>> your_func(1,2)
	-> inside the wrapper function calling your_func() for the 1 time
	-> inside your function...

>>> your_func(1,2)
	-> inside the wrapper function calling your_func() for the 2 time
	-> inside your function...
"""

def feature97():
    """Wrapper/proxy pattern with function decorator"""
    print('Wrapper/proxy pattern with function decorator')
    print('=============================================\n')
    print(':py:mod:`codesnippets.feature97`')
    print('--------------------------------\n')
    print("The decorator adds a wrapper around the real function call which happens inside"
          " the wrapper itself:\n")
    print('.. code-block:: Python\n')
    print("""    def decorator(func):
        \\\"""decorator function\\\"""
        print(f"\t-> inside decorator function...")
        calls = 0
        print(f"\t-> inside decorator of function {a_func.__name__}()")
        def wrapper(*args):
            \\\"""wrapper function inside the decorator\\\"""
            nonlocal calls
            calls += 1
            print(f"\t-> inside the wrapper function calling {a_func.__name__}()"
                  f" for the {calls} time")
            a_func(*args)
        return wrapper
          """)
    def decorator(a_func):
        """decorator function"""
        calls = 0
        print(f"\t-> inside decorator of function {a_func.__name__}()")
        def wrapper(*args):
            """wrapper function inside the decorator"""
            nonlocal calls
            calls += 1
            print(f"\t-> inside the wrapper function calling {a_func.__name__}()"
                  f" for the {calls} time")
            a_func(*args)
        return wrapper
    print(""">>> @decorator
    def my_func(param_a,param_b):
        \\\"""my decorated function\\\"""
        print(f"\t-> inside my function...")""")
    @decorator
    def my_func(param_a,param_b):
        """my decorated function"""
        print(f"\t-> inside my function...")
    print()
    print("When ``my_func(a,b)`` is called, it is the ``wrapper()`` that is actually called!")
    print()
    print(">>> my_func(1,2)")
    my_func(1,2)
    print()
    print(">>> my_func(1,2)")
    my_func(1,2)
    print()
    print("Works for different functions too:\n")
    print(""">>> @decorator
    def your_func(param_a,param_b):
        \\\"""my decorated function\\\"""
        print(f"\t-> inside your function...")""")
    @decorator
    def your_func(param_a,param_b):
        """my decorated function"""
        print(f"\t-> inside your function...")
    print()
    print(">>> your_func(1,2)")
    your_func(1,2)
    print()
    print(">>> your_func(1,2)")
    your_func(1,2)
    print(80*'-')
