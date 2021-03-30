##    Python codesnippets - Type built-in function applied to classes and instances
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
Type built-in function applied to classes and instances
=======================================================

:py:mod:`codesnippets.feature75`
--------------------------------

The ``type`` built-in function returns an object decribing the type of the instance provided:

* when applied to an instance of a class, it provides a reference to the class
* when applied to a class, it provides a reference to a ``type`` object.

Consider the following class:

.. code-block:: Python

    class MyClass:
        pass

>>> my_obj = MyClass()

``type`` applied to an instance of a class provides a reference to that class:

>>> type(my_obj)
<class 'codesnippets.feature76.feature76.<locals>.MyClass'>

The referenced class object is the same:

>>> id(type(my_obj))
0x7fa558a27650

>>> id(MyClass)
0x7fa558a27650

``type`` applied to a class object class provides a reference to a ``type`` object:

>>> type(MyClass)
<class 'type'>
"""

def feature75():
    """Type built-in function applied to classes and instances"""
    print('Type built-in function applied to classes and instances')
    print('=======================================================\n')
    print(':py:mod:`codesnippets.feature75`')
    print('--------------------------------\n')

    print("The ``type`` built-in function returns an object decribing "
        "the type of the instance provided:\n")
    print('* when applied to an instance of a class, it provides a reference to the class')
    print('* when applied to a class, it provides a reference to a ``type`` object.\n')
    print('Consider the following class:\n')
    print('.. code-block:: Python\n')
    print("""    class MyClass:
        pass
        """)
    class MyClass:
        """my class"""
        pass
    print(">>> my_obj = MyClass()")
    my_obj = MyClass()
    print('\n``type`` applied to an instance of a class provides a reference to that class:\n')
    print(">>> type(my_obj)")
    print(type(my_obj))
    print('\nThe referenced class object is the same:\n')
    print(">>> id(type(my_obj))")
    print(f'0x{id(type(my_obj)):x}')
    print("\n>>> id(MyClass)")
    print(f'0x{id(MyClass):x}')
    print('\n``type`` applied to a class object class provides a reference to a ``type`` object:\n')
    print(">>> type(MyClass)")
    print(type(MyClass))
    print(80*'-')