##    Python codesnippets - Simulating output parameters in a function call
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
# Feature 38
#

"""
Simulating output parameters in a function call
===============================================

:py:mod:`codesnippets.feature38`
--------------------------------

Input parameters are always passed by assignment. Immutable objects
cannot be changed inside the function, but multiple new values
can be returned by the ``return`` statement.

.. code-block:: Python

    def assign_new_values(a_value,b_value,c_value):
        a_value, b_value, c_value = 11, 22, 33
        return a_value, b_value, c_value

>>> a_value, b_value, c_value = 1, 2, 3

>>> a_value, b_value, c_value = assign_new_values(a_value,b_value,c_value)

>>> a_value,b_value,c_value
(11, 22, 33)
"""

def assign_new_values(a_value,b_value,c_value):
    """shadows its input parameters"""
    a_value, b_value, c_value = 11, 22, 33
    return a_value, b_value, c_value


def feature38():
    """Simulating output parameters in a function call"""
    print('Simulating output parameters in a function call')
    print('===============================================\n')
    print(':py:mod:`codesnippets.feature38`')
    print('--------------------------------\n')
    print('Input parameters are always passed by assignment. Immutable objects')
    print('cannot be changed inside the function, but multiple new values')
    print('can be returned by the ``return`` statement.\n')
    print('.. code-block:: Python\n')
    print('    def assign_new_values(a_value,b_value,c_value):')
    print('        a_value, b_value, c_value = 11, 22, 33')
    print('        return a_value, b_value, c_value')
    print()
    print('>>> a_value, b_value, c_value = 1, 2, 3\n')
    a_value, b_value, c_value = 1, 2, 3
    print('>>> a_value, b_value, c_value = assign_new_values(a_value,b_value,c_value)\n')
    a_value, b_value, c_value = assign_new_values(a_value,b_value,c_value)
    print('>>> a_value,b_value,c_value')
    print((a_value,b_value,c_value))
    print(80*'-')