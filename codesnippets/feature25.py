##    Python codesnippets - Side effects in loops
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
# Feature 25
#

"""
Side effects in loops
=====================

:py:mod:`codesnippets.feature25`
--------------------------------

If the data type is immutable, there are no side effects!

>>> a_lst = [1,2,3,4]

>>> for a_value in a_lst:
        a_value += 1

>>> a_lst
[1, 2, 3, 4]

If the data type is mutable, beware of in-place changes!

>>> a_lst_of_lst = [[1,2],[3,4],[5,6],[7,8]]

>>> for a_lst in a_lst_of_lst:
        a_lst += [-1,-2] # calls list extend method

>>> a_lst_of_lst
[[1, 2, -1, -2], [3, 4, -1, -2], [5, 6, -1, -2], [7, 8, -1, -2]]
"""

def feature25():
    """Side effects in loops"""
    print('Side effects in loops')
    print('=====================\n')
    print(':py:mod:`codesnippets.feature25`')
    print('--------------------------------\n')
    print("If the data type is immutable, there are no side effects!\n")
    print(">>> a_lst = [1,2,3,4]\n")
    print(">>> for a_value in a_lst:")
    print("        a_value += 1\n")
    print(">>> a_lst")
    a_lst = [1,2,3,4]
    for a_value in a_lst:
        a_value += 1
    print(a_lst)
    print("\nIf the data type is mutable, beware of in-place changes!\n")
    print(">>> a_lst_of_lst = [[1,2],[3,4],[5,6],[7,8]]\n")
    print(">>> for a_lst in a_lst_of_lst:")
    print("        a_lst += [-1,-2] # calls list extend method\n")
    print(">>> a_lst_of_lst")
    a_lst_of_lst = [[1,2],[3,4],[5,6],[7,8]]
    for a_lst in a_lst_of_lst:
        a_lst += [-1,-2]
    print(a_lst_of_lst)
    print(80*'-')
