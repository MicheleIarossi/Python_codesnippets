##    Python codesnippets - Dictionary construction with zip()
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
# Feature 23
#

"""
Dictionary construction with ``zip()``
======================================

:py:mod:`codesnippets.feature23`
--------------------------------

Uses dictionary comprehension:

>>> key_lst   = ['abc','def','ghi']
>>> value_lst = [2,5,9]

>>> a_dict = {a_key:a_value for (a_key,a_value) in zip(key_lst,value_lst)}
>>> a_dict
{'abc': 2, 'def': 5, 'ghi': 9}

This is the same as:

>>> a_dict = dict(zip(key_lst,value_lst))
>>> a_dict
{'abc': 2, 'def': 5, 'ghi': 9}
"""

def feature23():
    """Dictionary construction with zip()"""
    print('Dictionary construction with ``zip()``')
    print('======================================\n')
    print(':py:mod:`codesnippets.feature23`')
    print('--------------------------------\n')
    print("Uses dictionary comprehension:\n")
    print(">>> key_lst   = ['abc','def','ghi']")
    print(">>> value_lst = [2,5,9]\n")
    key_lst   = ['abc','def','ghi']
    value_lst = [2,5,9]
    print(">>> a_dict = {a_key:a_value for (a_key,a_value) in zip(key_lst,value_lst)}")
    a_dict = {a_key:a_value for (a_key,a_value) in zip(key_lst,value_lst)}
    print(">>> a_dict")
    print(a_dict)
    print("\nThis is the same as:\n")
    print(">>> a_dict = dict(zip(key_lst,value_lst))")
    print(">>> a_dict")
    print(a_dict)
    print(80*'-')
