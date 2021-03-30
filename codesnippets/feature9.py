##    Python codesnippets - map() on the elements of a list
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
# Feature 9
#

"""
``map()`` on the elements of a ``list``
=======================================

:py:mod:`codesnippets.feature9`
-------------------------------

Applies the same function to the elements of a ``list``, and returns
an iterable that is passed to ``list()`` for producing the sequence values:

>>> res = list(map(abs, [-1,-2,0,1,2]))
[1, 2, 0, 1, 2]

.. seealso:: :doc:`Lambda functions, map() and list comprehension<feature47>`
"""

def feature9():
    """map() on the elements of a list"""
    print('``map()`` on the elements of a ``list``')
    print('=======================================\n')
    print(':py:mod:`codesnippets.feature9`')
    print('-------------------------------\n')
    print('Applies the same function to the elements of a ``list``, and returns')
    print("an iterable that is passed to ``list()`` for producing the sequence values:\n")
    print('>>> res = list(map(abs, [-1,-2,0,1,2]))')
    res = list(map(abs, [-1,-2,0,1,2]))
    print(res)
    print('\n.. seealso:: :doc:`Lambda functions, map() and list comprehension<feature47>`')
    print(80*'-')