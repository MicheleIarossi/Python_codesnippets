##    Python codesnippets - lambda functions, map() and list comprehension
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
# Feature 47
#

"""

``lambda`` functions, ``map()`` and ``list`` comprehension
==========================================================

:py:mod:`codesnippets.feature47`
--------------------------------

The combination of ``lambda`` function plus ``map()`` for creating a ``list`` represents
an alternative to the ``list`` comprehension pattern.

The following expressions are equivalent:

>>> [x_var**2 for x_var in range(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

>>> list(map(lambda x_var: x_var**2, range(10))
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

The ``filter()`` built-in function is used if filtering is required.\n
The following expressions are equivalent as well:

>>> [x_var**2 for x_var in range(10)] if x_var%2 != 0
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

>>> list(map(lambda x_var: x_var**2, filter(lambda x_var: x_var!=0, range(10))))
[1, 4, 9, 16, 25, 36, 49, 64, 81]

.. seealso:: :doc:`List comprehension<feature8>`,
	:doc:`map() on the elements of a list<feature9>`
"""

def feature47():
    """Lambda functions, map() and list comprehension"""
    print('``lambda`` functions, ``map()`` and ``list`` comprehension')
    print('==========================================================\n')
    print(':py:mod:`codesnippets.feature47`')
    print('--------------------------------\n')
    print('The combination of ``lambda`` function plus ``map()`` '
          'for creating a ``list`` represents\nan alternative to '
          'the ``list`` comprehension pattern.\n')
    print('The following expressions are equivalent:\n')
    print('>>> [x_var**2 for x_var in range(10)]')
    print([x_var**2 for x_var in range(10)])
    print('\n>>> list(map(lambda x_var: x_var**2, range(10))')
    print(list(map(lambda x_var: x_var**2, range(10))))
    print('\nThe ``filter()`` built-in function is used if filtering is required.\\n')
    print('The following expressions are equivalent as well:\n')
    print('>>> [x_var**2 for x_var in range(10)] if x_var%2 != 0')
    print([x_var**2 for x_var in range(10)])
    print('\n>>> list(map(lambda x_var: x_var**2, filter(lambda x_var: x_var!=0, range(10))))')
    print(list(map(lambda x_var: x_var**2, filter(lambda x_var: x_var!=0, range(10)))))
    print('\n.. seealso:: :doc:`List comprehension<feature8>`,'
          '\n\t:doc:`map() on the elements of a list<feature9>`')
    print(80*'-')