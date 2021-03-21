##    Python codesnippets - Built-in operations cannot be delegated via __getattr__
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
# Feature 75
#

"""
Built-in operations cannot be delegated via ``__getattr__``
===========================================================

:py:mod:`codesnippets.feature75`
--------------------------------

In a class, you cannot delegate built-in operations via ``__getattr__``.
You have to override the built-in operations in the class itself.

Consider the following class:

.. code-block:: Python

    class MyClass:
        \"""a class\"""
        def __init__(self,valstr):
            self.data = valstr
        def __getattr__(self,attrstr):
            return getattr(self.data,attrstr)

and the following object:

>>> my_obj = MyClass('hello')

The ``__getattr__`` method forwards every undefined attribute fetch to the ``self.data``
object, but not for built-in operations like indexing:

>>> my_obj[2]
	--> Exception: 'MyClass' object is not subscriptable
	__getattr__ is not called!

This is equivalent to ``type(my_obj).__getitem__(my_obj,2)`` and ``__getitem__``
is not overridden in the class!

The ``__getitem__`` built-in method needs to be overridden in order to avoid such exception:

.. code-block:: Python

    class MyClass:
        def __init__(self,valstr):
            self.data = valstr
        def __getattr__(self,attrstr):
            return getattr(self.data,attrstr)
        def __getitem__(self,index):
            return self.data[index]

The same object is created and indexed again:

>>> my_obj = MyClass('hello')

This works as expected:

>>> [x_var for x_var in my_obj]
['h', 'e', 'l', 'l', 'o']"""

def feature75():
    """Built-in operations cannot be delegated via __getattr__"""
    print('Built-in operations cannot be delegated via ``__getattr__``')
    print('===========================================================\n')
    print(':py:mod:`codesnippets.feature75`')
    print('--------------------------------\n')
    print('In a class, you cannot delegate built-in operations via ``__getattr__``.')
    print('You have to override the built-in operations in the class itself.\n')
    print('Consider the following class:\n')
    print('.. code-block:: Python\n')
    print("""    class MyClass:
        \\\"""my class\\\"""
        def __init__(self,valstr):
            self.data = valstr
        def __getattr__(self,attrstr):
            return getattr(self.data,attrstr)
        """)
    class MyClass:
        """my class"""
        def __init__(self,valstr):
            self.data = valstr
        def __getattr__(self,attrstr):
            return getattr(self.data,attrstr)
    print('and the following object:\n')
    print(">>> my_obj = MyClass('hello')")
    my_obj = MyClass('hello')
    print('\nThe ``__getattr__`` method forwards every undefined attribute fetch '
          'to the ``self.data``\nobject, but not for built-in operations like indexing:\n')
    print(">>> my_obj[2]")
    try:
        print(my_obj[2])
    except TypeError as exc:
        print('\t--> Exception: ' + str(exc))
        print('\t__getattr__ is not called!\n')
    print('This is equivalent to ``type(my_obj).__getitem__(my_obj,2)`` '
          'and ``__getitem__``\nis not overridden in the class!\n')
    print("The ``__getitem__`` built-in method needs to be overridden in order to "
        "avoid such exception:\n")
    print('.. code-block:: Python\n')
    print("""    class MyClass:
        def __init__(self,valstr):
            self.data = valstr
        def __getattr__(self,attrstr):
            return getattr(self.data,attrstr)
        def __getitem__(self,index):
            return self.data[index]
        """)
    class MyClass:
        """a class"""
        def __init__(self,valstr):
            self.data = valstr
        def __getattr__(self,attrstr):
            return getattr(self.data,attrstr)
        def __getitem__(self,index):
            return self.data[index]
    print('The same object is created and indexed again:\n')
    print(">>> my_obj = MyClass('hello')")
    my_obj = MyClass('hello')
    print('\nThis works as expected:\n')
    print(">>> [x_var for x_var in my_obj]")
    print([x_var for x_var in my_obj])
    print(80*'-')
