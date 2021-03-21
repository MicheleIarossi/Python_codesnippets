##    Python codesnippets - Unicode text
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
# Feature 89
#

"""
Unicode text
============

:py:mod:`codesnippets.feature89`
--------------------------------

Unicode escapes can be used.

.. note:: ASCII encoding works only if 7 bit representation is possible!

>>> a_str = '\u00d3\u00e8'
>>> a_str
Óè

>>> len(a_str)
2

>>> a_str_enc = a_str.encode('utf-8')

>>> list(a_str_enc)
[195, 147, 195, 168]

>>> len(a_str_enc)
4

ASCII encoding fails in this case because 7 bits are not enough!

>>> list(a_str.encode('ascii'))
UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)

Decoding provides the original string:

>>> a_str_enc.decode('utf-8')
Óè
>>> a_str == a_str_enc.decode('utf-8')
True
"""

def feature89():
    """Unicode text"""
    print('Unicode text')
    print('============\n')
    print(':py:mod:`codesnippets.feature89`')
    print('--------------------------------\n')
    print("Unicode escapes can be used.\n")
    print(".. note:: ASCII encoding works only if 7 bit representation is possible!\n")
    print(r">>> a_str = '\u00d3\u00e8'")
    a_str = '\u00d3\u00e8'
    print(">>> a_str")
    print(a_str)
    print("\n>>> len(a_str)")
    print(len(a_str))
    print("\n>>> a_str_enc = a_str.encode('utf-8')")
    a_str_enc = a_str.encode('utf-8')
    print("\n>>> list(a_str_enc)")
    print(list(a_str_enc))
    print("\n>>> len(a_str_enc)")
    print(len(a_str_enc))
    print()
    print('ASCII encoding fails in this case because 7 bits are not enough!\n')
    print(">>> list(a_str.encode('ascii'))")
    try:
        print(list(a_str.encode('ascii')))
    except UnicodeEncodeError as exc:
        print(exc.__class__.__name__ + ': ' + str(exc))
    finally:
        print()
    print('Decoding provides the original string:\n')
    print(">>> a_str_enc.decode('utf-8')")
    print(a_str_enc.decode('utf-8'))
    print(">>> a_str == a_str_enc.decode('utf-8')")
    print(a_str == a_str_enc.decode('utf-8'))
    print(80*'-')
