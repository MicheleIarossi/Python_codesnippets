##    Python codesnippets - Class statement protocol
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
# Feature 108
#

"""
Class statement protocol
========================

:py:mod:`codesnippets.feature108`
---------------------------------

Class objects are created by calling the ``type`` object:

>>> MyClass = type(classname,superclasses,attributedict)

at the end of a class definition.

The ``type`` object overloads the ``__call__`` operator and calls
``type.__new__`` for creating the class object, and ``type.__init__``
for initializing it.

Given the method function definition below:

.. code-block:: Python

    def a_method(self):
	print(f"	-> Inside {self.__class__.__name__} -> a_method()...")
	print(f"	-> Attribute self.name = {repr(self.name)}")

a ``class`` can be created dynamically like this:

>>> MyClass = type('MyClass',(object,),{'name':'My class','a_method':a_method},
                   '__module__':'codesnippets.feature108.feature108.<locals>')

>>> an_obj = MyClass()

>>> an_obj.a_method()
	-> Inside MyClass -> a_method()...
	-> Attribute self.name = 'My class'

>>> MyClass.__module__
codesnippets.feature108.feature108.<locals>

>>> dir(MyClass)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
'__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
'__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
'__weakref__', 'a_method', 'name']

.. seealso:: :doc:`Type<feature107>`
"""

def feature108():
    """Class statement protocol"""
    print('Class statement protocol')
    print('========================\n')
    print(':py:mod:`codesnippets.feature108`')
    print('---------------------------------\n')
    print("Class objects are created by calling the ``type`` object:\n")
    print(">>> MyClass = type(classname,superclasses,attributedict)\n")
    print("at the end of a class definition.\n")
    print("The ``type`` object overloads the ``__call__`` operator and calls")
    print("``type.__new__`` for creating the class object, and ``type.__init__``")
    print("for initializing it.\n")
    print("Given the method function definition below:\n")
    print('.. code-block:: Python\n')
    print("""    def a_method(self):
	print(f"\t-> Inside {self.__class__.__name__} -> a_method()...")
	print(f"\t-> Attribute self.name = {repr(self.name)}")
	""")
    def a_method(self):
        print(f"\t-> Inside {self.__class__.__name__} -> a_method()...")
        print(f"\t-> Attribute self.name = {repr(self.name)}")
    print("a ``class`` can be created dynamically like this:\n")
    print(">>> MyClass = type('MyClass',(object,),{'name':'My class',"
          "\n'a_method':a_method},'__module__':'codesnippets.feature108.feature108.<locals>')")
    MyClass = type('MyClass',(object,),
                   {'name':'My class','a_method':a_method,
                    '__module__':'codesnippets.feature108.feature108.<locals>'})
    print()
    print(">>> an_obj = MyClass()\n")
    an_obj = MyClass()
    print(">>> an_obj.a_method()")
    an_obj.a_method()
    print()
    print(">>> MyClass.__module__")
    print(MyClass.__module__)
    print()
    print(">>> dir(MyClass)")
    print(dir(MyClass))
    print('\n.. seealso:: :doc:`Type<feature107>`')
    print(80*'-')
