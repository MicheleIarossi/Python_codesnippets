##    Python codesnippets - Side effects in assignments
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
# Feature 18
#

"""
Side effects in assignments
===========================

:py:mod:`codesnippets.feature18`
--------------------------------

Side effect in multiple target assignment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Here both variables point to the same empty list!

>>> a_lst = b_lst = []
>>> b_lst.append(32)

>>> a_lst, b_lst   # both variables change!
([32], [32])

Side effects in augmented assignments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Difference between concatenation and in-place change:

>>> a_lst = [1, 2]
>>> b_lst = a_lst

When concatenation is used, a new object is created:

>>> a_lst = a_lst + [3, 4]   # concatenation makes a new object!

>>> a_lst, b_lst             # b_lst does not change
([1, 2, 3, 4], [1, 2])

Another try:

>>> a_lst = [1, 2]
>>> b_lst = a_lst

When extension is used, in-place change happens:

>>> a_lst += [3, 4]   # this calls l.extend([3,4])

>>> a_lst, b_lst      # b_lst changes too!
([1, 2, 3, 4], [1, 2, 3, 4])
"""

def feature18():
    """Side effects in assignments"""
    print('Side effects in assignments')
    print('===========================\n')
    print(':py:mod:`codesnippets.feature18`')
    print('--------------------------------\n')
    print('Side effect in multiple target assignment:')
    print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n')
    print('Here both variables point to the same empty list!\n')
    print(">>> a_lst = b_lst = []")
    print(">>> b_lst.append(32)\n")
    print(">>> a_lst, b_lst   # both variables change!")
    a_lst = b_lst = []
    b_lst.append(32)
    print((a_lst, b_lst))
    print('\nSide effects in augmented assignments')
    print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n')
    print('Difference between concatenation and in-place change:\n')
    print(">>> a_lst = [1, 2]")
    print(">>> b_lst = a_lst")
    print('\nWhen concatenation is used, a new object is created:\n')
    print(">>> a_lst = a_lst + [3, 4]   # concatenation makes a new object!\n")
    print(">>> a_lst, b_lst             # b_lst does not change")
    a_lst = [1,2]
    b_lst = a_lst
    a_lst = a_lst + [3, 4]
    print((a_lst,b_lst))
    print('\nAnother try:\n')
    print(">>> a_lst = [1, 2]")
    print(">>> b_lst = a_lst")
    print('\nWhen extension is used, in-place change happens:\n')
    print(">>> a_lst += [3, 4]   # this calls l.extend([3,4])\n")
    print(">>> a_lst, b_lst      # b_lst changes too!")
    a_lst = [1,2]
    b_lst = a_lst
    a_lst += [3, 4]
    print((a_lst,b_lst))
    print(80*'-')
