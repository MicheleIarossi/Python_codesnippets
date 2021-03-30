##    Python codesnippets - First classes
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
# Feature 59
#

"""
First classes
=============

:py:mod:`codesnippets.feature59`
--------------------------------

This is a basic class modeling an animal:

.. code-block:: Python

    class Animal:
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
            return 'Animal(name=%r,species=%r, rank=%r)' % (self.name,self.species,self.rank)

In the class definition above:

* the special method ``__init__`` is the *constructor*. It attaches the attributes ``name``,
  ``species`` and ``rank`` to a newly created instance,
* the method ``elevate_rank`` changes the ``rank`` value,
* the special method ``__repr__`` returns a string representation of the instance, called for
  example when printing an instance from the interactive prompt.

The following is a subclass modeling mammals derived from ``Animal`` above:

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
            # Customizes representation of the base class
            return 'Mammal(name=%r,rank=%r,weight=%r,height=%r)' % (self.name,self.rank,
                                                                    self.weight,self.height)

The class ``Mammal`` reuses methods of its base class

* in the constructor and
* in the overridden method ``elevate_rank``.

Given the classes above, the creation of instances of ``Animal`` and ``Mammal`` is done as:

>>> snake = Animal('snake','reptile',23)
>>> snake
Animal(name='snake',species='reptile', rank=23)

>>> snake.elevate_rank(3)
>>> snake
Animal(name='snake',species='reptile', rank=26)

>>> tiger = Mammal('tiger',143,132,110)
>>> tiger
Mammal(name='Tiger',rank=143,weight=132,height=110)

>>> tiger.elevate_rank(3)
>>> tiger
Mammal(name='Tiger',rank=149,weight=132,height=110)
"""

def feature59():
    """First classes"""
    print('First classes')
    print('=============\n')
    print(':py:mod:`codesnippets.feature59`')
    print('--------------------------------\n')
    print('This is a basic class modeling an animal:\n')
    class Animal:
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
            """Overloaded repr operator"""
            return 'Animal(name=%r,species=%r, rank=%r)' % (self.name,self.species,self.rank)
    print('.. code-block:: Python\n')
    print("""    class Animal:
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
            return 'Animal(name=%r,species=%r, rank=%r)' % (self.name,self.species,self.rank)
            """)
    print('In the class definition above:\n')
    print('* the special method ``__init__`` is the *constructor*. It attaches the'
          ' attributes ``name``, \n  ``species`` and ``rank`` to a newly created instance,')
    print('* the method ``elevate_rank`` changes the ``rank`` value,')
    print('* the special method ``__repr__`` returns a string representation of the instance,'
          ' called for\n  example when printing an instance from the interactive prompt.')
    print('\nThe following is a subclass modeling mammals derived from ``Animal`` above:\n')
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
            """Overloaded repr operator"""
            # Customizes representation of the base class
            return 'Mammal(name=%r,rank=%r,weight=%r,height=%r)' % (self.name,self.rank,
                                                                    self.weight,self.height)
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
            # Customizes representation of the base class
            return 'Mammal(name=%r,rank=%r,weight=%r,height=%r)' % (self.name,self.rank,
                                                                    self.weight,self.height)
            """)
    print('The class ``Mammal`` reuses methods of its base class\n')
    print('* in the constructor and')
    print('* in the overridden method ``elevate_rank``.\n')
    print('Given the classes above, the creation of instances of ``Animal`` and ``Mammal``'
          ' is done as:\n')
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
    print(80*'-')