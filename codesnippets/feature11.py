##    Python codesnippets - Merging dictionaries by dictionary unpacking
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
# Feature 11
#

"""
Merging dictionaries by dictionary unpacking
============================================

:py:mod:`codesnippets.feature11`
--------------------------------

This works because ``**a_dict_1`` and ``**a_dict_2`` perform
dictionary unpacking into keyword arguments.

>>> a_dict_1 = {'a':1, 'b':2, 'c':3}
>>> a_dict_2 = {'c':4, 'd':5, 'e':6}

>>> {**a_dict_1,**a_dict_2}
{'a': 1, 'b': 2, 'c': 4, 'd': 5, 'e': 6}

Equivalent to:

>>> dict(a=1,b=2,c=4,d=5,e=6)
{'a': 1, 'b': 2, 'c': 4, 'd': 5, 'e': 6}
"""

def feature11():
    """Merging dictionaries by dictionary unpacking"""
    print('Merging dictionaries by dictionary unpacking')
    print('============================================\n')
    print(':py:mod:`codesnippets.feature11`')
    print('--------------------------------\n')
    print("This works because **a_dict_1 and **a_dict_2 perform")
    print("dictionary unpacking into keyword arguments.\n")
    print(">>> a_dict_1 = {'a':1, 'b':2, 'c':3}")
    print(">>> a_dict_2 = {'c':4, 'd':5, 'e':6}")
    a_dict_1 = {'a':1, 'b':2, 'c':3}
    a_dict_2 = {'c':4, 'd':5, 'e':6}
    print("\n>>> {**a_dict_1,**a_dict_2}")
    print({**a_dict_1,**a_dict_2})
    print("\nEquivalent to:\n")
    print(">>> dict(a=1,b=2,c=4,d=5,e=6)")
    print(dict(a=1,b=2,c=4,d=5,e=6))
    print(80*'-')
