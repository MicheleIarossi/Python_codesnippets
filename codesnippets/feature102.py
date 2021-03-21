##    Python codesnippets - Decorator arguments
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
# Feature 102
#

"""
Decorator arguments
===================

:py:mod:`codesnippets.feature102`
---------------------------------

The arguments are passed to the outer decorator, which needs to return an
inner decorator that actually takes a function:

.. code-block:: Python

    def decorator_1(param_a,param_b):
        \"""decorator function\"""
        print(f"	-> inside decorator_1({param_a},{param_b})...")
        def decorator_2(a_func):
            print("inside decorator_2...")
            def wrapper(*args):
                \"""wrapper function inside decorator_2\"""
                print("	-> inside the wrapper function...")
                args = tuple(param_a*x+param_b for x in args)
                a_func(*args)
            return wrapper
        return decorator_2

>>> @decorator_1(3,4)
    def myfunc(param_a,param_b):
        print(f"	-> inside my function...")
	-> inside decorator_1(3,4)...
	-> inside decorator_2...

This is equivalent to:

>>> def myfunc(param_a,param_b):
        \"""my decorated function\"""
        print(f"	-> inside my function({param_a},{param_b})...")

>>> myfunc = decorator_1(3,4)(myfunc)

When ``myfunc(param_a,param_b)`` is called, it is the ``wrapper()``
that is actually called,
because the wrapper is returned by the ``decorator_2``.
The wrapper uses the parameters of ``decorator_1`` for changing the function
arguments to be used for the actual function call:

>>> myfunc(2,3)
inside the wrapper function...
	-> inside myfunc(10,13)...
"""

def feature102():
    """Decorator arguments"""
    print('Decorator arguments')
    print('===================\n')
    print(':py:mod:`codesnippets.feature102`')
    print('---------------------------------\n')
    print('The arguments are passed to the outer decorator, which needs to return an')
    print('inner decorator that actually takes a function:\n')
    print('.. code-block:: Python\n')
    print("""    def decorator_1(param_a,param_b):
        \\\"""decorator function\\\"""
        print(f"\t-> inside decorator_1({param_a},{param_b})...")
        def decorator_2(a_func):
            print("inside decorator_2...")
            def wrapper(*args):
                \\\"""wrapper function inside decorator_2\\\"""
                print("\t-> inside the wrapper function...")
                args = tuple(a*x+b for x in args)         
                a_func(*args)
            return wrapper
        return decorator_2
          """)
    def decorator_1(param_a,param_b):
        """decorator function"""
        print(f"\t-> inside decorator_1({param_a},{param_b})...")
        def decorator_2(a_func):
            print("\t-> inside decorator_2...")
            def wrapper(*args):
                """wrapper function inside decorator_2"""
                print("inside the wrapper function...")
                args = tuple(param_a*x+param_b for x in args)
                a_func(*args)
            return wrapper
        return decorator_2
    print(""">>> @decorator_1(3,4)
    def myfunc(a,b):
        print(f"\t-> inside my function...")""")
    @decorator_1(3,4)
    def myfunc(param_a,param_b):
        """my decorated function"""
        print(f"\t-> inside myfunc({param_a},{param_b})...")
    print()
    print("This is equivalent to:\n")
    print(""">>> def myfunc(param_a,param_b):
        \\\"""my decorated function\\\"""
        print(f"\t-> inside my function({param_a},{param_b})...") """)
    print()
    print(">>> myfunc = decorator_1(3,4)(myfunc)")
    print()
    print("When ``myfunc(param_a,param_b)`` is called, it is the ``wrapper()``"
          "\nthat is actually called,")
    print("because the wrapper is returned by the ``decorator_2``.")
    print("The wrapper uses the parameters of ``decorator_1`` for changing the function")
    print("arguments to be used for the actual function call:")
    print()
    print(">>> myfunc(2,3)")
    myfunc(2,3)
    print(80*'-')
