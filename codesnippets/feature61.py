##    Python codesnippets - Class and per-instance attributes
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
Class and per-instance attributes
=================================

:py:mod:`codesnippets.feature61`
--------------------------------

In Python a class is a statement that is run and not only a declaration:

.. code-block:: Python

    class Car:
        \"""A simple Car class\"""
        n_val = 0 # global class counter
        def __init__(self,brand='BMW',color='navy'):
            \"""Simple constructor for Car instances\"""
            self.brand = brand # Per instance attributes
            self.color = color
            Car.n_val += 1
        def __repr__(self):
            \"""overloads repr operator\"""
            return 'Car(brand=%r,color=%r)' % (self.brand,self.color)

When the class definition is run, it creates a global class counter ``n_val``:

>>> Car.n_val
0

The attribute ``n_value`` really belongs to the class,
but it can be accessed by the instances as well:

>>> golf = Car('VW', 'black')
>>> (golf.n_val, Car.n_val)
(1, 1)

The attribute ``n_value`` is shared among the instances:

>>> bmw = Car('BMW','red')
>>> (bmw.n_val, Car.n_val) # Attribute n is shared among the instances
(2, 2)
>>> (golf.n_val,Car.n_val) # Attribute n is shared among the instances
(2, 2)

Per-instance attributes, e.g. ``brand`` or ``color``, are created
when ``__init__`` is called, i.e. at instance creation:

>>> jaguar = Car('Jaguar','silver')
>>> jaguar.brand, jaguar.color
('Jaguar', 'silver')

These per-intstance attributes are printed when the ``__repr__`` method is called:

>>> jaguar
Car(brand='Jaguar',color='silver')
"""

def feature61():
    """Class and per-instance attributes"""
    print('Class and per-instance attributes')
    print('=================================\n')
    print(':py:mod:`codesnippets.feature61`')
    print('--------------------------------\n')
    print('In Python a class is a statement that is run and not only a declaration:\n')
    class Car:
        """ A simple Car class"""
        n_val = 0 # global class counter
        def __init__(self,brand='BMW',color='navy'):
            """Simple constructor for Car instances"""
            self.brand = brand # Per instance attributes
            self.color = color
            Car.n_val += 1
        def __repr__(self):
            """overloads repr operator"""
            return 'Car(brand=%r,color=%r)' % (self.brand,self.color)
    print('.. code-block:: Python\n')
    print("""    class Car:
        \\\"""A simple Car class\\\"""
        n_val = 0 # global class counter
        def __init__(self,brand='BMW',color='navy'):
            \\\"""Simple constructor for Car instances\\\"""
            self.brand = brand # Per instance attributes
            self.color = color
            Car.n_val += 1
        def __repr__(self):
            \\\"""overloads repr operator\\\"""
            return 'Car(brand=%r,color=%r)' % (self.brand,self.color)
        """)
    print('When the class definition is run, it creates a global class counter ``n_val``:\n')
    print(">>> Car.n_val")
    print(Car.n_val)
    print('\nThe attribute ``n_value`` really belongs to the class,\nbut it can be accessed '
          'by the instances as well:\n')
    print(">>> golf = Car('VW', 'black')")
    golf = Car('VW', 'black')
    print(">>> (golf.n_val, Car.n_val)")
    print("(%s, %s)" % (golf.n_val, Car.n_val))
    print('\nThe attribute ``n_value`` is shared among the instances:\n')
    print(">>> bmw = Car('BMW','red')")
    bmw = Car('BMW','red')
    print(">>> (bmw.n_val, Car.n_val) # Attribute n is shared among the instances")
    print("(%s, %s)" % (bmw.n_val, Car.n_val))
    print(">>> (golf.n_val,Car.n_val) # Attribute n is shared among the instances")
    print("(%s, %s)" % (golf.n_val, Car.n_val))
    print('\nPer-instance attributes, e.g. ``brand`` or ``color``, are created '
          '\n when ``__init__`` is called, i.e. at instance creation:\n')
    print(">>> jaguar = Car('Jaguar','silver')")
    jaguar = Car('Jaguar','silver')
    print('>>> jaguar.brand, jaguar.color')
    print((jaguar.brand, jaguar.color))
    print('\nThese per-intstance attributes are printed when the ``__repr__`` method is called:\n')
    print('>>> jaguar')
    print(jaguar)
    print(80*'-')
