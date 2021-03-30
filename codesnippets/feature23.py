##    Python codesnippets - Parallel traversals with zip()
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
# Feature 23
#

"""
Parallel traversals with ``zip()``
==================================

:py:mod:`codesnippets.feature23`
--------------------------------

Three lists can be traversed in parallel with ``zip()``:

>>> lst1, lst2, lst3 = (1,2,3), (4,5,6), (7,8,9)

>>> for (a_value,b_value,c_value) in zip(lst1,lst2,lst3):
        print(a_value,b_value,c_value)
1 4 7
2 5 8
3 6 9

If the lists have different length, use ``itertools.zip_longest()``:

>>> lst1, lst2, lst3 = (1,2), (3,4,5), (6,7,8,9)

>>> for (a_value,b_value,c_value) in itertools.zip_longest(lst1,lst2,lst3,fillvalue=0):
        print(a_value,b_value,c_value)
1 3 6
2 4 7
0 5 8
0 0 9
"""

import itertools

def feature23():
    """Parallel traversals with zip()"""
    print('Parallel traversals with ``zip()``')
    print('==================================\n')
    print(':py:mod:`codesnippets.feature23`')
    print('--------------------------------\n')
    print('Three lists can be traversed in parallel with ``zip()``:\n')
    print('>>> lst1, lst2, lst3 = (1,2,3), (4,5,6), (7,8,9)')
    print('\n>>> for (a_value,b_value,c_value) in zip(lst1,lst2,lst3):')
    print('        print(a_value,b_value,c_value)')
    lst1, lst2, lst3 = (1,2,3), (4,5,6), (7,8,9)
    for (a_value,b_value,c_value) in zip(lst1,lst2,lst3):
        print(a_value,b_value,c_value)
    print()
    print('If the lists have different length, use ``itertools.zip_longest()``:')
    print()
    print('>>> lst1, lst2, lst3 = (1,2), (3,4,5), (6,7,8,9)')
    print('\n>>> for (a_value,b_value,c_value) in '
          'itertools.zip_longest(lst1,lst2,lst3,fillvalue=0):')
    print('        print(a_value,b_value,c_value)')
    lst1, lst2, lst3 = (1,2), (3,4,5), (6,7,8,9)
    for (a_value,b_value,c_value) in itertools.zip_longest(lst1,lst2,lst3,fillvalue=0):
        print(a_value,b_value,c_value)
    print(80*'-')