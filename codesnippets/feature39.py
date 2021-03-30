##    Python codesnippets - Arguments matched by default values, by position and by name
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
# Feature 39
#

"""
Arguments matched by default values, by position and by name
============================================================

:py:mod:`codesnippets.feature39`
--------------------------------

The following function assigns default values to its parameters:

.. code-block:: Python

    def func(a_value=44,b_value=55,c_value=66):
        print(a_value,b_value,c_value)

If no arguments are provided, the default values are used:

>>> func()  # uses default values
(44, 55, 66)

If no special matching is used, position is the normal matching mode, where
arguments are matched from left to right:

>>> func(111,222,333)  # match by position
(111, 222, 333)

If keyword arguments are used, the matching is done by name in any order:

>>> func(c_value=333,b_value=222,a_value=111)  # match by name
(111, 222, 333)

.. note:: Positional arguments must precede any keyword arguments.
"""

def func(a_value=44,b_value=55,c_value=66):
    """default values assigned to its parameters"""
    print((a_value,b_value,c_value))


def feature39():
    """Arguments matched by position and by name"""
    print('Arguments matched by default values, by position and by name')
    print('============================================================\n')
    print(':py:mod:`codesnippets.feature39`')
    print('--------------------------------\n')
    print('The following function assigns default values to its parameters:\n')
    print('.. code-block:: Python\n')
    print('    def func(a_value=44,b_value=55,c_value=66):')
    print('        print(a_value,b_value,c_value)\n')
    print('If no arguments are provided, the default values are used:\n')
    print('>>> func()  # uses default values')
    func()  # default values
    print('\nIf no special matching is used, position is the normal matching mode, where')
    print('arguments are matched from left to right:\n')
    print('>>> func(111,222,333)  # match by position')
    func(111,222,333)  # match by position
    print('\nIf keyword arguments are used, the matching is done by name in any order:\n')
    print('>>> func(c_value=333,b_value=222,a_value=111)  # match by name')
    func(c_value=333,b_value=222,a_value=111)  # match by name
    print('\n.. note:: Positional arguments must precede any keyword arguments.')
    print(80*'-')