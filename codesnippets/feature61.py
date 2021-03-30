##    Python codesnippets - Adding features via inheritance
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
# Feature 61
#

"""
Adding features via inheritance
===============================

:py:mod:`codesnippets.feature61`
--------------------------------

New features can be added to an existing class via inheritance.

The following ``class`` provides a representation method that prints out the
instance class name and attributes:

.. code-block:: Python

    class Attributes:
        \"""Class for printing attributes of inherited classes.\"""
        def __repr__(self):
            \"""Overloaded repr operator.\"""
            class_name = self.__class__.__name__
            class_keys = self.__dict__.keys()
            attr_list  = ['%s=%r' % (k,self.__dict__[k]) for k in class_keys]
            attr_str   = ','.join(attr_list)
            return '%s(%s)' % (class_name,attr_str)

The classes ``Animal`` and ``Mammal`` from :doc:`First classes<feature59>` are now adapted for
taking advantage of the usage of the ``Attributes`` class:

.. code-block:: Python

    class Animal(Attributes):
        \"""Base class for describing an animal.\"""
        def __init__(self,name='',species='',rank=0):
            \"""Animal constructor.\"""
            self.name    = name
            self.species = species
            self.rank    = rank
        def elevate_rank(self,delta):
            \"""Method for changing the rank.\"""
            self.rank += delta
        def __repr__(self):
            \"""Overloaded repr operator.\"""
            return Attributes.__repr__(self)

In the class definition above:

* ``Animal`` is derived now from ``Attributes``,
* the special method ``__repr__`` uses the ``Attributes.__repr__`` method, instead of
  its own implementation.

The following is the subclass modeling mammals derived from ``Animal`` above:

.. code-block:: Python

    class Mammal(Animal):
        \"""Specialized class for describing a mammal.\"""
        def __init__(self,name='',rank=0,weight=100,height=100):
            \"""Mammal constructor.\"""
            Animal.__init__(self,name,'mammal',rank) # Base class constructor is called
            self.weight = weight
            self.height = height
        def elevate_rank(self,delta):
            \"""Customized method for changing the rank for mammals.\"""
            Animal.elevate_rank(self,2*delta)        # Reuses the method from the base class
        def __repr__(self):
            \"""Overloaded repr operator.\"""
            return Animal.__repr__(self)

The class ``Mammal`` now still reuses methods of its base class ``Animal`` as before, but
``__repr__`` uses the ``Attributes.__repr__`` method as well, via ``Animal.__repr__``.

Given the classes above, the creation of instances of ``Animal`` and ``Mammal`` is done as:

>>> snake = Animal('snake','reptile',23)
>>> snake
Animal(name='snake',species='reptile',rank=23)

>>> snake.elevate_rank(3)
>>> snake
Animal(name='snake',species='reptile',rank=26)

>>> tiger = Mammal('tiger',143,132,110)
>>> tiger
Mammal(name='Tiger',species='mammal',rank=143,weight=132,height=110)

>>> tiger.elevate_rank(3)
>>> tiger
Mammal(name='Tiger',species='mammal',rank=149,weight=132,height=110)

.. seealso:: :doc:`First classes<feature59>`"""

