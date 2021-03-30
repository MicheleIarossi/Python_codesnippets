##    Python codesnippets - More on class introspection tools: __class__, __bases__, __dict__
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
# Feature 63
#

"""
More on class introspection tools: ``__class__`` , ``__bases__`` , ``__dict__``
===============================================================================

:py:mod:`codesnippets.feature63`
--------------------------------

These special attributes are useful as introspection tools:

* ``__class__`` is a reference to the class object,
* ``__bases__`` is a list of references to the base class objects,
* ``__dict__`` is a dictionary of the object attributes.

Their usage is shown by means of the following classes:

.. code-block:: Python

    class Aircraft:
	\"""a base class\"""
        counter = 0
        def __init__(self,name):
            self._name = name
            Aircraft.counter += 1
        def __repr__(self):
            \"""overloads repr operator\"""
            return 'Aircraft(name=%r)' % (self._name)

.. code-block:: Python

    class Airplane(Aircraft):
	\"""a derived class\"""
        max_speed = 900
        def __init__(self,name,passengers):
            Aircraft.__init__(self,name)
            self._passengers = passengers
        def __repr__(self):
            \"""overloads repr operator\"""
            return 'Airplane(name=%r,passengers=%r)' % (self._name,self._passengers)

These are now examples of instances:

>>> helicopter = Aircraft('Helicopter')
>>> helicopter
Aircraft(name='Helicopter')

>>> airbus320 = Airplane('Airbus_320',300)
>>> airbus320
Airplane(name='Airbus_320',passengers=300)

The attribute ``__class__`` provides a reference to the class object:

>>> helicopter.__class__
<class 'codesnippets.feature63.feature63.<locals>.Aircraft'>
>>> helicopter.__class__.__name__ # String of the name of the class
Aircraft

>>> airbus320.__class__
<class 'codesnippets.feature63.feature63.<locals>.Airplane'>
>>> airbus320.__class__.__name__ # String of the name of the class
Airplane

The attribute ``__dict__`` provides a dictionary of attributes.
Notice the difference when applied to an instance and to a class:

>>> list(helicopter.__dict__.keys())
['_name']
>>> list(airbus320.__dict__.keys())
['_name', '_passengers']

>>> list(Aircraft.__dict__.keys())
['__module__', '__doc__', 'counter', '__init__', '__repr__', '__dict__', '__weakref__']
>>> list(Airplane.__dict__.keys())
['__module__', '__doc__', 'max_speed', '__init__', '__repr__']

The attribute ``__bases__`` provides a list of the superclasses.
It can be used only on class objects, not instances:

>>> Aircraft.__bases__
(<class 'object'>,)
>>> Airplane.__bases__
(<class 'codesnippets.feature63.feature63.<locals>.Aircraft'>,)

.. seealso:: :doc:`Built-in class attributes for introspection<feature60>`
"""

def feature63():
    """More on class introspection tools: __class__, __bases__, __dict__"""
    print('More on class introspection tools: ``__class__`` , ``__bases__`` , ``__dict__``')
    print('===============================================================================\n')
    print(':py:mod:`codesnippets.feature63`')
    print('--------------------------------\n')
    print("These special attributes are useful as introspection tools:\n")
    print('* ``__class__`` is a reference to the class object,')
    print('* ``__bases__`` is a list of references to the base class objects,')
    print('* ``__dict__`` is a dictionary of the object attributes.')
    print('\nTheir usage is shown by means of the following classes:\n')
    class Aircraft:
        """a base class"""
        counter = 0
        def __init__(self,name):
            self._name = name
            Aircraft.counter += 1
        def __repr__(self):
            """overloads repr operator"""
            return 'Aircraft(name=%r)' % (self._name)
    print('.. code-block:: Python\n')
    print("""    class Aircraft:
	\\\"""a base class\\\"""
        counter = 0
        def __init__(self,name):
            self._name = name
            Aircraft.counter += 1
        def __repr__(self):
            \\\"""overloads repr operator\\\"""
            return 'Aircraft(name=%r)' % (self._name)
	""")
    class Airplane(Aircraft):
        """a derived class"""
        max_speed = 900
        def __init__(self,name,passengers):
            Aircraft.__init__(self,name)
            self._passengers = passengers
        def __repr__(self):
            """overloads repr operator"""
            return 'Airplane(name=%r,passengers=%r)' % (self._name,self._passengers)
    print('.. code-block:: Python\n')
    print("""   class Airplane(Aircraft):
	\\\"""a derived class\\\"""
        max_speed = 900
        def __init__(self,name,passengers):
            Aircraft.__init__(self,name)
            self._passengers = passengers
        def __repr__(self):
            \\\"""overloads repr operator\\\"""
            return 'Airplane(name=%r,passengers=%r)' % (self._name,self._passengers)
	""")
    print("These are now examples of instances:\n")
    print(">>> helicopter = Aircraft('Helicopter')")
    helicopter = Aircraft('Helicopter')
    print(">>> helicopter")
    print(helicopter)
    print("\n>>> airbus320 = Airplane('Airbus_320',300)")
    airbus320 = Airplane('Airbus_320',300)
    print(">>> airbus320")
    print(airbus320)
    print("\nThe attribute ``__class__`` provides a reference to the class object:\n")
    print(">>> helicopter.__class__")
    print(helicopter.__class__)
    print(">>> helicopter.__class__.__name__ # String of the name of the class")
    print(helicopter.__class__.__name__)
    print("\n>>> airbus320.__class__")
    print(airbus320.__class__)
    print(">>> airbus320.__class__.__name__ # String of the name of the class")
    print(airbus320.__class__.__name__)
    print("\nThe attribute ``__dict__`` provides a dictionary of attributes.")
    print("Notice the difference when applied to an instance and to a class:\n")
    print(">>> list(helicopter.__dict__.keys())")
    print(list(helicopter.__dict__.keys()))
    print(">>> list(airbus320.__dict__.keys())")
    print(list(airbus320.__dict__.keys()))
    print("\n>>> list(Aircraft.__dict__.keys())")
    print(list(Aircraft.__dict__.keys()))
    print(">>> list(Airplane.__dict__.keys())")
    print(list(Airplane.__dict__.keys()))
    print("\nThe attribute ``__bases__`` provides a list of the superclasses. ")
    print("It can be used only on class objects, not instances:\n")
    print(">>> Aircraft.__bases__")
    print(Aircraft.__bases__)
    print(">>> Airplane.__bases__")
    print(Airplane.__bases__)
    print('\n.. seealso:: :doc:`Built-in class attributes for introspection<feature60>`')
    print(80*'-')