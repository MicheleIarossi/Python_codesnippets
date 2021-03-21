##    Python codesnippets - Implementation of the singleton pattern via class decorator
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
Implementation of the singleton pattern via class decorator
===========================================================

:py:mod:`codesnippets.feature106`
---------------------------------

In the singleton pattern only one instance of a class is allowed.

The following decorator stores the single instance as a class attribute:

.. code-block:: Python

    class Singleton:
        \"""singleton decorator\"""
        def __init__(self,a_class):
            print(f"	-> Decorating class {a_class.__name__}")
            self._instance = None
            self._a_class  = a_class
        def __call__(self,*args,**kwargs):
            print(f"	-> Creating an instance of class {self.a_class.__name__}")
            if self._instance is None:
                self._instance = self._a_class(*args,**kwargs)
            else:
                exc_str = f"{RuntimeError.__name__}: Class {self._a_class.__name__} is"
                          f" a singleton class"
                raise RuntimeError(exc_str)
            return self._instance

Example of a decorated class:

>>> @Singleton
    class Car():
        \"""a car class\"""
        def __init__(self,name):
            print("	-> Creating an instance of Car({repr(name)})")
            self._name = name
        def __repr__(self):
            return f"Car(name={repr(self._name)})"
	-> Decorating class 'Car'
Creation of a single instance is allowed:

>>> try:
        bmw_5_limo = Car("BMW 5 Limousine")
    except RuntimeError as exc:
        print(exc)
	-> Creating an instance of class 'Car'
	-> Creating an instance of Car('BMW 5 Limousine')

>>> bmw_5_limo
Car(name='BMW 5 Limousine')

Creation of a second instance is NOT allowed:

>>> try:
        audi_a6_limo = Car("AUDI A6 Limousine")
    except RuntimeError as exc:
        print(exc)
	-> Creating an instance of class 'Car'
RuntimeError: Class 'Car' is a singleton class
"""

def feature106():
    """Implementation of the singleton pattern via class decorator"""
    print('Implementation of the singleton pattern via class decorator')
    print('===========================================================\n')
    print(':py:mod:`codesnippets.feature106`')
    print('---------------------------------\n')
    print('In the singleton pattern only one instance of a class is allowed.\n')
    print("The following decorator stores the single instance as a class attribute:\n")
    print('.. code-block:: Python\n')
    print("""    class Singleton:
        \\\"""singleton decorator\\\"""
        def __init__(self,a_class):
            print(f"\t-> Decorating class {a_class.__name__}")
            self._instance = None
            self._a_class  = a_class
        def __call__(self,*args,**kwargs):
            print(f"\t-> Creating an instance of class {self._a_class.__name__}")
            if self._instance is None:
                self._instance = self._a_class(*args,**kwargs)
            else:
                exc_str = f"{RuntimeError.__name__}: Class {self._a_class.__name__}"
                          f" is a singleton class"
                raise RuntimeError(exc_str)
            return self._instance
        """)
    class Singleton:
        """singleton decorator"""
        def __init__(self,a_class):
            print(f"\t-> Decorating class {repr(a_class.__name__)}")
            self._instance = None
            self._a_class  = a_class
        def __call__(self,*args,**kwargs):
            print(f"\t-> Creating an instance of class {repr(self._a_class.__name__)}")
            if self._instance is None:
                self._instance = self._a_class(*args,**kwargs)
            else:
                exc_str = f"{RuntimeError.__name__}: Class {repr(self._a_class.__name__)} is a singleton class"
                raise RuntimeError(exc_str)
            return self._instance
    print("Example of a decorated class:\n")
    print(""">>> @Singleton
    class Car():
        \\\"""a car class'\\\"""
        def __init__(self,name):
            print("\t-> Creating an instance of Car({repr(name)})")
            self._name = name
        def __repr__(self):
            return f"Car(name={repr(self._name)})" """)
    @Singleton
    class Car():
        """a car class"""
        def __init__(self,name):
            print(f"\t-> Creating an instance of Car({repr(name)})")
            self._name = name
        def __repr__(self):
            """overloads repr operator"""
            return f"Car(name={repr(self._name)})"
    print("Creation of a single instance is allowed:\n")
    print(""">>> try:
        bmw_5_limo = Car("BMW 5 Limousine")
    except RuntimeError as exc:
        print(exc)""")
    try:
        bmw_5_limo = Car("BMW 5 Limousine")
    except RuntimeError as exc:
        print(exc)
    print("\n>>> bmw_5_limo")
    print(bmw_5_limo)
    print()
    print("Creation of a second instance is NOT allowed:\n")
    print(""">>> try:
        audi_a6_limo = Car("AUDI A6 Limousine")
    except RuntimeError as exc:
        print(exc)""")
    try:
        audi_a6_limo = Car("AUDI A6 Limousine")
    except RuntimeError as exc:
        print(exc)
    print(80*'-')
