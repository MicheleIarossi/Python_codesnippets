##    Python codesnippets - Proxy pattern
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
# Feature 96
#

"""
Proxy pattern
=============

:py:mod:`codesnippets.feature96`
--------------------------------

An object is embedded in a wrapper class that delegates all accesses
to its embedded opbject:

.. code-block:: Python

    class Wrapper:
        \"""a wrapper class\"""
        def __init__(self,obj):
            self.embedded_obj = obj
        def __getattr__(self,attr):
            print("__getattr__: " + attr)
            return getattr(self.embedded_obj,attr)

>>> a_wrapper = Wrapper([1,2,3])

>>> a_wrapper.append(4)
__getattr__: append

>>> print(a_wrapper.embedded_obj)
[1, 2, 3, 4]
"""

def feature96():
    """Proxy pattern"""
    print('Proxy pattern')
    print('=============\n')
    print(':py:mod:`codesnippets.feature96`')
    print('--------------------------------\n')
    print('An object is embedded in a wrapper class that delegates all accesses')
    print('to its embedded opbject:\n')
    class Wrapper:
        """a wrapper class"""
        def __init__(self,obj):
            self.embedded_obj = obj
        def __getattr__(self,attr):
            """overloads getattr operator"""
            print("__getattr__: " + attr)
            return getattr(self.embedded_obj,attr)
    print('.. code-block:: Python\n')
    print("""    class Wrapper:
        \\\"""a wrapper class\\\"""
        def __init__(self,obj):
            self.embedded_obj = obj
        def __getattr__(self,attr):
            print("__getattr__: " + attr)
            return getattr(self.embedded_obj,attr)
        """)
    print(">>> a_wrapper = Wrapper([1,2,3])")
    a_wrapper = Wrapper([1,2,3])
    print("\n>>> a_wrapper.append(4)")
    a_wrapper.append(4)
    print("\n>>> print(a_wrapper.embedded_obj)")
    print(a_wrapper.embedded_obj)
    print(80*'-')