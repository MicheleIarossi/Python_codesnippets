##    Python codesnippets - List comprehension
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
# Feature 8
#

"""
``list`` comprehension
======================

:py:mod:`codesnippets.feature8`
-------------------------------

Basic syntax:

>>> a_str = [a_chr*4 for a_chr in 'MIKE']
['MMMM', 'IIII', 'KKKK', 'EEEE']

A filter (condition) can also be specified:

>>> a_str = [a_chr*4 for a_chr in 'MIKE' if a_chr != 'I']
['MMMM', 'KKKK', 'EEEE']

.. seealso:: :doc:`Lambda functions, map() and list comprehension<feature46>`
"""

def feature8():
    """List comprehension"""
    print('``list`` comprehension')
    print('======================\n')
    print(':py:mod:`codesnippets.feature8`')
    print('-------------------------------\n')
    print('Basic syntax:\n')
    print(">>> a_str = [a_chr*4 for a_chr in 'MIKE']")
    a_str = [a_chr*4 for a_chr in 'MIKE']
    print(a_str)
    print('\nA filter (condition) can also be specified:\n')
    print(">>> a_str = [a_chr*4 for a_chr in 'MIKE' if a_chr != 'I']")
    a_str = [a_chr*4 for a_chr in 'MIKE' if a_chr != 'I']
    print(a_str)
    print('\n.. seealso:: :doc:`Lambda functions, map() and list comprehension<feature46>`')
    print(80*'-')
