##    Python codesnippets - String and byte literals
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
# Feature 90
#

"""
String and byte literals
========================

:py:mod:`codesnippets.feature90`
--------------------------------

In bytes literals only ``\\x`` escapes can be used!

>>> b_str = b'\\xae\\xeb\\x56\\xa4\\x89'

>>> s_str = b_str.decode('latin-1')
>>> s_str
®ëV¤

In strings you can use hex and unicode escape characters:

>>> s_str_utf16 = '\\u00ae\\u00eb\\u0056\\u00a4\\u0089'
>>> s_str_utf16
®ëV¤

>>> s_str_utf32 = '\\U000000ae\\U000000eb\\U00000056\\U000000a4\\U00000089'
>>> s_str_utf32
®ëV¤
"""

def feature90():
    """String and byte literals"""
    print('String and byte literals')
    print('========================\n')
    print(':py:mod:`codesnippets.feature90`')
    print('--------------------------------\n')
    print("In bytes literals only ``\\\\x`` escapes can be used!")
    print()
    print(r">>> b_str = b'\\xae\\xeb\\x56\\xa4\\x89'")
    b_str = b'\xae\xeb\x56\xa4\x89'
    print()
    print(">>> s_str = b_str.decode('latin-1')")
    s_str = b_str.decode('latin-1')
    print(">>> s_str")
    print(s_str)
    print()
    print("In strings you can use hex and unicode escape characters:\n")
    print(r">>> s_str_utf16 = '\\u00ae\\u00eb\\u0056\\u00a4\\u0089'")
    s_str_utf16 = "\u00ae\u00eb\u0056\u00a4\u0089"
    print(">>> s_str_utf16")
    print(s_str_utf16)
    print()
    print(r">>> s_str_utf32 = '\\U000000ae\\U000000eb\\U00000056\\U000000a4\\U00000089'")
    s_str_utf32 = "\U000000ae\U000000eb\U00000056\U000000a4\U00000089"
    print(">>> s_str_utf32")
    print(s_str_utf32)
    print(80*'-')
