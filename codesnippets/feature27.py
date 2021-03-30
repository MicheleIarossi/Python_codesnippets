##    Python codesnippets - The iteration protocol
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
# Feature 27
#

"""
The iteration protocol
======================

:py:mod:`codesnippets.feature27`
--------------------------------

Automatic iteration:

>>> a_lst = ['abc','def','ghi']
>>> for a_str in a_lst:
        print(a_str)
abc
def
ghi

Manual iteration:

>>> a_lst = ['abc','def','ghi']       # a list is an iterable object

>>> a_lst_iter = iter(str_lst)        # get iterator object

>>> while True:
        try:
            a_str = next(a_lst_iter)  # same as str_lst_iter.__next__()
        except StopIteration:
            break
        print(a_str)
abc
def
ghi
"""

def feature27():
    """The iteration protocol"""
    print('The iteration protocol')
    print('======================\n')
    print(':py:mod:`codesnippets.feature27`')
    print('--------------------------------\n')
    print('Automatic iteration:\n')
    print(">>> a_lst = ['abc','def','ghi']")
    print('>>> for a_str in a_lst:')
    print('        print(a_str)')
    a_lst = ['abc','def','ghi']
    for a_str in a_lst:
        print(a_str)
    print('\nManual iteration:\n')
    print(">>> a_lst = ['abc','def','ghi']       # a list is an iterable object\n")
    print('>>> a_lst_iter = iter(str_lst)        # get iterator object\n')
    print('>>> while True:')
    print('        try:')
    print('            a_str = next(a_lst_iter)  # same as str_lst_iter.__next__()')
    print('        except StopIteration:')
    print('            break')
    print('        print(a_str)')
    a_lst = ['abc','def','ghi']
    a_lst_iter = iter(a_lst)
    while True:
        try:
            a_str = next(a_lst_iter)
        except StopIteration:
            break
        print(a_str)
    print(80*'-')