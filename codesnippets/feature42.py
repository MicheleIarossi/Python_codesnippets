##    Python codesnippets - Recursion
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
# Feature 42
#

"""
Recursion
=========

:py:mod:`codesnippets.feature42`
--------------------------------

This function sums up all the elements in a list and
in its contained sublists by recursive calls:

.. code-block:: Python

    def sumtree(a_list):
        print(a_list)
        total = 0
        # For each item at this level
        for elem in a_list:
            if not isinstance(x, list):
                # Add numbers directly
                total += elem
            else:
                # Recur for sublists
                total += sumtree(elem)
        return total

>>> lst = [1, [2, [3, 4], 5], 6, [7, 8]]          # Arbitrary nesting

>>> sumtree(lst)                                  # Prints 36
[1, [2, [3, 4], 5], 6, [7, 8]]
[2, [3, 4], 5]
[3, 4]
[7, 8]
36
"""

def sumtree(a_list):
    """sums up all the elements in a list and in its sublists"""
    print(a_list)
    total = 0
    # For each item at this level
    for elem in a_list:
        if not isinstance(elem, list):
            # Add numbers directly
            total += elem
        else:
            # Recur for sublists
            total += sumtree(elem)
    return total

def feature42():
    """Recursion"""
    print('Recursion')
    print('=========\n')
    print(':py:mod:`codesnippets.feature42`')
    print('--------------------------------\n')
    print('This function sums up all the elements in a list and')
    print('in its contained sublists by recursive calls:\n')
    print('.. code-block:: Python\n')
    print('    def sumtree(a_list):')
    print('        print(a_list)')
    print('        total = 0')
    print('        # For each item at this level')
    print('        for elem in a_list:')
    print('            if not isinstance(x, list):')
    print('                # Add numbers directly')
    print('                total += elem')
    print('            else:')
    print('                # Recur for sublists')
    print('                total += sumtree(elem)')
    print('        return total\n')
    print('>>> lst = [1, [2, [3, 4], 5], 6, [7, 8]]          # Arbitrary nesting\n')
    # Arbitrary nesting
    lst = [1, [2, [3, 4], 5], 6, [7, 8]]
    print('>>> sumtree(lst)                                  # Prints 36')
    # Prints 36
    print(sumtree(lst))
    print(80*'-')
