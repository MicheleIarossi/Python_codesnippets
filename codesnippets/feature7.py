##    Python codesnippets - Changing lists in place
##    Copyright (C) 2021  Michele Iarossi  (micheleiarossi@gmail.com)
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
# Feature 7
#

"""
Changing lists in place
=======================

:py:mod:`codesnippets.feature7`
-------------------------------

Python ``lists`` are mutable, i.e. they can be changed in place:

>>> a_lst = [6,7,8,9]
>>> a_lst
[6, 7, 8, 9]

Insertion in front:

>>> a_lst[:0] = [0,1,2,3]
>>> a_lst
[0, 1, 2, 3, 6, 7, 8, 9]

Extension at the end:

>>> a_lst[len(l):] = [10,11,12,13]
>>> a_lst
[0, 1, 2, 3, 6, 7, 8, 9, 10, 11, 12, 13]

Insertion at position 4:

>>> a_lst[4:4] = [4,5]
>>> a_lst
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

Delete elements from position 4 to 5, same as ``del a_lst[4:6]``

>>> a_lst[4:6] = []
>>> a_lst
[0, 1, 2, 3, 6, 7, 8, 9, 10, 11, 12, 13]
"""

def feature7():
    """Changing lists in place"""
    print('Changing lists in place')
    print('=======================\n')
    print(':py:mod:`codesnippets.feature7`')
    print('-------------------------------\n')
    print("Python ``lists`` are mutable, i.e. they can be changed in place:\n")
    print('>>> a_lst = [6,7,8,9]')
    a_lst = [6,7,8,9]
    print('>>> a_lst')
    print(a_lst)
    print('\nInsertion in front:\n')
    print('>>> a_lst[:0] = [0,1,2,3]')
    a_lst[:0] = [0,1,2,3]
    print('>>> a_lst')
    print(a_lst)
    print('\nExtension at the end:\n')
    print('>>> a_lst[len(l):] = [10,11,12,13]')
    a_lst[len(a_lst):] = [10,11,12,13]
    print('>>> a_lst')
    print(a_lst)
    print('\nInsertion at position 4:\n')
    print('>>> a_lst[4:4] = [4,5]')
    a_lst[4:4] = [4,5]
    print('>>> a_lst')
    print(a_lst)
    print('\nDelete elements from position 4 to 5, '
        'same as del a_lst[4:6]\n')
    print('>>> a_lst[4:6] = []')
    a_lst[4:6] = []
    print('>>> a_lst')
    print(a_lst)
    print(80*'-')
