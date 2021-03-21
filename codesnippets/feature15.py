##    Python codesnippets - Comparison and equality
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
# Feature 15
#

"""
Comparison and equality
=======================

:py:mod:`codesnippets.feature15`
--------------------------------

These objects have the same values but are 2 different objects in memory:

>>> lst1 = [1, ('a',3)]
>>> lst2 = [1, ('a',3)]

>>> lst1 == lst2, lst1 is lst2
(True, False)
"""

def feature15():
    """Comparison and equality"""
    print('Comparison and equality')
    print('=======================\n')
    print(':py:mod:`codesnippets.feature15`')
    print('--------------------------------\n')
    print('These objects have the same values but are 2 different objects in memory:\n')
    print(">>> lst1 = [1, ('a',3)]")
    print(">>> lst2 = [1, ('a',3)]")
    print('\n>>> lst1 == lst2, lst1 is lst2')
    lst1 = [1, ('a',3)]
    lst2 = [1, ('a',3)]
    print((lst1==lst2, lst1 is lst2))
    print(80*'-')
