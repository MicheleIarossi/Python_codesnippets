##    Python codesnippets - Formatting string expressions with the basic syntax
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
# Feature 4
#

"""
Formatting string expressions with the basic syntax
===================================================

:py:mod:`codesnippets.feature4`
-------------------------------

Everything can be formatted as a string.

This shows the basic formatting string syntax:

>>> a_str = '%s %s %s %s' % (1.23,-3,5.67,7.889)
>>> a_str
1.23 -3 5.67 7.889

>>> a_str = '%+05d | 0x%x | %+10.*f' % (23,1043,3,3.1415)
>>> a_str
+0023 | 0x413 |     +3.142

Reads in the width (10) and precision (3) from the input list:

>>> a_str = '%*.*f' % (10,3,3.1415) # Reads in the width (10) and precision (3) from the input list
>>> a_str
     3.142

Dictionaries can be also used for specifying values to print:

>>> a_str = '%(key)-10s = %(value).3f' % {'key': 'a_var','value': 13.4351}
>>> a_str
a_var      = 13.435
"""

def feature4():
    """Formatting string expressions with the basic syntax"""
    print('Formatting string expressions with the basic syntax')
    print('===================================================\n')
    print(':py:mod:`codesnippets.feature4`')
    print('-------------------------------\n')
    print('Everything can be formatted as a string\n')
    print('This shows the basic formatting string syntax:\n')

    print(">>> a_str = '%s %s %s %s' % (1.23,-3,5.67,7.889)")
    a_str = '%s %s %s %s' % (1.23,-3,5.67,7.889)
    print('>>> a_str')
    print(a_str)

    print("\n>>> a_str = '%+05d | 0x%x | %+10.*f' % (23,1043,3,3.1415)")
    a_str = '%+05d | 0x%x | %+10.*f' % (23,1043,3,3.1415)
    print('>>> a_str')
    print(a_str)

    print('\nReads in the width (10) and precision (3) from the input list:\n')
    print(">>> a_str = '%*.*f' % (10,3,3.1415) # Reads in the width (10) "
        "and precision (3) from the input list")
    a_str = '%*.*f' % (10,3,3.1415)
    print('>>> a_str')
    print(a_str)

    print('\nDictionaries can be also used for specifying values to print:\n')
    a_str = '%(key)-10s = %(value).3f' % {'key': 'a_var','value': 13.4351}
    print(">>> a_str = '%(key)-10s = %(value).3f' % {'key': 'a_var','value': 13.4351}")
    print(">>> a_str")
    print(a_str)
    print(80*'-')
