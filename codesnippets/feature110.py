##    Python codesnippets - Metaclass
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
# Feature 110
#

"""
Metaclass
=========

:py:mod:`codesnippets.feature110`
---------------------------------

Metaclasses are used for generating classes.

A Metaclass inherits from the ``type`` class:

.. code-block:: Python

    class MetaClass(type):
        \"""a metaclass\"""
        def __new__(cls,classname,superclass,classdict):
            print(f"	-> Inside MetaClass.__new__:")
            print(f"	-> cls        -> {cls}")
            print(f"	-> classname  -> {classname}")
            print(f"	-> superclass -> {superclass}")
            print(f"	-> classdict  -> {classdict}")
            return type.__new__(cls,classname,superclass,classdict)
        def __init__(cls,classname,superclass,classdict):
            print(f"	-> Inside MetaClass.__init__:")
            print(f"	-> cls        -> {cls}")
            print(f"	-> classname  -> {classname}")
            print(f"	-> superclass -> {superclass}")
            print(f"	-> classdict  -> {classdict}")

Base classes can be also combined with metaclasses:

.. code-block:: Python

    class BaseClass:
        \"""a base class\"""
        def __init__(self,param=0):
            print(f"	-> Inside BaseClass.__init__: param = {param}")
            self.var_base = param
        def method(self,param=0):
            \"""a method\"""
            print(f"	-> Inside BaseClass.method: param = {param}")
            self.var_base += param

A normal class managed by a metaclass:

>>> class NormalClass(BaseClass,metaclass=MetaClass):
        \"""a normal class\"""
        def __init__(self,param=0):
            print(f"	-> Inside NormalClass.__init__: param = {param}")
            self.var = param
        def method(self,param=0):
            \"""a method\"""
            print(f"	-> Inside NormalClass.method: param = {param}")
            self.var += self.var_base + param
	-> Inside MetaClass.__new__:
	-> cls        -> <class 'codesnippets.feature110.feature110.<locals>.MetaClass'>
	-> classname  -> NormalClass
	-> superclass -> (<class 'codesnippets.feature110.feature110.<locals>.BaseClass'>,)
	-> classdict  -> {'__module__': 'codesnippets.feature110',
	                  '__qualname__': 'feature110.<locals>.NormalClass',
	                  '__init__': <function feature110.<locals>.NormalClass.__init__ at 0x7f8d794d2af0>,
	                  'method': <function feature110.<locals>.NormalClass.method at 0x7f8d7949e4c0>}
	-> Inside MetaClass.__init__:
	-> cls        -> <class 'codesnippets.feature110.feature110.<locals>.NormalClass'>
	-> classname  -> NormalClass
	-> superclass -> (<class 'codesnippets.feature110.feature110.<locals>.BaseClass'>,)
	-> classdict  -> {'__module__': 'codesnippets.feature110',
	                  '__qualname__': 'feature110.<locals>.NormalClass',
	                  '__init__': <function feature110.<locals>.NormalClass.__init__ at 0x7f8d794d2af0>,
	                  'method': <function feature110.<locals>.NormalClass.method at 0x7f8d7949e4c0>}

Creating an instance of ``NormalClass``:

>>> obj = NormalClass()
	-> Inside NormalClass.__init__: param = 2
	-> Inside BaseClass.__init__: param = 0

>>> obj.var
2

>>> obj.method(3)
	-> Inside NormalClass.method: param = 3

>>> obj.var
5

.. seealso:: :doc:`Class statement protocol<feature109>`
"""

def feature110():
    """Metaclass"""
    print('Metaclass')
    print('=========\n')
    print(':py:mod:`codesnippets.feature110`')
    print('---------------------------------\n')
    print("Metaclasses are used for generating classes.\n")
    print("A Metaclass inherits from the ``type`` class:\n")
    print('.. code-block:: Python\n')
    print("""    class MetaClass(type):
        \\\"""a metaclass\\\"""
        def __new__(cls,classname,superclass,classdict):
            print(f"\t-> Inside MetaClass.__new__:")
            print(f"\t-> cls        -> {cls}")
            print(f"\t-> classname  -> {classname}")
            print(f"\t-> superclass -> {superclass}")
            print(f"\t-> classdict  -> {classdict}")
            return type.__new__(cls,classname,superclass,classdict)
        def __init__(cls,classname,superclass,classdict):
            print(f"\t-> Inside MetaClass.__init__:")
            print(f"\t-> cls        -> {cls}")
            print(f"\t-> classname  -> {classname}")
            print(f"\t-> superclass -> {superclass}")
            print(f"\t-> classdict  -> {classdict}")
	""")
    class MetaClass(type):
        """a metaclass"""
        def __new__(cls,classname,superclass,classdict):
            print(f"\t-> Inside MetaClass.__new__:")
            print(f"\t-> cls        -> {cls}")
            print(f"\t-> classname  -> {classname}")
            print(f"\t-> superclass -> {superclass}")
            print(f"\t-> classdict  -> {classdict}")
            return type.__new__(cls,classname,superclass,classdict)
        def __init__(cls,classname,superclass,classdict):
            print(f"\t-> Inside MetaClass.__init__:")
            print(f"\t-> cls        -> {cls}")
            print(f"\t-> classname  -> {classname}")
            print(f"\t-> superclass -> {superclass}")
            print(f"\t-> classdict  -> {classdict}")
    print("Base classes can be also combined with metaclasses:\n")
    print('.. code-block:: Python\n')
    print("""    class BaseClass:
        \\\"""a base class\\\"""
        def __init__(self,param=0):
            print(f"\t-> Inside BaseClass.__init__: param = {param}")
            self.var_base = param
        def method(self,param=0):
            \\\"""a method\\\"""
            print(f"\t-> Inside BaseClass.method: param = {param}")
            self.var_base += param
        """)
    class BaseClass:
        """a base class"""
        def __init__(self,param=0):
            print(f"\t-> Inside BaseClass.__init__: param = {param}")
            self.var_base = param
        def method(self,param=0):
            """a method"""
            print(f"\t-> Inside BaseClass.method: param = {param}")
            self.var_base += param
    print("A normal class managed by a metaclass:\n")
    print(""">>> class NormalClass(BaseClass,metaclass=MetaClass):
        \\\"""a normal class\\\"""
        def __init__(self,param=0):
            print(f"\t-> Inside NormalClass.__init__: param = {param}")
            self.var = param
        def method(self,param=0):
            \\\"""a method\\\"""
            print(f"\t-> Inside NormalClass.method: param = {param}")
            self.var += self.var_base + param""")
    class NormalClass(BaseClass,metaclass=MetaClass):
        """a normal class"""
        def __init__(self,param=0):
            print(f"\t-> Inside NormalClass.__init__: param = {param}")
            BaseClass.__init__(self)
            self.var = param
        def method(self,param=0):
            """a method"""
            print(f"\t-> Inside NormalClass.method: param = {param}")
            self.var += self.var_base + param
    print()
    print("Creating an instance of ``NormalClass``:\n")
    print(">>> obj = NormalClass()")
    obj = NormalClass(2)
    print("\n>>> obj.var")
    print(obj.var)
    print()
    print(">>> obj.method(3)")
    obj.method(3)
    print()
    print(">>> obj.var")
    print(obj.var)
    print('\n.. seealso:: :doc:`Class statement protocol<feature109>`')
    print(80*'-')