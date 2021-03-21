##    Python codesnippets - ASCII text
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
# Feature 88
#

"""
ASCII text
==========

:py:mod:`codesnippets.feature88`
--------------------------------

ASCII uses only 7 bits for the encoding.
ASCII is supported by Latin-1 and UTF-8.
Latin-1 uses 8 bits, and UTF-8/16/32 uses 8, 16 or 32 bits.

>>> a_str = 'ABC'
>>> len(a_str)
3

>>> list(a_str.encode('ascii'))
[65, 66, 67]

>>> list(a_str.encode('latin-1'))
[65, 66, 67]

>>> list(a_str.encode('utf-8'))
[65, 66, 67]
"""

def feature88():
    """ASCII text"""
    print('ASCII text')
    print('==========\n')
    print(':py:mod:`codesnippets.feature88`')
    print('--------------------------------\n')
    print("ASCII uses only 7 bits for the encoding.")
    print("ASCII is supported by Latin-1 and UTF-8.")
    print("Latin-1 uses 8 bits, and UTF-8/16/32 uses 8, 16 or 32 bits.\n")
    print(">>> a_str = 'ABC'")
    a_str = 'ABC'
    print(">>> len(a_str)")
    print(len(a_str))
    print("\n>>> list(a_str.encode('ascii'))")
    print(list(a_str.encode('ascii')))
    print("\n>>> list(a_str.encode('latin-1'))")
    print(list(a_str.encode('latin-1')))
    print("\n>>> list(a_str.encode('utf-8'))")
    print(list(a_str.encode('utf-8')))
    print(80*'-')
