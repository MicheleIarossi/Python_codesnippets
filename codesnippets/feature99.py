##    Python codesnippets - Decorator implementation via classes
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
# Feature 99
#

"""
Decorator implementation via classes
====================================

:py:mod:`codesnippets.feature99`
--------------------------------

The following class implements a decorator by means of the ``__call__`` operator:

.. code-block:: Python

    class Decorator:
        \"""implements a decorator\"""
        def __init__(self,a_func):
            print(f"	-> inside Decorator.__init__() called on function {a_func.__name__}")
            self.func  = a_func
            self.calls = 0
        def __call__(self,*args):
            self.calls += 1
            print(f"	-> inside Decorator.__call__() calling {self.func.__name__}"
                  f" for the {self.calls} time")
            return self.func(*args)

This is the function to be decorated:

>>> @Decorator
    def my_func(param_a,param_b):
        \"""function to be decorated\"""
        print(f"	-> inside my_func({param_a},{param_b})...")
	-> inside Decorator.__init__() called on function my_func

When the decorator runs, the following happens:

>>> my_func = Decorator()

The function ``my_func`` gets assigned an instance of the class Decorator.

Now the function is called:

>>> my_func(6,4)
	-> inside Decorator.__call__() calling my_func for the 1 time
	-> inside my_func(6,4)...

>>> my_func(6,4)
	-> inside Decorator.__call__() calling my_func for the 2 time
	-> inside my_func(6,4)...

The function call triggers the ``__call__`` method of the instance bound to ``my_func()``

It works also for different functions because the decorator
runs again on any new function definition:

>>> @Decorator
    def your_func(param_a,param_b):
        print(f"	-> inside your_func({param_a},{param_b})...")
	-> inside Decorator.__init__() called on function your_func

>>> your_func(7,5)
	-> inside Decorator.__call__() calling your_func for the 1 time
	-> inside your_func(7,5)...

>>> my_func(6,4)
	-> inside Decorator.__call__() calling my_func for the 3 time
	-> inside my_func(6,4)...

>>> your_func(7,5)
	-> inside Decorator.__call__() calling your_func for the 2 time
	-> inside your_func(7,5)...

.. seealso:: :doc:`Operator overloading: __call__ , __len__ , __bool__<feature69>`
"""

def feature99():
    """Decorator implementation via classes"""
    print('Decorator implementation via classes')
    print('====================================\n')
    print(':py:mod:`codesnippets.feature99`')
    print('--------------------------------\n')
    print("The following class implements a decorator by means of the ``__call__`` operator:\n")
    print('.. code-block:: Python\n')
    print("""    class Decorator:
        \\\"""implements a decorator\\\"""
        def __init__(self,a_func):
            print(f"\t-> inside Decorator.__init__() called on function {a_func.__name__}")
            self.func  = a_func
            self.calls = 0
        def __call__(self,*args):
            self.calls += 1
            print(f"\t-> inside Decorator.__call__() calling {self.func.__name__}"
                  f" for the {self.calls} time")
            return self.func(*args)
        """)
    class Decorator:
        """implements a decorator"""
        def __init__(self,a_func):
            print(f"\t-> inside Decorator.__init__() called on function {a_func.__name__}")
            self.func = a_func
            self.calls = 0
        def __call__(self,*args):
            self.calls += 1
            print(f"\t-> inside Decorator.__call__() calling {self.func.__name__}"
                  f" for the {self.calls} time")
            return self.func(*args)
    print("This is the function to be decorated:\n")
    print(""">>> @Decorator
    def my_func(param_a,param_b):
        \\\"""function to be decorated\\\"""
        print(f"\t-> inside my_func({param_a},{param_b})...")""")
    @Decorator
    def my_func(param_a,param_b):
        """function to be decorated"""
        print(f"\t-> inside my_func({param_a},{param_b})...")
    print()
    print("When the decorator runs, the following happens:\n")
    print(">>> my_func = Decorator()\n")
    print("The function ``my_func`` gets assigned an instance of the class Decorator.\n")
    print("Now the function is called:\n")
    print(">>> my_func(6,4)")
    my_func(6,4)
    print()
    print(">>> my_func(6,4)")
    my_func(6,4)
    print()
    print("The function call triggers the ``__call__`` method of the"
          " instance bound to ``my_func()``")
    print()
    print("It works also for different functions because the decorator")
    print("runs again on any new function definition:\n")
    print(""">>> @Decorator
    def your_func(param_a,param_b):
        print(f"\t-> inside your_func({param_a},{param_b})...")""")
    @Decorator
    def your_func(param_a,param_b):
        """function to be decorated"""
        print(f"\t-> inside your_func({param_a},{param_b})...")
    print()
    print(">>> your_func(7,5)")
    your_func(7,5)
    print()
    print(">>> my_func(6,4)")
    my_func(6,4)
    print()
    print(">>> your_func(7,5)")
    your_func(7,5)
    print('\n.. seealso:: :doc:`Operator overloading: __call__ , __len__ , __bool__<feature69>`')
    print(80*'-')