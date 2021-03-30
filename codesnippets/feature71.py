##    Python codesnippets - Pseudoprivate class attributes
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
# Feature 71
#

"""
Pseudoprivate class attributes
==============================

:py:mod:`codesnippets.feature71`
--------------------------------

If attributes in a class hierarchy have the same names, then some
unintended attribute hiding might occur.
Pseudoprivate class attributes solve this problem by adding
the name of the class in front of the attribute name:

.. code-block:: Python

    class MyClass:
        \"""my class\"""
        def __init__(self,val):
            self.__val = val
        def __repr__(self):
            return 'MyClass(val=%r)' % (self.__val)

>>> an_obj = MyClass(5)
>>> an_obj.__dict__.keys()
['_MyClass__val']

Notice how the class name has been added in front of ``__val``:

>>> an_obj._MyClass__val
5
"""

def feature71():
    """Pseudoprivate class attributes"""
    print('Pseudoprivate class attributes')
    print('==============================\n')
    print(':py:mod:`codesnippets.feature71`')
    print('--------------------------------\n')
    print('If attributes in a class hierarchy have the same names, then some')
    print('unintended attribute hiding might occur.')
    print('Pseudoprivate class attributes solve this problem by adding')
    print('the name of the class in front of the attribute name:\n')
    class MyClass:
        """a class"""
        def __init__(self,val):
            self.__val = val
        def __repr__(self):
            """overloads repr operator"""
            return 'MyClass(val=%r)' % (self.__val)
    print('.. code-block:: Python\n')
    print("""    class MyClass:
        \\\"""my class\\\"""
        def __init__(self,val):
            self.__val = val
        def __repr__(self):
            return 'MyClass(val=%r)' % (self.__val)
            """)
    print('>>> an_obj = MyClass(5)')
    an_obj = MyClass(5)
    print('>>> an_obj.__dict__.keys()')
    print(list(an_obj.__dict__.keys()))
    print('\nNotice how the class name has been added in front of ``__val``:\n')
    print('>>> an_obj._MyClass__val')
    print(an_obj._MyClass__val)
    print(80*'-')