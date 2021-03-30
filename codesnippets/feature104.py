##    Python codesnippets - Call tracer with a function decorator
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
# Feature 104
#

"""
Call tracer with a function decorator
=====================================

:py:mod:`codesnippets.feature104`
---------------------------------

The ``wrapper()`` is the actual function that gets called after decoration:

.. code-block:: Python

    def func_tracer(a_func):
        \"""decorator for tracing the number of calls\"""
        print(f"	-> decorating {repr(a_func.__name__)}")
        calls = 0
        def wrapper(*args,**kwargs):
            \"""the real function that gets called\"""
            nonlocal calls
            calls =+ 1
            print(f"total function calls of {repr(a_func.__name__)}: {calls}")
            return a_func(*arg,**kwargs)
        return wrapper

>>> @func_tracer
    def my_func(param_a,param_b):
        \"""my decorated function\"""
        print("	-> inside my function...")
	-> decorating 'my_func'

When ``my_func(param_a,param_b)`` is called, it is the ``wrapper()`` that is actually called,
because the wrapper is returned by the ``func_tracer()`` decoration:

>>> my_func(2,3)
total function calls of 'my_func': 1
	-> inside myfunc(2,3)...

>>> my_func(6,7)
total function calls of 'my_func': 2
	-> inside myfunc(6,7)...

Works for different functions too:

>>> @func_tracer
    def your_func(a,b):
        \"""your decorated function\"""
        print(f"	-> inside your_func({a},{b})")
	-> decorating 'your_func'

>>> your_func(1,2)
total function calls of 'your_func': 1
	-> inside your_func(1,2)

>>> your_func(1,2)
total function calls of 'your_func': 2
	-> inside your_func(1,2)

.. seealso:: :doc:`Wrapper/proxy pattern with function decorator<feature98>`
"""

def feature104():
    """Call tracer with a function decorator"""
    print('Call tracer with a function decorator')
    print('=====================================\n')
    print(':py:mod:`codesnippets.feature104`')
    print('---------------------------------\n')
    print('The ``wrapper()`` is the actual function that gets called after decoration:\n')
    print('.. code-block:: Python\n')
    print("""    def func_tracer(a_func):
        \\\"""decorator for tracing the number of calls\\\"""
        print(f"\t-> decorating {repr(a_func.__name__)}")
        calls = 0
        def wrapper(*args,**kwargs):
            \\\"""the real function that gets called\\\"""
            nonlocal calls
            calls =+ 1
            print(f"total function calls of {repr(a_func.__name__)}: {calls}")
            return a_func(*arg,**kwargs)
        return wrapper
        """)
    def func_tracer(a_func):
        """decorator for tracing the number of calls"""
        print(f"\t-> decorating {repr(a_func.__name__)}")
        calls = 0
        def wrapper(*args,**kwargs):
            """the real function that gets called"""
            nonlocal calls
            calls += 1
            print(f"total function calls of {repr(a_func.__name__)}: {calls}")
            return a_func(*args,**kwargs)
        return wrapper
    print(""">>> @func_tracer
    def my_func(param_a,param_b):
        \\\"""my decorated function\\\"""
        print("\t-> inside my function...")""")
    @func_tracer
    def my_func(param_a,param_b):
        """my decorated function"""
        print(f"\t-> inside myfunc({param_a},{param_b})...")
    print()
    print("When ``my_func(param_a,param_b)`` is called, it is the ``wrapper()`` that is"
          " actually called,")
    print("because the wrapper is returned by the ``func_tracer()`` decoration:\n")
    print(">>> my_func(2,3)")
    my_func(2,3)
    print()
    print(">>> my_func(6,7)")
    my_func(6,7)
    print()
    print("Works for different functions too:")
    print()
    print(""">>> @func_tracer
    def your_func(param_a,param_b):
        \\\"""your decorated function\\\"""
        print(f"\t-> inside your_func({param_a},{param_b})") """)
    @func_tracer
    def your_func(param_a,param_b):
        """your decorated function"""
        print(f"\t-> inside your_func({param_a},{param_b})")
    print()
    print(">>> your_func(1,2)")
    your_func(1,2)
    print()
    print(">>> your_func(1,2)")
    your_func(1,2)
    print('\n.. seealso:: :doc:`Wrapper/proxy pattern with function decorator<feature100>`')
    print(80*'-')