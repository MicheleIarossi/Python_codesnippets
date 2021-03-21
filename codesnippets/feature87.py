##    Python codesnippets - String type conversions
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
String type conversions
=======================

:py:mod:`codesnippets.feature87`
--------------------------------

From ``str`` to ``bytes``: ``str.encode(encoding)`` and ``bytes(str, encoding)``

From ``bytes`` to ``str``  : ``bytes.decode(encoding)`` and ``str(bytes, encoding)``

>>> import sys, locale

Get the platform name:

>>> sys.platform
darwin

Get the default encoding on this platform:

>>> encoding = sys.getdefaultencoding()
>>> encoding
utf-8

A simple string:

>>> a_str = 'hello, world'

From ``str`` to ``bytes`` with ``str.encode()`` which uses
the default encoding if no parameter is given:

>>> b_bytes = a_str.encode()
>>> b_bytes
b'hello, world'

or

>>> b_bytes = bytes(a_str,encoding) # requires the encoding type!
>>> b_bytes
b'hello, world'

From ``bytes`` to ``str`` with ``bytes.decode()`` which uses
the default encoding if no parameter is given:

>>> b_bytes.decode()
hello, world
>>> b_bytes.decode() == a_str
True

or

>>> str(b_bytes,encoding) # requires the encoding type!
hello, world
>>> str(b_bytes,encoding) == a_str
True
"""

import sys

def feature87():
    """String type conversions"""
    print('String type conversions')
    print('=======================\n')
    print(':py:mod:`codesnippets.feature87`')
    print('--------------------------------\n')
    print("From ``str`` to ``bytes``: ``str.encode(encoding)`` and ``bytes(str, encoding)``\n")
    print("From ``bytes`` to ``str``  : ``bytes.decode(encoding)`` and ``str(bytes, encoding)``\n")
    print(">>> import sys, locale")
    print("\nGet the platform name:")
    print("\n>>> sys.platform")
    print(sys.platform)
    print("\nGet the default encoding on this platform:")
    print("\n>>> encoding = sys.getdefaultencoding()")
    encoding = sys.getdefaultencoding()
    print(">>> encoding")
    print(encoding)
    print('\nA simple string:')
    print("\n>>> a_str = 'hello, world'")
    a_str = 'hello, world'
    print("\nFrom ``str`` to ``bytes`` with ``str.encode()`` which uses\nthe default"
          " encoding if no parameter "
          "is given:")
    print("\n>>> b_bytes = a_str.encode()")
    b_bytes = a_str.encode()
    print(">>> b_bytes")
    print(b_bytes)
    print('\nor')
    print("\n>>> b_bytes = bytes(a_str,encoding) # requires the encoding type!")
    b_bytes = bytes(a_str,encoding)
    print(">>> b_bytes")
    print(b_bytes)
    print("\nFrom ``bytes`` to ``str`` with ``bytes.decode()`` which uses\nthe default"
          " encoding if no parameter "
          "is given:")
    print("\n>>> b_bytes.decode()")
    print(b_bytes.decode())
    print(">>> b_bytes.decode() == a_str")
    print(b_bytes.decode() == a_str)
    print('\nor')
    print("\n>>> str(b_bytes,encoding) # requires the encoding type!")
    print(str(b_bytes,encoding))
    print(">>> str(b_bytes,encoding) == a_str")
    print(str(b_bytes,encoding) == a_str)
    print(80*'-')
