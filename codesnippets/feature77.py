##    Python codesnippets - Method resolution order (MRO)
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
# Feature 77
#

"""
Method resolution order (MRO)
=============================

:py:mod:`codesnippets.feature77`
--------------------------------

The attribute ``__mro__`` provides the list of classes used for method resolution.

Consider the following hierarchy of classes:

.. code-block:: Python

    class ClassA:
        \"""a class\"""
        def __repr__(self):
            return 'ClassA()'

    class ClassB(ClassA):
        \"""a derived class\"""
        def __repr__(self):
            return 'ClassB()'

    class ClassC(ClassA):
        \"""another derived class\"""
        def __repr__(self):
            return 'ClassC()'

    class ClassD(ClassB,ClassC):
        \"""multiple inheritance class\"""
        def __repr__(self):
            return 'ClassD()'

>>> ClassD.__mro__
(<class 'codesnippets.feature77.feature77.<locals>.ClassD'>,
<class 'codesnippets.feature77.feature77.<locals>.ClassB'>,
<class 'codesnippets.feature77.feature77.<locals>.ClassC'>,
<class 'codesnippets.feature77.feature77.<locals>.ClassA'>,
<class 'object'>)
"""

def feature77():
    """Method resolution order (MRO)"""
    print('Method resolution order (MRO)')
    print('=============================\n')
    print(':py:mod:`codesnippets.feature77`')
    print('--------------------------------\n')
    print('The attribute ``__mro__`` provides the list of classes used for method resolution.\n')
    print('Consider the following hierarchy of classes:\n')
    print('.. code-block:: Python\n')
    print("""    class ClassA:
        \\\"""a class\\\"""
        def __repr__(self):
            return 'ClassA()'
        """)
    class ClassA:
        """a class"""
        def __repr__(self):
            """overloads repr operator"""
            return 'ClassA()'
    print("""    class ClassB(ClassA):
        \\\"""a derived class\\\"""
        def __repr__(self):
            return 'ClassB()'
        """)
    class ClassB(ClassA):
        """a derived class"""
        def __repr__(self):
            """overloads repr operator"""
            return 'ClassB()'
    print("""    class ClassC(ClassA):
        \\\"""another derived class\\\"""
        def __repr__(self):
            return 'ClassC()'
        """)
    class ClassC(ClassA):
        """another derived class"""
        def __repr__(self):
            """overloads repr operator"""
            return 'ClassC()'
    print("""    class ClassD(ClassB,ClassC):
        \\\"""multiple inheritance class\\\"""
        def __repr__(self):
            return 'ClassD()'
        """)
    class ClassD(ClassB,ClassC):
        """multiple inheritance class"""
        def __repr__(self):
            """overloads repr operator"""
            return 'ClassD()'
    print('>>> ClassD.__mro__')
    print(ClassD.__mro__)
    print(80*'-')
