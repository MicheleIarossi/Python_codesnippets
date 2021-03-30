##    Python codesnippets - Ternary expression
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
# Feature 22
#

"""
Ternary expression
==================

:py:mod:`codesnippets.feature22`
--------------------------------

Saves lines when typing code:

>>> a_str = 't' if 'spam' else 'f'
>>> a_str
t

>>> a_str = 't' if '' else 'f'
>>> a_str
f
"""

def feature22():
    """Ternary expression"""
    print("Ternary expression")
    print('==================\n')
    print(':py:mod:`codesnippets.feature22`')
    print('--------------------------------\n')
    print("Saves lines when typing code:\n")
    print(">>> a_str = 't' if 'spam' else 'f'")
    print(">>> a_str")
    a_str = 't' if 'spam' else 'f'
    print(a_str)
    print("\n>>> a_str = 't' if '' else 'f'")
    print(">>> a_str")
    a_str = 't' if '' else 'f'
    print(a_str)
    print(80*'-')