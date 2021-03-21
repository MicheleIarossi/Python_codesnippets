##    Python codesnippets - Formatting string expressions with .format() syntax
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
# Feature 5
#

"""
Formatting string expressions with .format() syntax
===================================================

:py:mod:`codesnippets.feature5`
-------------------------------

The second possibility for formatting strings is to use ``''.format()``:

* ``{0}``, ``{1}``, ... refer to the position of the parameters provided to ``format()``,
* ``>``, ``<`` mean left and right alignement

>>> a_var = 13.4351
>>> a_str = '{0:<10} = {1:.2f}'.format('a_var',a_var)
>>> a_str
a_var      = 13.44

A caret ``^`` can be used for centering the string:

>>> a_var = 13.4351
>>> a_str = '{0:^10} = {1:.2f}'.format('a_var',a_var)
>>> a_str
  a_var    = 13.44

Instead of dictionaries, keywords arguments are used:

>>> a_var = 13.4351
>>> a_str = '{key:^10} = {value:.2f}'.format(key='a_var',value=13.4351)
>>> a_str
  a_var    = 13.44
"""

def feature5():
    """Formatting string expressions with .format() syntax"""
    print('Formatting string expressions with .format() syntax')
    print('===================================================\n')
    print(':py:mod:`codesnippets.feature5`')
    print('-------------------------------\n')
    print("The second possibility for formatting strings is to use ''.format()\n")
    print("{0}, {1}, ... refer to the position of the parameters provided to format()")
    print(">, < mean left and right alignement:\n")
    a_var = 13.4351
    print('>>> a_var = 13.4351')
    a_str = '{0:<10} = {1:.2f}'.format('a_var',a_var)
    print(">>> a_str = '{0:<10} = {1:.2f}'.format('a_var',a_var)")
    print(">>> a_str")
    print(a_str)

    print('\nA caret ^ can be used for centering the string:\n')
    a_var = 13.4351
    print('>>> a_var = 13.4351')
    a_str = '{0:^10} = {1:.2f}'.format('a_var',a_var)
    print(">>> a_str = '{0:^10} = {1:.2f}'.format('a_var',a_var)")
    print(">>> a_str")
    print(a_str)

    print("\nInstead of dictionaries, keywords arguments are used:\n")
    a_var = 13.4351
    print('>>> a_var = 13.4351')
    a_str = '{key:^10} = {value:.2f}'.format(key='a_var',value=a_var)
    print(">>> a_str = '{key:^10} = {value:.2f}'.format(key='a_var',value=13.4351)")
    print(">>> a_str")
    print(a_str)
    print(80*'-')
