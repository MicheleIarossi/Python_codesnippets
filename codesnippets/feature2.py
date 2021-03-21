##    Python codesnippets - Slicing strings
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
# Feature 2
#

"""
Slicing strings
===============

:py:mod:`codesnippets.feature2`
-------------------------------

>>> a_str = 'donald'

From index 1 until one past the last index excluded:

>>> a_str[1:]
onald

From the beginning until the last index excluded:

>>> a_str[:-1]
donal

From the beginning until the end:

>>> a_str[:]
donald

Beyond the end (missing items are silently omitted):

>>> a_str[:20]
donald
"""

def feature2():
    """Slicing strings"""
    print('Slicing strings')
    print('===============\n')
    print(':py:mod:`codesnippets.feature2`')
    print('-------------------------------\n')
    print(">>> a_str = 'donald'\n")
    a_str = 'donald'
    print('From index 1 until one past the last index excluded:\n')
    print('>>> a_str[1:]')
    print(a_str[1:])
    print('\nFrom the beginning until the last index excluded:\n')
    print('>>> a_str[:-1]')
    print(a_str[:-1])
    print('\nFrom the beginning until the end:\n')
    print('>>> a_str[:]')
    print(a_str[:])
    print('\nBeyond the end (missing items are silently omitted):\n')
    print('>>> a_str[:20]')
    print(a_str[:20])
    print(80*'-')
