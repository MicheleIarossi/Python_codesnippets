##    Python codesnippets - Boolean and/or operators
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
# Feature 21
#

"""
Boolean and/or operators
========================

:py:mod:`codesnippets.feature21`
--------------------------------

Boolean operators ``and`` and ``or`` return true or false objects not values!

``or`` returns the left operand if true:

>>> 2 or 3, 3 or 2
(2, 3)

``and`` returns the right operand if true:

>>> 2 and 3, 3 and 2
(3, 2)
"""

def feature21():
    """Boolean and/or operators"""
    print("Boolean and/or operators")
    print('========================\n')
    print(':py:mod:`codesnippets.feature21`')
    print('--------------------------------\n')
    print("Boolean operators 'and' and 'or' return true or false objects not values!\n")
    print("'or' returns left operand if true:\n")
    print(">>> 2 or 3, 3 or 2")
    print((2 or 3, 3 or 2))
    print("\n'and' returns right operand if true:\n")
    print(">>> 2 and 3, 3 and 2")
    print((2 and 3, 3 and 2))
    print(80*'-')