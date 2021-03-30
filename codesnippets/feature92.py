##    Python codesnippets - Bytes, bytearray and string
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
# Feature 92
#

"""
Bytes, bytearray and string
===========================

:py:mod:`codesnippets.feature92`
--------------------------------

``bytes`` and ``bytearray`` are sequences of integers.
``str`` is a sequence of characters:

>>> b_byte = b'pippolone'

>>> list(b_byte)
[112, 105, 112, 112, 111, 108, 111, 110, 101]

>>> b_bytearray = bytearray(b_byte)

>>> list(b_bytearray)
[112, 105, 112, 112, 111, 108, 111, 110, 101]

>>> s_str = 'pippolone'

>>> list(s_str)
['p', 'i', 'p', 'p', 'o', 'l', 'o', 'n', 'e']

.. note:: ``bytearray`` is a mutable variant of ``bytes``.
"""

def feature92():
    """Bytes, bytearray and string"""
    print('Bytes, bytearray and string')
    print('===========================\n')
    print(':py:mod:`codesnippets.feature92`')
    print('--------------------------------\n')
    print("``bytes`` and ``bytearray`` are sequences of integers.")
    print("``str`` is a sequence of characters:\n")
    print(">>> b_byte = b'pippolone'")
    b_byte = b'pippolone'
    print("\n>>> list(b_byte)")
    print(list(b_byte))
    print("\n>>> b_bytearray = bytearray(b_byte)")
    b_bytearray = bytearray(b_byte)
    print("\n>>> list(b_bytearray)")
    print(list(b_bytearray))
    print("\n>>> s_str = 'pippolone'")
    s_str = 'pippolone'
    print("\n>>> list(s_str)")
    print(list(s_str))
    print('\n.. note:: ``bytearray`` is a mutable variant of ``bytes``.')
    print(80*'-')