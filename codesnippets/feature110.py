##    Python codesnippets - Metaclass of a metaclass and __call__ overloading
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
Metaclass of a metaclass and ``__call__`` overloading
=====================================================

:py:mod:`codesnippets.feature110`
---------------------------------

A metaclass can be generated by another metaclass:

.. code-block:: Python

    class SuperMetaClass(type):
        \"""a super meta class\"""
        def __call__(cls,classname,superclass,classdict):
            print(f"	-> Inside SuperMetaClass.__call__")
            print(f"	-> cls -> {cls}")
            return type.__call__(cls,classname,superclass,classdict)
        def __init__(cls,classname,superclass,classdict):
            print(f"	-> Inside SuperMetaClass.__init__")
            print(f"	-> cls -> {cls}")

This metaclass is an instance of ``type``:

>>> type(SuperMetaClass)
<class 'type'>

The following metaclass is generated by the previous one:

>>> class SubMetaClass(type, metaclass=SuperMetaClass):
        \"""a sub meta class\"""
        def __new__(cls,classname,superclass,classdict):
            print(f"	-> Inside SubMetaClass.__new__")
            print(f"	-> cls -> {cls}")
            return type.__new__(cls,classname,superclass,classdict)
        def __init__(cls,classname,superclass,classdict):
            print(f"	-> Inside SubMetaClass.__init__")
            print(f"	-> cls -> {cls}")
	-> Inside SuperMetaClass.__init__
	-> cls -> <class 'codesnippets.feature110.feature110.<locals>.SubMetaClass'>

Remember that at the end of the class definition:

>>> SubMetaClass = SuperMetaClass(classname,superclass,dictattrib)

but since ``SuperMetaClass`` is an instance of type, the type object
is invoked, i.e. ``type.__call__`` is called which calls ``SuperMetaClass.__init__``!

The class object ``SubMetaClass`` is now an instance of ``SuperMetaClass``:

>>> type(SubMetaClass)
<class 'codesnippets.feature110.feature110.<locals>.SuperMetaClass'>

Base classes can be also combined with metaclasses:

.. code-block:: Python

    class BaseClass:
        \"""a base class\"""
        def __init__(self,param=0):
            print(f"	-> Inside BaseClass.__init__: param = {param}")
            self.var_base = param
        def method(self,param=0):
            print(f"	-> Inside BaseClass.method: param = {param}")
            self.var_base += param

A normal class managed by the metaclasses above:

>>> class NormalClass(BaseClass,metaclass=SubMetaClass):
        \"""a normal class\"""
        def __init__(self,param=0):
            print(f"	-> Inside NormalClass.__init__: param = {param}")
            self.var = param
        def method(self,param=0):
            print(f"	-> Inside NormalClass.method: param = {param}")
            self.var += self.var_base + param
	-> Inside SuperMetaClass.__call__
	-> cls -> <class 'codesnippets.feature110.feature110.<locals>.SubMetaClass'>
	-> Inside SubMetaClass.__new__
	-> cls -> <class 'codesnippets.feature110.feature110.<locals>.SubMetaClass'>
	-> Inside SubMetaClass.__init__
	-> cls -> <class 'codesnippets.feature110.feature110.<locals>.NormalClass'>

Remember that at the end of the class definition:

>>> NormalClass = SubMetaClass(classname,superclass,dictattrib)

but since ``SubMetaClass`` is an instance of ``SuperMetaClass``, then
``SuperMetaClass.__call__(SubMetaClass,...)`` is called which calls
``SubMetaClass.__new__(SubMetaClass,...)`` and ``SubMetaClass.__init__(NormalClass,...)``

The class object ``NormalClass`` is now an instance of ``SubMetaClass``:

>>> type(NormalClass)
<class 'codesnippets.feature110.feature110.<locals>.SubMetaClass'>

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

.. seealso:: :doc:`Metaclass<feature110>`
"""

