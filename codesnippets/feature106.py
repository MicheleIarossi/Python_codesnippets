##    Python codesnippets - Implementation of the singleton pattern via function attributes
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
# Feature 106
#

"""
Implementation of the singleton pattern via function attributes
===============================================================

:py:mod:`codesnippets.feature106`
---------------------------------

In the singleton pattern only one instance of a class is allowed.

The following decorator stores the single instance as a function attribute:

.. code-block:: Python

    def singleton(a_class):
        \"""singleton decorator\"""
        def singleton_wrapper(*args,**kwargs):
            \"""creates an instance and throws exception\"""
            print(f"	-> Decorating class {a_class.__name__}")
            if singleton_wrapper.instance == None:
                print(f"	-> Creating single instance of class {a_class.__name__}")
                singleton_wrapper.instance = a_class(*args,**kwargs)
            else:
                exc_str = f"Class {a_class.__name__} is a singleton class"
                raise RuntimeError(exc_str)
            return singleton_wrapper.instance
        singleton_wrapper.instance = None
        return singleton_wrapper

Example of a decorated class

>>> @singleton
    class Car():
        \"""a car class\"""
        def __init__(self,name):
            print("	-> Creating an instance of Car({repr(name)})")
            self._name = name
        def __repr__(self):
            return f"Car(name={repr(self._name)})"
	-> Decorating class Car

Creation of a single instance is allowed:

>>> try:
        bmw_5_limo = Car("BMW 5 Limousine")
    except RuntimeError as exc:
        print(exc.__class__.__name__ + ': ' + str(exc))
	-> Creating single instance of class Car
	-> Creating an instance of Car('BMW 5 Limousine')

>>> bmw_5_limo
Car(name='BMW 5 Limousine')

Creation of a second instance is NOT allowed:

>>> try:
        audi_a6_limo = Car("AUDI A6 Limousine")
    except RuntimeError as exc:
        print(exc.__class__.__name__ + ': ' + str(exc))
RuntimeError: Class Car is a singleton class
"""

def feature106():
    """Implementation of the singleton pattern via function attributes"""
    print('Implementation of the singleton pattern via function attributes')
    print('===============================================================\n')
    print(':py:mod:`codesnippets.feature106`')
    print('---------------------------------\n')
    print('In the singleton pattern only one instance of a class is allowed.\n')
    print("The following decorator stores the single instance as a function attribute:\n")
    print('.. code-block:: Python\n')
    print("""    def singleton(a_class):
        \\\"""singleton decorator\\\"""
        def singleton_wrapper(*args,**kwargs):
            \\\"""creates an instance and throws exception\\\"""
            print(f"\t-> Decorating class {a_class.__name__}")
            if singleton_wrapper.instance == None:
                print(f"\t-> Creating single instance of class {a_class.__name__}")
                singleton_wrapper.instance = a_class(*args,**kwargs)
            else:
                exc_str = f"Class {a_class.__name__} is a singleton class"
                raise RuntimeError(exc_str)
            return singleton_wrapper.instance
        singleton_wrapper.instance = None
        return singleton_wrapper
        """)
    def singleton(a_class):
        """singleton decorator"""
        print(f"\t-> Decorating class {a_class.__name__}")
        def singleton_wrapper(*args,**kwargs):
            """creates an instance and throws exception"""
            if singleton_wrapper.instance is None:
                print(f"\t-> Creating single instance of class {a_class.__name__}")
                singleton_wrapper.instance = a_class(*args,**kwargs)
            else:
                exc_str = f"Class {a_class.__name__} is a singleton class"
                raise RuntimeError(exc_str)
            return singleton_wrapper.instance
        singleton_wrapper.instance = None
        return singleton_wrapper
    print("Example of a decorated class\n")
    print(""">>> @singleton
    class Car():
        \\\"""a car class\\\"""
        def __init__(self,name):
            print("\t-> Creating an instance of Car({repr(name)})")
            self._name = name
        def __repr__(self):
            return f"Car(name={repr(self._name)})" """)
    @singleton
    class Car():
        """a car class"""
        def __init__(self,name):
            print(f"\t-> Creating an instance of Car({repr(name)})")
            self._name = name
        def __repr__(self):
            return f"Car(name={repr(self._name)})"
    print("\nCreation of a single instance is allowed:")
    print()
    print(""">>> try:
        bmw_5_limo = Car("BMW 5 Limousine")
    except RuntimeError as exc:
        print(exc.__class__.__name__ + ': ' + str(exc))""")
    try:
        bmw_5_limo = Car("BMW 5 Limousine")
    except RuntimeError as exc:
        print(exc.__class__.__name__ + ': ' + str(exc))
    print("\n>>> bmw_5_limo")
    print(bmw_5_limo)
    print()
    print("Creation of a second instance is NOT allowed:")
    print()
    print(""">>> try:
        audi_a6_limo = Car("AUDI A6 Limousine")
    except RuntimeError as exc:
        print(exc.__class__.__name__ + ': ' + str(exc))""")
    try:
        audi_a6_limo = Car("AUDI A6 Limousine")
    except RuntimeError as exc:
        print(exc.__class__.__name__ + ': ' + str(exc))
    print(80*'-')