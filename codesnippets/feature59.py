##    Python codesnippets - Built-in class attributes for introspection
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
Built-in ``class`` attributes for introspection
===============================================

:py:mod:`codesnippets.feature59`
--------------------------------

Instances of classes have built-in attributes that are available for introspection.

Given the ``Mammal`` class in :doc:`First classes<feature58>`, a ``tiger`` is instanced as:

>>> tiger = Mammal('tiger',143,132,110)
>>> tiger
Mammal(name='Tiger',rank=143,weight=132,height=110)

>>> tiger.elevate_rank(3)
>>> tiger
Mammal(name='Tiger',rank=149,weight=132,height=110)

The following are some of the built-in attributes available for introspection:

* the ``__class__`` attribute points to the class object

>>> tiger.__class__
<class 'codesnippets.feature59.feature59.<locals>.Mammal'>

* the ``__class__.__name__`` attribute is a string of the name of the class

>>> tiger.__class__.__name__
Mammal

* the ``__dict__`` attribute is a dictionary of the instance attributes

>>> list(tiger.__dict__.keys())
['name', 'species', 'rank', 'weight', 'height']

.. seealso:: :doc:`First classes<feature58>`, :doc:`More on class introspection tools: __class__,
    __bases__, __dict__<feature62>`
"""

def feature59():
    """Built-in attributes of class for introspection"""
    print('Built-in ``class`` attributes for introspection')
    print('===============================================\n')
    print(':py:mod:`codesnippets.feature59`')
    print('--------------------------------\n')
    print('Instances of classes have built-in attributes that are available for introspection.\n')
    print('Given the ``Mammal`` class in :doc:`First classes<feature58>`, a ``tiger`` '
          'is instanced as:\n')
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
    print(">>> tiger = Mammal('tiger',143,132,110)")
    tiger = Mammal('Tiger',143,132,110)
    print(">>> tiger")
    print(tiger)
    print("\n>>> tiger.elevate_rank(3)")
    tiger.elevate_rank(3)
    print(">>> tiger")
    print(tiger)
    print('\nThe following are some of the built-in attributes available for introspection:\n')
    print('* the ``__class__`` attribute points to the class object\n')
    print(">>> tiger.__class__")
    print(tiger.__class__)
    print('\n* the ``__class__.__name__`` attribute is a string of the name of the class\n')
    print(">>> tiger.__class__.__name__")
    print(tiger.__class__.__name__)
    print('\n* the ``__dict__`` attribute is a dictionary of the instance attributes\n')
    print(">>> list(tiger.__dict__.keys())")
    print(list(tiger.__dict__.keys()))
    print('\n.. seealso:: :doc:`First classes<feature58>`, '
          ':doc:`More on class introspection tools: __class__,\n    '
          '__bases__, __dict__<feature62>`')
    print(80*'-')
