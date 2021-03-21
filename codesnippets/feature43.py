##    Python codesnippets - Avoiding recursive calls by depth-first scanning
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
# Feature 43
#

"""
Avoiding recursive calls by depth-first scanning
================================================

:py:mod:`codesnippets.feature43`
--------------------------------

This function sums up all the elements in a list and
in its contained sublists.
Sublists are scanned immediately (stacked) and then single elements are summed up.

.. code-block:: Python

    def sumtree(lst):
        # Depth-first, explicit stack
        total = 0
        # Start with copy of top level
        items = list(lst)
        while items:
            # Fetch/delete front item
            front = items.pop(0)
            if not isinstance(front, list):
                # Add numbers directly
                total += front
                print(front)
            else:
                # Prepend all in nested list
                items[:0] = front
        return total

>>> lst = [1, [2, [3, 4], 5], 6, [7, 8]]          # Arbitrary nesting

>>> sumtree(lst)                                  # Prints 36
1
2
3
4
5
6
7
8
36
"""

def sumtree(lst):
    # Depth-first, explicit stack
    """sums up all the elements in a list and in its sublists by depth-first scanning"""
    total = 0
    # Start with copy of top level
    items = list(lst)
    while items:
        # Fetch/delete front item
        front = items.pop(0)
        if not isinstance(front, list):
            # Add numbers directly
            total += front
            print(front)
        else:
            # Prepend all in nested list
            items[:0] = front
    return total

def feature43():
    """Avoiding recursive calls by depth-first scanning"""
    print('Avoiding recursive calls by depth-first scanning')
    print('================================================\n')
    print(':py:mod:`codesnippets.feature43`')
    print('--------------------------------\n')
    print('This function sums up all the elements in a list and')
    print('in its contained sublists.')
    print('Sublists are scanned immediately (stacked) and then single elements are summed up.\n')
    print('.. code-block:: Python\n')
    print('    def sumtree(lst):')
    print('        # Depth-first, explicit stack')
    print('        total = 0')
    print('        # Start with copy of top level')
    print('        items = list(lst)')
    print('        while items:')
    print('            # Fetch/delete front item')
    print('            front = items.pop(0)')
    print('            if not isinstance(front, list):')
    print('                # Add numbers directly')
    print('                total += front')
    print('                print(front)')
    print('            else:')
    print('                # Prepend all in nested list')
    print('                items[:0] = front')
    print('        return total\n')
    print('>>> lst = [1, [2, [3, 4], 5], 6, [7, 8]]          # Arbitrary nesting\n')
    # Arbitrary nesting
    lst = [1, [2, [3, 4], 5], 6, [7, 8]]
    print('>>> sumtree(lst)                                  # Prints 36')
    # Prints 36
    print(sumtree(lst))
    print(80*'-')
