##    Python codesnippets - Byte and string types
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
# Feature 87
#

"""
Byte and string types
=====================

:py:mod:`codesnippets.feature87`
--------------------------------

The type ``byte`` is used for representing binary data.
And the type ``str`` is used for representing strings, whose
binary representation depends on the encoding chosen.

.. note:: The two types cannot be mixed.

>>> bin_array = bytes([100,234,98,23,67,180,201])

>>> type(bin_array)
<class 'bytes'>

>>> bin_array
b'd\\xeab\\x17C\\xb4\\xc9'

>>> len(bin_array)
7

>>> text_str = 'The sky is blue.'

>>> type(text_str)
<class 'str'>

>>> text_str.encode('UTF-16')
b'\\xff\\xfeT\\x00h\\x00e\\x00 \\x00s\\x00k\\x00y\\x00 \\x00i\\x00s\\x00 \\x00b\\x00l\\x00u\\x00e\\x00.\\x00'

>>> len(text_str)
16
"""

def feature87():
    """Byte and string types"""
    print('Byte and string types')
    print('=====================\n')
    print(':py:mod:`codesnippets.feature87`')
    print('--------------------------------\n')
    print("The type ``byte`` is used for representing binary data.")
    print("And the type ``str`` is used for representing strings, whose")
    print("binary representation depends on the encoding chosen.\n")
    print(".. note: The two types cannot be mixed.\n")
    print(">>> bin_array = bytes([100,234,98,23,67,180,201])")
    bin_array = bytes([100,234,98,23,67,180,201])
    print("\n>>> type(bin_array)")
    print(type(bin_array))
    print("\n>>> bin_array")
    print(bin_array)
    print("\n>>> len(bin_array)")
    print(len(bin_array))
    print()
    print(">>> text_str = 'The sky is blue.'")
    text_str = 'The sky is blue.'
    print("\n>>> type(text_str)")
    print(type(text_str))
    print("\n>>> text_str.encode('UTF-16')")
    print(text_str.encode('UTF-16'))
    print("\n>>> len(text_str)")
    print(len(text_str))
    print(80*'-')