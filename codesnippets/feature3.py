##    Python codesnippets - Transforming a string into a list
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
# Feature 3
#

"""
Transforming a string into a list
=================================

:py:mod:`codesnippets.feature3`
-------------------------------

>>> a_str = 'jennifer'

>>> a_lst = list(a_str)

>>> a_lst
['j', 'e', 'n', 'n', 'i', 'f', 'e', 'r']

>>> a_lst[1] = 'r'

>>> a_lst
['j', 'r', 'n', 'n', 'i', 'f', 'e', 'r']

>>> a_str = ''.join(a_lst)
jrnnifer
"""

def feature3():
    """Transforming a string into a list"""
    print('Transforming a string into a list')
    print('=================================\n')
    print(':py:mod:`codesnippets.feature3`')
    print('-------------------------------\n')
    print(">>> a_str = 'jennifer'")
    a_str = 'jennifer'
    print('\n>>> a_lst = list(a_str)')
    a_lst = list(a_str)
    print('\n>>> a_lst')
    print(a_lst)
    print("\n>>> a_lst[1] = 'r'")
    a_lst[1] = 'r'
    print('\n>>> a_lst')
    print(a_lst)
    print("\n>>> a_str = ''.join(a_lst)")
    a_str = ''.join(a_lst)
    print(a_str)
    print(80*'-')
