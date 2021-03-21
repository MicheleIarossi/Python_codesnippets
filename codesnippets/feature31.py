##    Python codesnippets - How to avoid nested scopes
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
# Feature 31
#

"""
How to avoid nested scopes
==========================

:py:mod:`codesnippets.feature31`
--------------------------------

Remember that flat is better than nested!

Given the function definitions below:

.. code-block:: Python

    def func1():
        global_var = 200 # Shadows the global variable
        func2(global_var)

    def func2(x_value):
        # prints 200
        print(x_value)

Forward referencing is used which is valid code,
as long as the function ``func2`` is defined before the function ``func1`` is called.

.. note:: Code inside a ``def`` is never evaluated until the function is called.

>>> global_var = 100 # global variable at module level

>>> func1()
200

The local variable ``global_var`` inside the function ``func1`` shadows the global one, but the
function ``func2`` gets the value of the local global counter from its parameter istead of
fetching it from a nested scope.

.. seealso:: :doc:`The LEGB rule (nested scopes) <feature30>`
"""

# global variable at module level
global_var = 100

def func1():
    """shadows the global variable"""
    # Shadows the global variable
    global_var = 200
    # The local variable is passed along
    func2(global_var)

def func2(x_value):
    """prints its parameter"""
    # prints 200
    print(x_value)

def feature31():
    """How to avoid nested scopes"""
    print('How to avoid nested scopes')
    print('==========================\n')
    print(':py:mod:`codesnippets.feature31`')
    print('--------------------------------\n')
    print('Remember that flat is better than nested!\n')
    print('Given the function definitions below:\n')
    print('.. code-block:: Python\n')
    print('    def func1():')
    print('        global_var = 200 # Shadows the global variable')
    print('        func2(global_var)\n')
    print('    def func2(x_value):')
    print('        # prints 200')
    print('        print(x_value)\n')
    print('Forward referencing is used which is valid code,')
    print("as long as the function ``func2`` is defined before the function ``func1`` is called.\n")
    print(".. note:: Code inside a ``def`` is never evaluated until the function is called.\n")
    print('>>> global_var = 100 # global variable at module level\n')
    print('>>> func1()')
    func1()
    print('\nThe local variable ``global_var`` inside the function ``func1`` '
          'shadows the global one, but the\nfunction ``func2`` gets the value '
          'of the local global counter from its parameter istead of\nfetching it '
          'from a nested scope.')
    print('\n.. seealso:: :doc:`The LEGB rule (nested scopes) <feature30>`')
    print(80*'-')
