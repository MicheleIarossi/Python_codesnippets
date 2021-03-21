##    Python codesnippets - More assignment unpacking
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
# Feature 16
#

"""
More assignment unpacking
=========================

:py:mod:`codesnippets.feature16`
--------------------------------

Similar to enumerated data type:

>>> red, green, blue = range(3)
>>> red, green, blue
(0, 1, 2)

Nested sequence assignment unpacking:

>>> ((a_str, b_str), c_str) = ('SP', 'AM')
>>> a_str, b_str, c_str
('S', 'P', 'AM')

Extended sequence unpacking (always assigns a ``list``!):

>>> a_value, *b_lst, c_value = (1, 2, 3, 4)
>>> (a_val, b_lst, c_value)
(1, [2, 3], 4)

Similar to slicing but slicing keeps the type!

>>> s_str = 'spam'
>>> s_str[0], s_str[1:3], s_str[3]
('s', 'pa', 'm')

>>> a_str, *b_lst, c_str = s_str
>>> (a_str, b_lst, c_str)
('s', ['p', 'a'], 'm')
"""

def feature16():
    """More assignment unpacking"""
    print('More assignment unpacking')
    print('=========================\n')
    print(':py:mod:`codesnippets.feature16`')
    print('--------------------------------\n')
    print('Similar to enumerated data type:\n')
    print('>>> red, green, blue = range(3)')
    print('>>> red, green, blue')
    red, green, blue = range(3)
    print((red, green, blue))
    print('\nNested sequence assignment unpacking:\n')
    print(">>> ((a_str, b_str), c_str) = ('SP', 'AM')")
    print(">>> a_str, b_str, c_str")
    ((a_str, b_str), c_str) = ('SP', 'AM')
    print((a_str,b_str,c_str))
    print('\nExtended sequence unpacking (always assigns a ``list``!):\n')
    print(">>> a_value, *b_lst, c_value = (1, 2, 3, 4)")
    print(">>> (a_val, b_lst, c_value)")
    a_value, *b_lst, c_value = [1, 2, 3, 4]
    print((a_value, b_lst, c_value))
    print('\nSimilar to slicing but slicing keeps the type!\n')
    print(">>> s_str = 'spam'")
    print(">>> s_str[0], s_str[1:3], s_str[3]")
    s_str = 'spam'
    print((s_str[0], s_str[1:3], s_str[3]))
    print("\n>>> a_str, *b_lst, c_str = s_str")
    print(">>> (a_str, b_lst, c_str)")
    a_str, *b_lst, c_str = s_str
    print((a_str, b_lst, c_str))
    print(80*'-')
