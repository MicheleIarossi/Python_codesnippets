##    Python codesnippets - Usage of super() in diamond class trees
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
Usage of super() in diamond class trees
=======================================

:py:mod:`codesnippets.feature83`
--------------------------------

Each ``super()`` call selects the method from a next class that implements the
requested method following it in the MRO ordering of the class of the
``self`` subject of the method call. This selection process chooses
the first class following the calling class having the requested method.

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
            super().__init__()
        def __repr__(self):
            return 'ClassB()'

    class ClassC(ClassA):
        \"""another derived class\"""
        def __init__(self):
            print('	-> ClassC.__init__')
            super().__init__()
        def __repr__(self):
            return 'ClassC()'

    class ClassD(ClassB,ClassC):
        \"""multiple inheritance class\"""
        def __init__(self):
            print('	-> ClassD.__init__')
            super().__init__()
        def __repr__(self):
            return 'ClassD()'

and an instance of ``ClassD``:

>>> obj_d = ClassD()
	-> ClassD.__init__
	-> ClassB.__init__
	-> ClassC.__init__
	-> ClassA.__init__

>>> ClassD.__mro__
(<class 'codesnippets.feature83.feature83.<locals>.ClassD'>,
<class 'codesnippets.feature83.feature83.<locals>.ClassB'>,
<class 'codesnippets.feature83.feature83.<locals>.ClassC'>,
<class 'codesnippets.feature83.feature83.<locals>.ClassA'>,
<class 'object'>)

When the constructor of ``classD`` is called, ``self`` is an instance of the ``classD``, so
the MRO of the ``classD`` is considered as printed above, in all the calls.

When the constructor of ``classD`` calls ``super().__init__()`` then the next class in
the MRO following the ``classD`` that has an ``__init__`` function is called.
In this case it is the ``classB``.

When the constructor of the ``classB`` calls ``super().__init__()`` then the next class in
the MRO following the ``classB`` that has an ``__init__`` function is called.
In this case it is the ``classC``.

When the constructor of the ``classC`` calls ``super().__init__()`` then the next class in
the MRO following the ``classC`` that has an ``__init__`` function is called.
In this case it is the ``classA``.

The constructor of the ``classA`` has no ``super`` call and so the chain stops.

.. seealso:: :doc:`Method resolution order (MRO)<feature78>`
"""

def feature83():
    """Usage of super() in diamond class trees"""
    print('Usage of super() in diamond class trees')
    print('=======================================\n')
    print(':py:mod:`codesnippets.feature83`')
    print('--------------------------------\n')
    print("Each ``super()`` call selects the method from a next class that implements the")
    print("requested method following it in the MRO ordering of the class of the")
    print("``self`` subject of the method call. This selection process chooses")
    print("the first class following the calling class having the requested method.\n")
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
            super().__init__()
        def __repr__(self):
            return 'ClassB()'
        """)
    class ClassB(ClassA):
        """a derived class"""
        def __init__(self):
            print('\t-> ClassB.__init__')
            super().__init__()
        def __repr__(self):
            """overloads repr operator"""
            return 'ClassB()'
    print("""    class ClassC(ClassA):
        \\\"""another derived class\\\"""
        def __init__(self):
            print('\t-> ClassC.__init__')
            super().__init__()
        def __repr__(self):
            return 'ClassC()'
        """)
    class ClassC(ClassA):
        """another derived class"""
        def __init__(self):
            print('\t-> ClassC.__init__')
            super().__init__()
        def __repr__(self):
            """overloads repr operator"""
            return 'ClassC()'
    print("""    class ClassD(ClassB,ClassC):
        \\\"""multiple inheritance class\\\"""
        def __init__(self):
            print('\t-> ClassD.__init__')
            super().__init__()
        def __repr__(self):
            return 'ClassD()'
        """)
    class ClassD(ClassB,ClassC):
        """multiple inheritance class"""
        def __init__(self):
            print('\t-> ClassD.__init__')
            super().__init__()
        def __repr__(self):
            """overloads repr operator"""
            return 'ClassD()'
    print('and an instance of ``ClassD``:\n')
    print('>>> obj_d = ClassD()')
    obj_d = ClassD()
    print('\n>>> ClassD.__mro__')
    print(ClassD.__mro__)
    print("\nWhen the constructor of ``classD`` is called, ``self`` is "
          "an instance of the ``classD``, so")
    print("the MRO of the ``classD`` is considered as printed above, in all the calls.\n")
    print("When the constructor of ``classD`` calls ``super().__init__()`` then "
          "the next class in")
    print("the MRO following the ``classD`` that has an ``__init__`` function"
          " is called.")
    print("In this case it is the ``classB``.\n")
    print("When the constructor of the ``classB`` calls ``super().__init__()`` then"
          "the next class in")
    print("the MRO following the ``classB`` that has an ``__init__`` function is called.")
    print("In this case it is the ``classC``.\n")
    print("When the constructor of the ``classC`` calls ``super().__init__()`` then"
          " the next class in")
    print("the MRO following the ``classC`` that has an ``__init__`` function is called.")
    print("In this case it is the ``classA``.\n")
    print("The constructor of the ``classA`` has no ``super`` call and so the chain stops.")
    print('\n.. seealso:: :doc:`Method resolution order (MRO)<feature78>`')
    print(80*'-')