##    Python codesnippets - Type
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
# Feature 107
#

"""
Type
====

:py:mod:`codesnippets.feature107`
---------------------------------

Instances are made from classes, but classes are instances of ``type``.
A class object is an instance of a ``type`` object:

>>> class MyClass:
        \"""my class\"""
        pass

>>> an_obj = MyClass()

>>> (type(an_obj), an_obj.__class__)
(<class 'codesnippets.feature107.feature107.<locals>.MyClass'>,
 <class 'codesnippets.feature107.feature107.<locals>.MyClass'>)

>>> (type(MyClass), MyClass.__class__)
(<class 'type'>, <class 'type'>)
"""

def feature107():
    """Type"""
    print('Type')
    print('====\n')
    print(':py:mod:`codesnippets.feature107`')
    print('---------------------------------\n')
    print("Instances are made from classes, but classes are instances of ``type``.")
    print("A class object is an instance of a ``type`` object:\n")
    print(""">>> class MyClass:
        \\\"""my class\\\"""
        pass
          """)
    class MyClass:
        """my class"""
        pass
    print(">>> an_obj = MyClass()")
    an_obj = MyClass()
    print()
    print(">>> (type(an_obj), an_obj.__class__)")
    print((type(an_obj), an_obj.__class__))
    print()
    print(">>> (type(MyClass), MyClass.__class__)")
    print((type(MyClass), MyClass.__class__))
    print(80*'-')
