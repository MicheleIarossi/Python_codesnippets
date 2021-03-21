##    Python codesnippets - Decorator for a class
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
# Feature 100
#

"""
Decorator for a ``class``
=========================

:py:mod:`codesnippets.feature100`
---------------------------------

The class is given to the decorator which rebinds it to a wrapper class:

.. code-block:: Python

    def decorator(a_class):
        class Wrapper:
            \"""a wrapper class\"""
            def __init__(self, *args):
                print(f"	-> Wrapper.__init__(self,{args})")
                self.wrapped = a_class(*args)
            def __getattr__(self,attr):
                print(f"	-> Wrapper.__getattr__(self,{attr})")
                return getattr(self.wrapped,attr)
        return Wrapper

>>> @decorator
    class MyClass:
        \"""a class\"""
        def __init__(self,a,b):
            print(f"	-> MyClass.__init__(self,{a},{b})")
            self.name = "MyClass"

The following object is actually an instance of ``Wrapper``:

>>> obj = MyClass(43,67)
	-> Wrapper.__init__(self,(43, 67))
	-> MyClass.__init__(self,43,67)

``Wrapper`` has no attribute 'name' which is passed on to the wrapped class:

>>> obj.name
	-> Wrapper.__getattr__(self,name)
MyClass
"""

def feature100():
    """Decorator for a class"""
    print('Decorator for a ``class``')
    print('=========================\n')
    print(':py:mod:`codesnippets.feature100`')
    print('---------------------------------\n')
    print("The class is given to the decorator which rebinds it to a wrapper class:\n")
    def decorator(a_class):
        class Wrapper:
            """a wrapper class"""
            def __init__(self, *args):
                print(f"\t-> Wrapper.__init__(self,{args})")
                self.wrapped = a_class(*args)
            def __getattr__(self,attr):
                print(f"\t-> Wrapper.__getattr__(self,{attr})")
                return getattr(self.wrapped,attr)
        return Wrapper
    print('.. code-block:: Python\n')
    print("""    def decorator(a_class):
        class Wrapper:
            \\\"""a wrapper class\\\"""
            def __init__(self, *args):
                print(f"\t-> Wrapper.__init__(self,{args})")
                self.wrapped = a_class(*args)
            def __getattr__(self,attr):
                print(f"\t-> Wrapper.__getattr__(self,{attr})")
                return getattr(self.wrapped,attr)
        return Wrapper
        """)
    print(""">>> @decorator
    class MyClass:
        \\\"""a class\\\"""
        def __init__(self,a,b):
            print(f"\t-> MyClass.__init__(self,{a},{b})")
            self.name = "MyClass"
        """)
    @decorator
    class MyClass:
        """a class"""
        def __init__(self,a,b):
            print(f"\t-> MyClass.__init__(self,{a},{b})")
            self.name = "MyClass"
    print("The following object is actually an instance of ``Wrapper``:\n")
    print(">>> obj = MyClass(43,67)")
    obj = MyClass(43,67)
    print()
    print("``Wrapper`` has no attribute 'name' which is passed on to the wrapped class:\n")
    print(">>> obj.name")
    print(obj.name)
    print(80*'-')
