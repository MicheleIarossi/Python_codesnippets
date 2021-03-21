##    Python codesnippets - Dictionaries
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
# Feature 10
#

"""
Dictionaries
============

:py:mod:`codesnippets.feature10`
--------------------------------

Construction with keywords:

>>> a_dic = dict(name='Bob', age=40)
{'name': 'Bob', 'age': 40}

Same as:

>>> a_dic = {'name':'Bob','age':40}
{'name': 'Bob', 'age': 40}

Keys, values and items:

>>> a_dic = {'eggs':3 ,'spam':2, 'ham':1}
{'eggs': 3, 'spam': 2, 'ham': 1}

>>> list(a_dic.keys())
['eggs', 'spam', 'ham']

>>> list(a_dic.values())
[3, 2, 1]

>>> list(a_dic.items())
[('eggs', 3), ('spam', 2), ('ham', 1)]
"""

def feature10():
    """Dictionaries"""
    print('Dictionaries')
    print('============\n')
    print(':py:mod:`codesnippets.feature10`')
    print('--------------------------------\n')
    print('Construction with keywords:\n')
    print(">>> a_dic = dict(name='Bob', age=40)")
    a_dic = dict(name='Bob', age=40)
    print(a_dic)
    print('\nSame as:\n')
    print(">>> a_dic = {'name':'Bob','age':40}")
    a_dic = {'name':'Bob','age':40}
    print(a_dic)
    print('\nKeys, values and items:\n')
    print(">>> a_dic = {'eggs':3 ,'spam':2, 'ham':1}")
    a_dic = {'eggs':3 ,'spam':2, 'ham':1}
    print(a_dic)
    print("\n>>> list(a_dic.keys())")
    print(list(a_dic.keys()))
    print("\n>>> list(a_dic.values())")
    print(list(a_dic.values()))
    print("\n>>> list(a_dic.items())")
    print(list(a_dic.items()))
    print(80*'-')