def feature61():
    """Adding features via inheritance"""
    print('Adding features via inheritance')
    print('===============================\n')
    print(':py:mod:`codesnippets.feature61`')
    print('--------------------------------\n')
    print('New features can be added to an existing class via inheritance.\n')
    print('The following ``class`` provides a representation method that prints out'
          '\nthe instance class name and attributes:\n')
    class Attributes:
        """Class for printing attributes of inherited classes"""
        def __repr__(self):
            """Overloaded repr operator"""
            class_name = self.__class__.__name__
            class_keys = self.__dict__.keys()
            attr_list  = ['%s=%r' % (k,self.__dict__[k]) for k in class_keys]
            attr_str   = ','.join(attr_list)
            return '%s(%s)' % (class_name,attr_str)
    print('.. code-block:: Python\n')
    print("""    class Attributes:
        \\\"""Class for printing attributes of inherited classes.\\\"""
        def __repr__(self):
            \\\"""Overloaded repr operator.\\\"""
            class_name = self.__class__.__name__
            class_keys = self.__dict__.keys()
            attr_list  = ['%s=%r' % (k,self.__dict__[k]) for k in class_keys]
            attr_str   = ','.join(attr_list)
            return '%s(%s)' % (class_name,attr_str)
        """)
    print('The classes ``Animal`` and ``Mammal`` from :doc:`First classes<feature59>`'
          ' are now adapted for\ntaking advantage of the usage of the ``Attributes`` class:\n')
    class Animal(Attributes):
        """Base class for describing an animal"""
        def __init__(self,name='',species='',rank=0):
            """Animal constructor"""
            self.name    = name
            self.species = species
            self.rank    = rank
        def elevate_rank(self,delta):
            """Method for changing the rank"""
            self.rank += delta
        def __repr__(self):
            """overloads repr operator"""
            return Attributes.__repr__(self)
    print('.. code-block:: Python\n')
    print("""    class Animal(Attributes):
        \\\"""Base class for describing an animal.\\\"""
        def __init__(self,name='',species='',rank=0):
            \\\"""Animal constructor.\\\"""
            self.name    = name
            self.species = species
            self.rank    = rank
        def elevate_rank(self,delta):
            \\\"""Method for changing the rank.\\\"""
            self.rank += delta
        def __repr__(self):
            \\\"""Overloaded repr operator.\\\"""
            return Attributes.__repr__(self)
            """)
    print('In the class definition above:\n')
    print('* ``Animal`` is derived now from ``Attributes``,')
    print('* the special method ``__repr__`` uses the ``Attributes.__repr__`` method, '
          'instead of\n  its own implementation.')
    print('\nThe following is the subclass modeling mammals derived from ``Animal`` above:\n')
    class Mammal(Animal):
        """Specialized class for describing a mammal"""
        def __init__(self,name='',rank=0,weight=100,height=100):
            """Mammal constructor"""
            Animal.__init__(self,name,'mammal',rank) # Base class constructor is called
            self.weight = weight
            self.height = height
        def elevate_rank(self,delta):
            """Customized method for changing the rank for mammals"""
            Animal.elevate_rank(self,2*delta)         # Reuses the method from the base class
        def __repr__(self):
            """overloads repr operator"""
            return Animal.__repr__(self)
    print('.. code-block:: Python\n')
    print("""    class Mammal(Animal):
        \\\"""Specialized class for describing a mammal.\\\"""
        def __init__(self,name='',rank=0,weight=100,height=100):
            \\\"""Mammal constructor.\\\"""
            Animal.__init__(self,name,'mammal',rank) # Base class constructor is called
            self.weight = weight
            self.height = height
        def elevate_rank(self,delta):
            \\\"""Customized method for changing the rank for mammals.\\\"""
            Animal.elevate_rank(self,2*delta)        # Reuses the method from the base class
        def __repr__(self):
            \\\"""Overloaded repr operator.\\\"""
            return Animal.__repr__(self)
            """)
    print('The class ``Mammal`` now still reuses methods of its base class ``Animal`` as before, '
          'but\n``__repr__`` uses the ``Attributes.__repr__`` method as well, via'
          '``Animal.__repr__``.\n')
    print('Given the classes above, the creation of instances of ``Animal`` and'
          ' ``Mammal`` is done as:\n')
    print(">>> snake = Animal('snake','reptile',23)")
    snake = Animal('snake','reptile',23)
    print(">>> snake")
    print(snake)
    print("\n>>> snake.elevate_rank(3)")
    snake.elevate_rank(3)
    print(">>> snake")
    print(snake)
    print("\n>>> tiger = Mammal('tiger',143,132,110)")
    tiger = Mammal('Tiger',143,132,110)
    print(">>> tiger")
    print(tiger)
    print("\n>>> tiger.elevate_rank(3)")
    tiger.elevate_rank(3)
    print(">>> tiger")
    print(tiger)
    print('\n.. seealso:: :doc:`First classes<feature59>`')
    print(80*'-')