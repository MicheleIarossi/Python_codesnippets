##    Python codesnippets - Assignment unpacking
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
# Feature 13
#

"""
Assignment unpacking
====================

:py:mod:`codesnippets.feature13`
--------------------------------

>>> a_value, b_value, c_value = (4,-3,6)

>>> a_value, b_value, c_value
(4, -3, 6)

.. seealso:: :doc:`More assignment unpacking<feature16>`
"""

def feature13():
    """Assignment unpacking"""
    print('Assignment unpacking')
    print('====================\n')
    print(':py:mod:`codesnippets.feature13`')
    print('--------------------------------\n')
    print(">>> a_value, b_value, c_value = (4,-3,6)")
    a_value, b_value, c_value = (4,-3,6)
    print("\n>>> a_value, b_value, c_value")
    print((a_value,b_value,c_value))
    print('\n.. seealso:: :doc:`More assignment unpacking<feature16>`')
    print(80*'-')
