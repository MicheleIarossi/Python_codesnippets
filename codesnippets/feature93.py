##    Python codesnippets - Descriptors
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
# Feature 93
#

"""
Descriptors
===========

:py:mod:`codesnippets.feature93`
--------------------------------

Descriptors are another way to control attribute access, and they need
to be created as separate classes.

The following ``price`` descriptor defines how the price is calculated
based on the brand and engine of the car.
This attribute is read only: it cannot be set and deleted:

.. code-block:: Python

    class DescPrice():
        \"""price attribute\"""
        def __get__(self,instance,owner):
            if instance._brand.lower() in ("bmw","mercedes"):
                price = instance._engine*30
            elif instance._brand.lower() == 'audi':
                price = instance._engine*25
            elif instance._brand.lower() == 'vw':
                price = instance._engine*20
            else:
                price = instance._engine*15
            return price
        def __set__(self,instance,value):
            raise AttributeError("attribute cannot be set")
        def __delete__(self,instance):
            raise AttributeError("attribute cannot be deleted")

The following ``engine`` descriptor defines methods for getting and setting
the ``engine`` attribute.
This attribute cannot be deleted as well:

.. code-block:: Python

    class DescEngine():
        \"""engine attribute\"""
        def __get__(self,instance,owner):
            return instance._engine
        def __set__(self,instance,value):
            instance._engine = value
        def __delete__(self,instance):
            raise AttributeError("attribute cannot be deleted")

The following ``model`` descriptor defines methods for getting, setting
and deleting the ``model`` attribute:

.. code-block:: Python

    class DescModel():
        \"""model attribute\"""
        def __get__(self,instance,owner):
            return instance._model
        def __set__(self,instance,value):
            instance._model = value
        def __delete__(self,instance):
            del instance._model

The following class makes use of the descriptors defined above:

.. code-block:: Python

    class Car:
        def __init__(self,brand,model,engine):
            self._brand  = brand
            self._model  = model
            self._engine = engine
        def __repr__(self):
            return 'Car(%r,%r,%r,%r)' % (self.__class__.__name__,self._brand,
                    self._model, self._engine)
        model  = DescModel()
        engine = DescEngine()
        price  = DescPrice()

Creating a BMW:

>>> a_bmw = Car('BMW','3 series',2500)
>>> a_bmw
Car('Car','BMW','3 series',2500)
>>> a._bmw.price
75000

Trying to set the ``price`` attribute:

>>> a._bmw.price = 80000
AttributeError: attribute cannot be set

Changing the ``engine`` attribute:

>>> a_bmw.engine = 3000
>>> a_bmw
Car('Car','BMW','3 series',3000)
>>> a._bmw.price
90000

Trying to delete the ``engine`` attribute:

>>> del a_bmw.engine
AttributeError: attribute cannot be deleted

Deleting and creating new ``model`` attribute:

>>> del a_bmw.model
>>> a_bmw.model = '5 series'
>>> a_bmw
Car('Car','BMW','5 series',3000)

>>> dir(a_bmw)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
'__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__',
'__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
'__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
'_brand', '_engine', '_model', 'engine', 'model', 'price']
"""