def feature110():
    """Metaclass of a metaclass and __call__ overloading"""
    print('Metaclass of a metaclass and ``__call__`` overloading')
    print('=====================================================\n')
    print(':py:mod:`codesnippets.feature110`')
    print('---------------------------------\n')
    print("A metaclass can be generated by another metaclass:\n")
    print('.. code-block:: Python\n')
    print("""    class SuperMetaClass(type):
        \\\"""a super meta class\\\"""
        def __call__(cls,classname,superclass,classdict):
            print(f"\t-> Inside SuperMetaClass.__call__")
            print(f"\t-> cls -> {cls}")
            return type.__call__(cls,classname,superclass,classdict)
        def __init__(cls,classname,superclass,classdict):
            print(f"\t-> Inside SuperMetaClass.__init__")
            print(f"\t-> cls -> {cls}")
	""")
    class SuperMetaClass(type):
        """a super meta class"""
        def __call__(cls,classname,superclass,classdict):
            print(f"\t-> Inside SuperMetaClass.__call__")
            print(f"\t-> cls -> {cls}")
            return type.__call__(cls,classname,superclass,classdict)
        def __init__(cls,classname,superclass,classdict):
            print(f"\t-> Inside SuperMetaClass.__init__")
            print(f"\t-> cls -> {cls}")
    print("This metaclass is an instance of ``type``:\n")
    print(">>> type(SuperMetaClass)")
    print(type(SuperMetaClass))
    print("\nThe following metaclass is generated by the previous one:\n")
    print(""">>> class SubMetaClass(type, metaclass=SuperMetaClass):
        \\\"""a sub meta class\\\"""
        def __new__(cls,classname,superclass,classdict):
            print(f"\t-> Inside SubMetaClass.__new__")
            print(f"\t-> cls -> {cls}")
            return type.__new__(cls,classname,superclass,classdict)
        def __init__(cls,classname,superclass,classdict):
            print(f"\t-> Inside SubMetaClass.__init__")
            print(f"\t-> cls -> {cls}")""")
    class SubMetaClass(type, metaclass=SuperMetaClass):
        """a sub meta class"""
        def __new__(cls,classname,superclass,classdict):
            print(f"\t-> Inside SubMetaClass.__new__")
            print(f"\t-> cls -> {cls}")
            return type.__new__(cls,classname,superclass,classdict)
        def __init__(cls,classname,superclass,classdict):
            print(f"\t-> Inside SubMetaClass.__init__")
            print(f"\t-> cls -> {cls}")
    print("\nRemember that at the end of the class definition:\n")
    print(">>> SubMetaClass = SuperMetaClass(classname,superclass,dictattrib)\n")
    print("but since ``SuperMetaClass`` is an instance of type, the type object")
    print("is invoked, i.e. ``type.__call__`` is called which "
          "calls ``SuperMetaClass.__init__``!\n")
    print("The class object ``SubMetaClass`` is now an instance of ``SuperMetaClass``:\n")
    print(">>> type(SubMetaClass)")
    print(type(SubMetaClass))
    print("\nBase classes can be also combined with metaclasses:\n")
    print('.. code-block:: Python\n')
    print("""    class BaseClass:
        \\\"""a base class\\\"""
        def __init__(self,param=0):
            print(f"\t-> Inside BaseClass.__init__: param = {param}")
            self.var_base = param
        def method(self,param=0):
            print(f"\t-> Inside BaseClass.method: param = {param}")
            self.var_base += param
        """)
    class BaseClass:
        """a base class"""
        def __init__(self,param=0):
            print(f"\t-> Inside BaseClass.__init__: param = {param}")
            self.var_base = param
        def method(self,param=0):
            print(f"\t-> Inside BaseClass.method: param = {param}")
            self.var_base += param
    print("A normal class managed by the metaclasses above:\n")
    print(""">>> class NormalClass(BaseClass,metaclass=SubMetaClass):
        \\\"""a normal class\\\"""
        def __init__(self,param=0):
            print(f"\t-> Inside NormalClass.__init__: param = {param}")
            self.var = param
        def method(self,param=0):
            print(f"\t-> Inside NormalClass.method: param = {param}")
            self.var += self.var_base + param""")
    class NormalClass(BaseClass,metaclass=SubMetaClass):
        """a normal class"""
        def __init__(self,param=0):
            print(f"\t-> Inside NormalClass.__init__: param = {param}")
            BaseClass.__init__(self)
            self.var = param
        def method(self,param=0):
            print(f"\t-> Inside NormalClass.method: param = {param}")
            self.var += self.var_base + param
    print("\nRemember that at the end of the class definition:")
    print()
    print(">>> NormalClass = SubMetaClass(classname,superclass,dictattrib)")
    print()
    print("but since ``SubMetaClass`` is an instance of ``SuperMetaClass``, then")
    print("``SuperMetaClass.__call__(SubMetaClass,...)`` is called which calls")
    print("``SubMetaClass.__new__(SubMetaClass,...)`` and "
          "``SubMetaClass.__init__(NormalClass,...)``")
    print()
    print("The class object ``NormalClass`` is now an instance of ``SubMetaClass``:\n")
    print(">>> type(NormalClass)")
    print(type(NormalClass))
    print()
    print("Creating an instance of ``NormalClass``:\n")
    print(">>> obj = NormalClass()")
    obj = NormalClass(2)
    print()
    print(">>> obj.var")
    print(obj.var)
    print()
    print(">>> obj.method(3)")
    obj.method(3)
    print()
    print(">>> obj.var")
    print(obj.var)
    print('\n.. seealso:: :doc:`Metaclass<feature110>`')
    print(80*'-')
