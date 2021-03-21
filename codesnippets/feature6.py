##    Python codesnippets - Formatting string expressions with f-strings syntax
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
# Feature 6
#

"""
Formatting string expressions with f-strings syntax
===================================================

:py:mod:`codesnippets.feature6`
-------------------------------

The third and recommended method for formatting strings is to use f-strings:

>>> a_var = 13.4351
>>> a_str = f"{'a_str':<10} = {a_var:.2f}"
>>> a_str
a_str      = 13.44

Python expression can be embedded into the format specifiers too:

>>> a_var = 13.4351
>>> a_str = f"{'a_str':<10} = {a_var*2:.2f}"
>>> a_str
a_str      = 26.87
"""

def feature6():
    """Formatting string expressions with f-strings syntax"""
    print('Formatting string expressions with f-strings syntax')
    print('===================================================\n')
    print(':py:mod:`codesnippets.feature6`')
    print('-------------------------------\n')
    print("The third and recommended method for formatting strings is to use f-strings:\n")
    a_var = 13.4351
    print('>>> a_var = 13.4351')
    a_str = f"{'a_str':<10} = {a_var:.2f}"
    print(""">>> a_str = f"{'a_str':<10} = {a_var:.2f}" """)
    print(">>> a_str")
    print(a_str)

    print("\nPython expression can be embedded into the format specifiers too:\n")
    a_var = 13.4351
    print('>>> a_var = 13.4351')
    a_str = f"{'a_str':<10} = {a_var*2:.2f}"
    print(""">>> a_str = f"{'a_str':<10} = {a_var*2:.2f}" """)
    print(">>> a_str")
    print(a_str)
    print(80*'-')
