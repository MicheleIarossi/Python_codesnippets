##    Python codesnippets - The property protocol
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
# Feature 92
#

"""
The property protocol
=====================

:py:mod:`codesnippets.feature92`
--------------------------------

The property protocol lets you run your own access functions when access operations
are invoced on a given attribute (read, write, deletion):

.. code-block:: Python

    class Car:
        \"""a car class\"""
        def __init__(self,model):
            print("	-> Car.__init__: creating an instance of the Car class...")
            self._model = model
        def get_model(self):
            \"""returns the car model\"""
            print("	-> Car.get_model: getter function called...")
            return self._model
        def set_model(self,name):
            \"""sets the car brand name\"""
            print("	-> Car.set_model: setter function called...")
            self._model = name
        def del_model(self):
            \"""deletes the car model attribute\"""
            print("	-> Car.del_model: delete function called...")
            del self._model
        model = property(get_model,set_model,del_model,"the car model name")

>>> a_bmw = Car('BMW 3')
	-> Car.__init__: creating an instance of the Car class...

>>> a_bmw.model = 'BMW 5'
	-> Car.set_model: setter function called...

>>> print(a_bmw.model)
	-> Car.get_model: getter function called...
BMW 5
>>> help(Car.model)
Help on property:
    the car model name

>>> del a_bmw.model
	-> Car.del_model: delete function called...
"""

def feature92():
    """The property protocol"""
    print('The property protocol')
    print('=====================\n')
    print(':py:mod:`codesnippets.feature92`')
    print('--------------------------------\n')
    print('The property protocol lets you run your own access functions when access operations')
    print('are invoced on a given attribute (read, write, deletion):\n')
    print('.. code-block:: Python\n')
    print("""    class Car:
        \\\"""a car class\\\"""
        def __init__(self,model):
            print("\t-> Car.__init__: creating an instance of the Car class...")
            self._model = model
        def get_model(self):
            \\\"""returns the car model\\\"""
            print("\t-> Car.get_model: getter function called...")
            return self._model
        def set_model(self,name):
            \\\"""sets the car brand name\\\"""
            print("\t-> Car.set_model: setter function called...")
            self._model = name
        def del_model(self):
            \\\"""deletes the car model attribute\\\"""
            print("\t-> Car.del_model: delete function called...")
            del self._model
        model = property(get_model,set_model,del_model,"the car model name")
        """)
    class Car:
        """a car class"""
        def __init__(self,model):
            print("\t-> Car.__init__: creating an instance of the Car class...")
            self._model = model
        def get_model(self):
            """returns the car model"""
            print("\t-> Car.get_model: getter function called...")
            return self._model
        def set_model(self,name):
            """sets the car brand name"""
            print("\t-> Car.set_model: setter function called...")
            self._model = name
        def del_model(self):
            """deletes the car model attribute"""
            print("\t-> Car.del_model: delete function called...")
            del self._model
        model = property(get_model,set_model,del_model,"the car model name")
    print(">>> a_bmw = Car('BMW 3')")
    a_bmw = Car('BMW')
    print("\n>>> a_bmw.model = 'BMW 5'")
    a_bmw.model = 'BMW 5'
    print("\n>>> print(a_bmw.model)")
    print(a_bmw.model)
    print(">>> help(Car.model)")
    help(Car.model)
    print(">>> del a_bmw.model")
    del a_bmw.model
    print(80*'-')
