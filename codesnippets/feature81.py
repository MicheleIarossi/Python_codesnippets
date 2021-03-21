##    Python codesnippets - Static methods via function decorator @staticmethod
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
# Feature 81
#

"""
Static methods via function decorator @staticmethod
===================================================

:py:mod:`codesnippets.feature81`
--------------------------------

By decorating a method with ``@staticmethod``, it can be called either
via the class or via the instance and without the required ``self`` parameter.

The following class counts the instances of Cars:

.. code-block:: Python

    class Car():
        \"""a car class\"""
        n_val = 0
        def __init__(self,name):
            self.name = name
            Car.n_val += 1
            print('<Car: %s created>' % (name))
        @staticmethod
        def num_of_instances():
            \"""returns the total number of instances\"""
            return Car.n_val
        def __repr__(self):
            return 'Car(%r)' % (self.name)

>>> bmw = Car('BMW 3er')
<Car: BMW 3er created>
>>> bmw
Car('BMW 3er')

>>> audi = Car('Audi A6')
<Car: Audi A6 created>
>>> audi
Car('Audi A6')

>>> vwag = Car('VW Golf')
<Car: VW Golf created>
>>> vwag
Car('VW Golf')

>>> Car.num_of_instances()
3

.. seealso:: :doc:`Basic function decorator<feature96>`
"""

def feature81():
    """Static methods via function decorator @staticmethod"""
    print('Static methods via function decorator @staticmethod')
    print('===================================================\n')
    print(':py:mod:`codesnippets.feature81`')
    print('--------------------------------\n')
    print('By decorating a method with ``@staticmethod``, it can be called either')
    print('via the class or via the instance and without the required ``self`` parameter.\n')
    print('The following class counts the instances of Cars:\n')
    class Car():
        """a car class"""
        n_val = 0
        def __init__(self,name):
            self.name = name
            Car.n_val += 1
            print('<Car: %s created>' % (name))
        @staticmethod
        def num_of_instances():
            """returns the total number of instances"""
            return Car.n_val
        def __repr__(self):
            """overloads repr operator"""
            return 'Car(%r)' % (self.name)
    print('.. code-block:: Python\n')
    print("""    class Car():
        \\\"""a car class\\\"""
        n_val = 0
        def __init__(self,name):
            self.name = name
            Car.n_val += 1
            print('<Car: %s created>' % (name))
        @staticmethod
        def num_of_instances():
            \\\"""returns the total number of instances\\\"""
            return Car.n_val
        def __repr__(self):
            return 'Car(%r)' % (self.name)
        """)
    print("\n>>> bmw = Car('BMW 3er')")
    bmw = Car('BMW 3er')
    print('>>> bmw')
    print(bmw)
    print("\n>>> audi = Car('Audi A6')")
    audi = Car('Audi A6')
    print('>>> audi')
    print(audi)
    print("\n>>> vwag = Car('VW Golf')")
    vwag   = Car('VW Golf')
    print('>>> vwag')
    print(vwag)
    print("\n>>> Car.num_of_instances()")
    print(Car.num_of_instances())
    print('\n.. seealso:: :doc:`Basic function decorator<feature96>`')
    print(80*'-')
