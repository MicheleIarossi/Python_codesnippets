##    Python codesnippets - Built-in method resolution starts at the class
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
# Feature 76
#

"""
Built-in method resolution starts at the class
==============================================

:py:mod:`codesnippets.feature76`
--------------------------------

Built-in method resolution starts at the class and skips the instance.

This is equivalent to ``type(my_obj).__xxxxx__(my_obj,...)``, which means
that you have to override the built-in operations in the class itself.

Consider the following class:

.. code-block:: Python

    class MyClass:
        \"""a class\"""
        def __init__(self,valstr):
            self.data = valstr

and the following object:

>>> my_obj = MyClass('hello')

When indexed, an exception is thrown since the instance has no ``__getitem__`` built-in defined:

>>> my_obj[2]
	--> Exception: 'MyClass' object is not subscriptable
	Instance has no __getitem__ built-in defined

But ``__getitem__`` can be added to the instance itself:

>>> def my_getitem(self,index):
        return self.data[index]

>>> my_obj.__getitem__ = my_getitem

If the method is explicitely called, then it works:

>>> my_obj.__getitem__(my_obj,2)
l

But if it is called as a built-in operation, it fails because the
instance is skipped and the operation is not overloaded in the class:

>>> my_obj[2]
	--> Exception: 'MyClass' object is not subscriptable
	__getitem__ is not called! Equivalent to type(my_obj).__getitem__(my_obj,idx)
	and __getitem__ is not overridden in the class!

The ``__getitem__`` built-in method needs to be overridden in
the class in order to avoid such exception.

.. seealso:: :doc:`Built-in operations cannot be delegated via __getattr__<feature74>`
"""

def feature76():
    """Built-in method resolution starts at the class"""
    print('Built-in method resolution starts at the class')
    print('==============================================\n')
    print(':py:mod:`codesnippets.feature76`')
    print('--------------------------------\n')
    print('Built-in method resolution starts at the class and skips the instance.\n')
    print('This is equivalent to ``type(my_obj).__xxxxx__(my_obj,...)``, which means\nthat '
          'you have to override the built-in operations in the class itself.\n')
    print('Consider the following class:\n')
    print('.. code-block:: Python\n')
    print("""    class MyClass:
        \\\"""a class\\\"""
        def __init__(self,valstr):
            self.data = valstr
        """)
    class MyClass:
        """a class"""
        def __init__(self,valstr):
            self.data = valstr
    print('and the following object:\n')
    print(">>> my_obj = MyClass('hello')")
    my_obj = MyClass('hello')
    print('\nWhen indexed, an exception is thrown since the instance has no '
          '``__getitem__`` built-in defined:\n')
    print(">>> my_obj[2]")
    try:
        print(my_obj[2])
    except TypeError as exc:
        print('\t--> Exception: ' + str(exc))
        print('\tInstance has no __getitem__ built-in defined')
    print("\nBut ``__getitem__`` can be added to the instance itself:\n")
    def my_getitem(self,index):
        return self.data[index]
    print(""">>> def my_getitem(self,index):
        return self.data[index]
        """)
    print(">>> my_obj.__getitem__ = my_getitem")
    my_obj.__getitem__ = my_getitem
    print("\nIf the method is explicitely called, then it works:\n")
    try:
        print(">>> my_obj.__getitem__(my_obj,2)")
        print(my_obj.__getitem__(my_obj,2))
    except TypeError as exc:
        print('\t--> Exception: ' + str(exc))
        print('\tInstance has no __getitem__ built-in defined')
    print("\nBut if it is called as a built-in operation, it fails because the")
    print("instance is skipped and the operation is not overloaded in the class:\n")
    try:
        print(">>> my_obj[2]")
        print(my_obj[2])
    except TypeError as exc:
        print('\t--> Exception: ' + str(exc))
        print('\t__getitem__ is not called! Equivalent to type(my_obj).__getitem__(my_obj,idx)')
        print('\tand __getitem__ is not overridden in the class!')
    print("\nThe ``__getitem__`` built-in method needs to be overridden in\nthe class in order to "
        "avoid such exception.")
    print('\n.. seealso:: :doc:`Built-in operations cannot be '
          'delegated via __getattr__<feature75>`')
    print(80*'-')
