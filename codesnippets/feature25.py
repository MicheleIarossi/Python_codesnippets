##    Python codesnippets - Loop with enumerate()
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
Loop with ``enumerate()``
=========================

:py:mod:`codesnippets.feature25`
--------------------------------

The built-in ``enumerate()`` gives the offset and the item to use:

>>> a_lst = ['abc','def','ghi']

>>> for (i_idx,s_str) in enumerate(a_lst):
        print(i_idx,s_str)
0 abc
1 def
2 ghi

A start value can be also given, e.g. starting from 1 instead of 0:

>>> a_lst = ['abc','def','ghi']

>>> for (i_idx,s_str) in enumerate(a_lst,1):
        print(i_idx,s_str)
1 abc
2 def
3 ghi
"""

def feature25():
    """Loop with enumerate()"""
    print('Loop with ``enumerate()``')
    print('=========================\n')
    print(':py:mod:`codesnippets.feature25`')
    print('--------------------------------\n')
    print("The built-in ``enumerate()`` gives the offset and the item to use:\n")
    print(">>> a_lst = ['abc','def','ghi']\n")
    print(">>> for (i_idx,s_str) in enumerate(a_lst):")
    print("        print(i_idx,s_str)")
    a_lst = ['abc','def','ghi']
    for (i_idx,s_str) in enumerate(a_lst):
        print(i_idx,s_str)
    print("\nA start value can be also given, e.g. starting from 1 instead of 0:\n")
    print(">>> a_lst = ['abc','def','ghi']\n")
    print(">>> for (i_idx,s_str) in enumerate(a_lst,1):")
    print("        print(i_idx,s_str)")
    a_lst = ['abc','def','ghi']
    for (i_idx,s_str) in enumerate(a_lst,1):
        print(i_idx,s_str)
    print(80*'-')