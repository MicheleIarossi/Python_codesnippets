##    Python codesnippets - Adding methods to classes
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
# Feature 111
#

"""
Adding methods to classes
=========================

:py:mod:`codesnippets.feature111`
---------------------------------

A metaclass is used for adding methods to a class.

The following functions are added to a class:

.. code-block:: Python

    def method2(self):
        return self.value + 3;
    def method3(self,param):
        return self.value + param;

This is the metaclass definition:

.. code-block:: Python

    class Extender(type):
        \"""extender class\"""
        def __new__(cls,classname,superclass,classdict):
            classdict['method2'] = method2
            classdict['method3'] = method3
            return type.__new__(cls,classname,superclass,classdict)

This is the class to be extended:

>>> class Client(metaclass=Extender):
        \"""client class\"""
        def __init__(self,param):
            self.value = param
        def method1(self):
            \"""a method\"""
            return self.value +8

When an instance is created, all methods are available:

>>> obj = Client(6)

>>> obj.method1()
14

>>> obj.method2()
9

>>> obj.method3(4)
10

.. seealso:: :doc:`Metaclass<feature110>`
"""

def feature111():
    """Adding methods to classes"""
    print('Adding methods to classes')
    print('=========================\n')
    print(':py:mod:`codesnippets.feature111`')
    print('---------------------------------\n')
    print("A metaclass is used for adding methods to a class.\n")
    print("The following functions are added to a class:\n")
    print('.. code-block:: Python\n')
    print("""    def method2(self):
        return self.value + 3
    def method3(self,param):
        return self.value + param
        """)
    def method2(self):
        return self.value + 3
    def method3(self,param):
        return self.value + param
    print("This is the metaclass definition:\n")
    print('.. code-block:: Python\n')
    print("""    class Extender(type):
        \\\"""extender class\\\"""
        def __new__(cls,classname,superclass,classdict):
            classdict['method2'] = method2
            classdict['method3'] = method3
            return type.__new__(cls,classname,superclass,classdict)
        """)
    class Extender(type):
        """extender class"""
        def __new__(cls,classname,superclass,classdict):
            classdict['method2'] = method2
            classdict['method3'] = method3
            return type.__new__(cls,classname,superclass,classdict)
    print("This is the class to be extended:\n")
    print(""">>> class Client(metaclass=Extender):
        \\\"""client class\\\"""
        def __init__(self,param):
            self.value = param
        def method1(self):
            \\\"""a method\\\"""
            return self.value +8""")
    class Client(metaclass=Extender):
        """client class"""
        def __init__(self,param):
            self.value = param
        def method1(self):
            """a method"""
            return self.value +8
    print("\nWhen an instance is created, all methods are available:\n")
    print(">>> obj = Client(6)")
    obj = Client(6)
    print()
    print(">>> obj.method1()")
    print(obj.method1())
    print()
    print(">>> obj.method2()")
    print(obj.method2())
    print()
    print(">>> obj.method3(4)")
    print(obj.method3(4))
    print('\n.. seealso:: :doc:`Metaclass<feature110>`')
    print(80*'-')
