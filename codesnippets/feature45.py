##    Python codesnippets - Avoiding calls by breadth-first scanning
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
# Feature 45
#

"""
Avoiding recursive calls by breadth-first scanning
==================================================

:py:mod:`codesnippets.feature45`
--------------------------------

This functions sums up all the elements in a list and
in its contained sublists.
Single elements are summed up first and sublists are scanned later (queued).

.. code-block:: Python

    def sumtree(lst):
        # Breadth-first, explicit queue
        total = 0
        # Start with copy of top level
        items = list(lst)
        while items:
            # Fetch/delete front item
            front = items.pop(0)
            if not isinstance(front, list):
                # Add numbers directly
                total += front
            else:
                # Append all in nested list
                items.extend(front)
        return total

>>> lst = [1, [2, [3, 4], 5], 6, [7, 8]]               # Arbitrary nesting

>>> sumtree(lst)                                       # Prints 36
1
6
2
5
7
8
3
4
36
"""

def sumtree(lst):
    # Breadth-first, explicit queue
    """sums up all the elements in a list and in its sublists by breadth-first scanning"""
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
            # <== Append all in nested list
            items.extend(front)
    return total

def feature45():
    """Avoiding recursive calls by breadth-first scanning"""
    print('Avoiding recursive calls by breadth-first scanning')
    print('==================================================\n')
    print(':py:mod:`codesnippets.feature45`')
    print('--------------------------------\n')
    print('This functions sums up all the elements in a list and')
    print('in its contained sublists.')
    print('Single elements are summed up first and sublists are scanned later (queued).\n')
    print('.. code-block:: Python\n')
    print('    def sumtree(lst):')
    print('        # Breadth-first, explicit queue')
    print('        total = 0')
    print('        # Start with copy of top level')
    print('        items = list(lst)')
    print('        while items:')
    print('            # Fetch/delete front item')
    print('            front = items.pop(0)')
    print('            if not isinstance(front, list):')
    print('                # Add numbers directly')
    print('                total += front')
    print('            else:')
    print('                # Append all in nested list')
    print('                items.extend(front)')
    print('        return total\n')
    print('>>> lst = [1, [2, [3, 4], 5], 6, [7, 8]]          # Arbitrary nesting\n')
    # Arbitrary nesting
    lst = [1, [2, [3, 4], 5], 6, [7, 8]]
    print('>>> sumtree(lst)                                  # Prints 36')
    # Prints 36
    print(sumtree(lst))
    print(80*'-')