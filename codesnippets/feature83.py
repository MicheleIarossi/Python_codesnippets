##    Python codesnippets - Constructor calls with multiple inheritance
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
# Feature 83
#

"""
Constructor calls with multiple inheritance
===========================================

:py:mod:`codesnippets.feature83`
--------------------------------

If no constructor is provided, Python calls the lowest and leftmost
constructor that is present in the inheritance hierarchy!

Given the following hierarchy of classes:

.. code-block:: Python

    class ClassA:
        \"""a class\"""
        def __init__(self):
            print('	-> ClassA.__init__')
        def __repr__(self):
            return 'ClassA()'

    class ClassB(ClassA):
        \"""a derived class\"""
        def __init__(self):
            print('	-> ClassB.__init__')
        def __repr__(self):
            return 'ClassB()'

    class ClassC(ClassA):
        \"""another derived class\"""
        def __init__(self):
            print('	-> ClassC.__init__')
        def __repr__(self):
            return 'ClassC()'

    class ClassD(ClassB):
        \"""yet another derived class\"""
        def __init__(self):
            print('	-> ClassD.__init__')
        def __repr__(self):
            return 'ClassD()'

    class ClassE(ClassC,ClassD):
        \"""multiple inheritance class\"""
        def __repr__(self):
            return 'ClassE()'

and an instance of ``ClassE``:

>>> obj_e = ClassE()
	-> ClassC.__init__

Notice that only the construtor of the ``ClassC`` is called!
"""

def feature83():
    """Constructor calls with multiple inheritance"""
    print('Constructor calls with multiple inheritance')
    print('===========================================\n')
    print(':py:mod:`codesnippets.feature83`')
    print('--------------------------------\n')
    print("If no constructor is provided, Python calls the lowest and leftmost")
    print("constructor that is present in the inheritance hierarchy!\n")
    print('Given the following hierarchy of classes:\n')
    print('.. code-block:: Python\n')
    print("""    class ClassA:
        \\\"""a class\\\"""
        def __init__(self):
            print('\t-> ClassA.__init__')
        def __repr__(self):
            return 'ClassA()'
        """)
    class ClassA:
        """a class"""
        def __init__(self):
            print('\t-> ClassA.__init__')
        def __repr__(self):
            """overloads repr operator"""
            return 'ClassA()'
    print("""    class ClassB(ClassA):
        \\\"""a derived class\\\"""
        def __init__(self):
            print('\t-> ClassB.__init__')
        def __repr__(self):
            return 'ClassB()'
        """)
    class ClassB(ClassA):
        """a derived class"""
        def __init__(self):
            print('\t-> ClassB.__init__')
        def __repr__(self):
            """overloads repr operator"""
            return 'ClassB()'
    print("""    class ClassC(ClassA):
        \\\"""another derived class\\\"""
        def __init__(self):
            print('\t-> ClassC.__init__')
        def __repr__(self):
            return 'ClassC()'
        """)
    class ClassC(ClassA):
        """another derived class"""
        def __init__(self):
            print('\t-> ClassC.__init__')
        def __repr__(self):
            """overloads repr operator"""
            return 'ClassC()'
    print("""    class ClassD(ClassB):
        \\\"""yet another derived class\\\"""
        def __init__(self):
            print('\t-> ClassD.__init__')
        def __repr__(self):
            return 'ClassD()'
        """)
    class ClassD(ClassB):
        """yet another derived class"""
        def __init__(self):
            print('\t-> ClassD.__init__')
        def __repr__(self):
            """overloads repr operator"""
            return 'ClassD()'
    print("""    class ClassE(ClassC,ClassD):
        \\\"""multiple inheritance class\\\"""
        def __repr__(self):
            return 'ClassE()'
        """)
    class ClassE(ClassC,ClassD):
        """multiple inheritance class"""
        def __repr__(self):
            """overloads repr operator"""
            return 'ClassE()'
    print('and an instance of ``ClassE``:\n')
    print('>>> obj_e = ClassE()')
    obj_e = ClassE()
    print('\nNotice that only the construtor of the ``ClassC`` is called!')
    print(80*'-')
