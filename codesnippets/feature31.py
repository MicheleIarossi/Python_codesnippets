##    Python codesnippets - The LEGB rule (nested scopes)
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
The LEGB rule (nested scopes)
=============================

:py:mod:`codesnippets.feature31`
--------------------------------

Remember that LEGB = Local, Enclosing, Global(Module), Built-in.

Given the following code:

.. code-block:: Python

    global_counter = 100                # global variable at module level

    def func1():
        global_counter = 200            # shadows the global variable
        def func2():
            print(global_counter)       # gets global_counter from the enclosing scope
        func2()

In the function ``func1`` the local ``global_counter`` variable shadows the global
``global_counter`` one, and the function ``func2`` gets the global counter
from the enclosing scope.

>>> func1()
200
"""

# global variable at module level
global_counter = 100

def func1():
    """shadows the global variable"""
    # Shadows the global variable
    global_counter = 200
    def func2():
        """prints the local variable"""
        # gets global_counter from the enclosing scope
        print(global_counter)
    func2()

def feature31():
    """LEGB rule (nested scopes)"""
    print('The LEGB rule (nested scopes)')
    print('=============================\n')
    print(':py:mod:`codesnippets.feature31`')
    print('--------------------------------\n')
    print('Remember that LEGB = Local, Enclosing, Global(Module), Built-in.\n')
    print('Given the following code:\n')
    print('.. code-block:: Python\n')
    print('    global_counter = 100                # global variable at module level\n')
    print('    def func1():')
    print('        global_counter = 200            # shadows the global variable')
    print('        def func2():')
    print('            print(global_counter)       # gets global_counter from the enclosing scope')
    print('        func2()')
    print('\nIn the function ``func1`` the local ``global_counter`` variable shadows the global\n'
          '``global_counter`` one, and the function ``func2`` gets the global '
          'counter\nfrom the enclosing scope.\n')
    print('>>> func1()')
    func1()
    print(80*'-')