def feature93():
    """Descriptors"""
    print('Descriptors')
    print('===========\n')
    print(':py:mod:`codesnippets.feature93`')
    print('--------------------------------\n')
    print('Descriptors are another way to control attribute access, and they need\n'
          'to be created as separate classes.\n')
    print("The following ``price`` descriptor defines how the price is calculated")
    print("based on the brand and engine of the car.")
    print("This attribute is read only: it cannot be set and deleted:\n")
    print('.. code-block:: Python\n')
    print("""    class DescPrice():
        \\\"""price attribute\\\"""
        def __get__(self,instance,owner):
            if instance._brand.lower() in ("bmw","mercedes"):
                price = instance._engine*30
            elif instance._brand.lower() == 'audi':
                price = instance._engine*25
            elif instance._brand.lower() == 'vw':
                price = instance._engine*20
            else:
                price = instance._engine*15
            return price
        def __set__(self,instance,value):
            raise AttributeError("attribute cannot be set")
        def __delete__(self,instance):
            raise AttributeError("attribute cannot be deleted")
        """)
    class DescPrice():
        """price attribute"""
        def __get__(self,instance,owner):
            """get method"""
            if instance._brand.lower() in ("bmw","mercedes"):
                price = instance._engine*30
            elif instance._brand.lower() == 'audi':
                price = instance._engine*25
            elif instance._brand.lower() == 'vw':
                price = instance._engine*20
            else:
                price = instance._engine*15
            return price
        def __set__(self,instance,value):
            """set method"""
            raise AttributeError("attribute cannot be set")
        def __delete__(self,instance):
            """delete method"""
            raise AttributeError("attribute cannot be deleted")
    print("The following ``engine`` descriptor defines methods for getting and setting")
    print("the ``engine`` attribute.")
    print("This attribute cannot be deleted as well:\n")
    print('.. code-block:: Python\n')
    print("""    class DescEngine():
        \\\"""engine attribute\\\"""
        def __get__(self,instance,owner):
            return instance._engine
        def __set__(self,instance,value):
            instance._engine = value
        def __delete__(self,instance):
            raise AttributeError("attribute cannot be deleted")
        """)
    class DescEngine():
        """engine attribute"""
        def __get__(self,instance,owner):
            """get access method"""
            return instance._engine
        def __set__(self,instance,value):
            """set access method"""
            instance._engine = value
        def __delete__(self,instance):
            """delete access method"""
            raise AttributeError("attribute cannot be deleted")
    print("The following ``model`` descriptor defines methods for getting, setting")
    print("and deleting the ``model`` attribute:\n")
    print('.. code-block:: Python\n')
    print("""    class DescModel():
        \\\"""model attribute\\\"""
        def __get__(self,instance,owner):
            return instance._model
        def __set__(self,instance,value):
            instance._model = value
        def __delete__(self,instance):
            del instance._model
        """)
    class DescModel():
        """model attribute"""
        def __get__(self,instance,owner):
            """get access method"""
            return instance._model
        def __set__(self,instance,value):
            """set access method"""
            instance._model = value
        def __delete__(self,instance):
            """delete access method"""
            del instance._model
    print("The following class makes use of the descriptors defined above:\n")
    print('.. code-block:: Python\n')
    print("""    class Car:
        def __init__(self,brand,model,engine):
            self._brand  = brand
            self._model  = model
            self._engine = engine
        def __repr__(self):
            return 'Car(%r,%r,%r,%r)' % (self.__class__.__name__,self._brand, self._model, self._engine)
        model  = DescModel()
        engine = DescEngine()
        price  = DescPrice()
        """)
    class Car:
        """a car class"""
        def __init__(self,brand,model,engine):
            self._brand  = brand
            self._model  = model
            self._engine = engine
        def __repr__(self):
            return 'Car(%r,%r,%r,%r)' % (self.__class__.__name__,self._brand,
                                         self._model, self._engine)
        model  = DescModel()
        engine = DescEngine()
        price  = DescPrice()
    print("Creating a BMW:\n")
    print(">>> a_bmw = Car('BMW','3 series',2500)")
    a_bmw = Car('BMW','3 series',2500)
    print(">>> a_bmw")
    print(a_bmw)
    print(">>> a._bmw.price")
    print(a_bmw.price)
    print()
    print("Trying to set the ``price`` attribute:\n")
    try:
        print(">>> a._bmw.price = 80000")
        a_bmw.price = 80000
    except AttributeError as exc:
        print(exc.__class__.__name__ + ': ' + str(exc))
    print()
    print("Changing the engine:\n")
    a_bmw.engine = 3000
    print(">>> a_bmw.engine = 3000")
    print(">>> a_bmw")
    print(a_bmw)
    print(">>> a_bmw.price")
    print(a_bmw.price)
    print("\nTrying to delete the ``engine`` attribute:\n")
    try:
        print(">>> del a_bmw.engine")
        del a_bmw.engine
    except AttributeError as exc:
        print(exc.__class__.__name__ + ': ' + str(exc))
    print()
    print("Deleting and creating new ``model`` attribute:\n")
    print(">>> del a_bmw.model")
    del a_bmw.model
    print(">>> a_bmw.model = '5 series'")
    a_bmw.model = '5 series'
    print(">>> a_bmw")
    print(a_bmw)
    print()
    print(">>> dir(a_bmw)")
    print(dir(a_bmw))
    print(80*'-')
