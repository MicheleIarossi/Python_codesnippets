##    Python codesnippets - Assignment expressions: walrus operator
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
# Feature 19
#

"""
Assignment expressions: walrus operator
=======================================

:py:mod:`codesnippets.feature19`
--------------------------------

Assignment expressions use the *walrus operator* ``:=`` and can be used in places where assignment statements are not allowed.

A typical place would be inside a conditional expression of an ``if`` statement:

>>> a,b = 23,17

>>> if (c:= a+b)>30:
        print(f'Above 30: c = {c}')
    else:
        print(f'Below 30: c = {c}')
Above 30: c = 40
"""

def feature19():
    """Assignment expressions: walrus operator"""
    print('Assignment expressions: walrus operator')
    print('=======================================\n')
    print(':py:mod:`codesnippets.feature19`')
    print('--------------------------------\n')
    print('Assignment expressions use the *walrus operator* ``:=`` and can be used in places '
          'where assignment statements are not allowed.\n')
    print('A typical place would be inside a conditional expression of an ``if`` statement:\n')
    a,b = 23,17
    print(">>> a,b = 23,17\n")
    print(""">>> if (c:= a+b)>30:
        print(f'Above 30: c = {c}')
    else:
        print(f'Below 30: c = {c}')""")
    if (c:= a+b)>30:
        print(f'Above 30: c = {c}')
    else:
        print(f'Below 30: c = {c}')
    print(80*'-')
