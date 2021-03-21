##    Python codesnippets - First, rest pattern
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
# Feature 17
#

"""
First, rest pattern
===================

:py:mod:`codesnippets.feature17`
--------------------------------

First, rest pattern:

>>> a_value, *b_lst = [1, 2, 3, 4]
>>> (a_value, b_lst)
(1, [2, 3, 4])

Rest, last pattern:

>>> *a_lst, b_value = [1, 2, 3, 4]
>>> (a_lst, b_value)
([1, 2, 3], 4)
"""

def feature17():
    """First, rest pattern"""
    print('First, rest pattern')
    print('===================\n')
    print(':py:mod:`codesnippets.feature17`')
    print('--------------------------------\n')
    print('First, rest pattern:\n')
    print(">>> a_value, *b_lst = [1, 2, 3, 4]")
    print(">>> (a_value, b_lst)")
    a_value, *b_lst = [1, 2, 3, 4]
    print((a_value, b_lst))
    print('\nRest, last pattern:\n')
    print(">>> *a_lst, b_value = [1, 2, 3, 4]")
    print(">>> (a_lst, b_value)")
    *a_lst, b_value = [1, 2, 3, 4]
    print((a_lst, b_value))
    print(80*'-')
