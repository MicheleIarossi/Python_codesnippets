##    Python codesnippets - Shallow and deep copy
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
# Feature 14
#

"""
Shallow and deep copy
=====================

:py:mod:`codesnippets.feature14`
--------------------------------

>>> import copy

>>> lst1 = [1,2,3]
>>> lst2 = [4,5,lst1]           # lst2 has a reference to lst1
>>> lst3 = lst2                 # lst3 points to lst2
>>> lst4 = lst2.copy()          # lst4 is a shallow copy of lst2, still points to lst1
>>> lst5 = copy.deepcopy(lst2)  # lst5 is a deep copy of lst2, no more references

>>> lst1[0] = 9                 # modify lst1
>>> lst2[0] = 7                 # modify lst2

>>> lst1                        # first element has changed
[9, 2, 3]

>>> lst2                        # first element has changed, as well as lst1 reference
[7, 5, [9, 2, 3]]

>>> lst3                        # points to lst2, no copy!
[7, 5, [9, 2, 3]]

.. note:: ``lst4`` is a shallow copy of ``lst2``, it includes a copy of the reference to ``lst1`` whose content has now changed

>>> lst4                        # shallow copy of the original lst2, includes copy of lst1 reference!
[4, 5, [9, 2, 3]]

>>> lst5                        # deep copy of original lst2, includes original values of lst1!
[4, 5, [1, 2, 3]]
"""

import copy

def feature14():
    """Shallow and deep copy"""
    print('Shallow and deep copy')
    print('=====================\n')
    print(':py:mod:`codesnippets.feature14`')
    print('--------------------------------\n')
    print(">>> import copy")
    print("\n>>> lst1 = [1,2,3]")
    lst1 = [1,2,3]
    print(">>> lst2 = [4,5,lst1]           # lst2 has a reference to lst1")
    lst2 = [4,5,lst1]
    print(">>> lst3 = lst2                 # lst3 points to lst2")
    lst3 = lst2
    print(">>> lst4 = lst2.copy()          # lst4 is a shallow copy of lst2, still points to lst1")
    lst4 = lst2.copy()
    print(">>> lst5 = copy.deepcopy(lst2)  # lst5 is a deep copy of lst2, no more references")
    lst5 = copy.deepcopy(lst2)
    print("\n>>> lst1[0] = 9                 # modify lst1")
    lst1[0] = 9
    print(">>> lst2[0] = 7                 # modify lst2")
    lst2[0] = 7
    print("\n>>> lst1                        # first element has changed")
    print(lst1)
    print("\n>>> lst2                        # first element has changed, as well as lst1 "
          "reference")
    print(lst2)
    print("\n>>> lst3                        # points to lst2, no copy!")
    print(lst3)
    print('\n.. note:: ``lst4`` is a shallow copy of ``lst2``, it includes a copy '
          'of the reference to ``lst1`` whose content has now changed')
    print("\n>>> lst4                        # shallow copy of the original lst2, includes copy "
        "of lst1 reference!")
    print(lst4)
    print("\n>>> lst5                        # deep copy of original lst2, includes original values"
          "of lst1!")
    print(lst5)
    print(80*'-')
