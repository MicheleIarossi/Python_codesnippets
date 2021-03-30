##    Python codesnippets - Generic attribute management
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
# Feature 95
#

"""
Generic attribute management
============================

:py:mod:`codesnippets.feature95`
--------------------------------

By overloading the methods below access to any attribute can be controlled:

.. code-block:: Python

	def __getattr__(self,name)        # on undefined attribute fetch [obj.name]
	def __getattribute__(self,name)   # on all attribute fetch [obj.name]
	def __setattr__(self,name)        # on all attribute assignment [obj.name=value]
	def __delattr__(self,name)        # on all attribute deletion [del obj.name]

Above notice that ``__setattr__``  leads to infinite loops if
instance attributes are assigned directly:

.. code-block:: Python

	self.attr = val

Use

.. code-block:: Python

	self.__dict__[attr] = val

instead.
This avoids loops because the dictionary key is assigned and not the
attribute ``__dict__`` of the instance itself.

The following class defines a car and intercepts the attributes
``price``, ``model``, ``engine``:

.. code-block:: Python

	class Car:
            \"""a car class\"""
            def __init__(self,brand,model,engine):
                print(f'	-> Car.__init__({repr(brand)},{repr(model)},{repr(engine)})')
                self._brand  = brand    #    triggers __setattr__!
                self._model  = model    #    triggers __setattr__!
                self._engine = engine   #    triggers __setattr__!
            def __getattr__(self,attr):
                \"""overloads getattr operator\"""
                print(f'	-> Car.__setattr__({repr(attr)},{repr(value)})')
                if attr == "price":
                    if self._brand.lower() in ("bmw","mercedes"):
                        price = self._engine*30
                    elif instance._brand.lower() == 'audi':
                        price = self._engine*25
                    elif instance._brand.lower() == 'vw':
                        price = self._engine*20
                    else:
                        price = self._engine*15
                    return price
                elif attr in ("model","engine"):
                    attr = "_" + attr
                    return self.__dict__[attr]    # avoids looping
            def __setattr__(self,att,value):
                \"""overloads setattr operator\"""
                print(f'	-> Car.__setattr__({repr(attr)},{repr(value)})')
                if attr == "price"":
                    raise AttributeError("attribute cannot be set")
                elif attr in ("model","engine"):
                    attr = "_" + attr
                    self.__dict__[attr] = value   # avoids looping
            def __delattr__(self,attr):
                \"""overloads delete attribute operator\"""
                print(f'	-> Car.__delattr__({repr(attr)})')
                if attr in ("price","engine"):
                    raise AttributeError("attribute cannot be set")
                elif attr == "model":
                    del self.__dict__["_model"]   # avoids looping
            def __repr__(self):
                return 'Car(%r,%r,%r,%r)' % (self.__class__.__name__,self._brand,
                        self._model, self._engine)

Creating a BMW:

>>> a_bmw = Car('BMW','3 series',2500)
	-> Car.__init__('BMW','3 series',2500)
	-> Car.__setattr__('_brand','BMW')
	-> Car.__setattr__('_model','3 series')
	-> Car.__setattr__('_engine',2500)
>>> a_bmw
Car('Car','BMW','3 series',2500)
>>> a._bmw.price
	-> Car.__getattr__('price')
75000

Trying to set the price attribute:

>>> a_bmw.price = 80000
	-> Car.__setattr__('price',80000)
AttributeError: attribute cannot be set

Changing the engine:

>>> a_bmw.engine = 3000
	-> Car.__setattr__('engine',3000)
>>> a_bmw
Car('Car','BMW','3 series',3000)
>>> a_bmw.price
	-> Car.__getattr__('price')
90000

Trying to delete the engine attribute:

>>> del a_bmw.engine
	-> Car.__delattr__('engine')
AttributeError: attribute cannot be set

Deleting and creating new model attribute:

>>> del a_bmw.model
	-> Car.__delattr__('model')
>>> a_bmw.model = '5 series'
	-> Car.__setattr__('model','5 series')
>>> a_bmw
Car('Car','BMW','5 series',3000)

>>> dir(a_bmw)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
'__ge__', '__getattr__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__',
'__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
'__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_brand',
'_engine', '_model']

.. seealso:: :doc:`Usage of __getattr__ and __getattribute__<feature74>`
"""

def feature95():
    """Generic attribute management"""
    print('Generic attribute management')
    print('============================\n')
    print(':py:mod:`codesnippets.feature95`')
    print('--------------------------------\n')
    print('By overloading the methods below access to any attribute can be controlled:\n')
    print('.. code-block:: Python\n')
    print('\tdef __getattr__(self,name)        # on undefined attribute fetch [obj.name]')
    print('\tdef __getattribute__(self,name)   # on all attribute fetch [obj.name]')
    print('\tdef __setattr__(self,name)        # on all attribute assignment [obj.name=value]')
    print('\tdef __delattr__(self,name)        # on all attribute deletion [del obj.name]')
    print()
    print('Above notice that ``__setattr__``  leads to infinite loops if')
    print('instance attributes are assigned directly:\n')
    print('.. code-block:: Python\n')
    print('\tself.attr = val\n')
    print('Use\n')
    print('.. code-block:: Python\n')
    print('\tself.__dict__[attr] = val\n')
    print('instead.')
    print('This avoids loops because the dictionary key is assigned and not the')
    print('attribute ``__dict__`` of the instance itself.\n')
    print("The following class defines a car and intercepts the attributes")
    print("``price``, ``model``, ``engine``:\n")
    print('.. code-block:: Python\n')
    print("""\tclass Car:
            \\\"""a car class\\\"""
            def __init__(self,brand,model,engine):
                print(f'\t-> Car.__init__({repr(brand)},{repr(model)},{repr(engine)})')
                self._brand  = brand    #    triggers __setattr__!
                self._model  = model    #    triggers __setattr__!
                self._engine = engine   #    triggers __setattr__!
            def __getattr__(self,attr):
                \\\"""overloads getattr operator\\\"""
                print(f'\t-> Car.__setattr__({repr(attr)},{repr(value)})')
                if attr == "price":
                    if self._brand.lower() in ("bmw","mercedes"):
                        price = self._engine*30
                    elif instance._brand.lower() == 'audi':
                        price = self._engine*25
                    elif instance._brand.lower() == 'vw':
                        price = self._engine*20
                    else:
                        price = self._engine*15
                    return price
                elif attr in ("model","engine"):
                    attr = "_" + attr
                    return self.__dict__[attr]    # avoids looping
            def __setattr__(self,att,value):
                \\\"""overloads setattr operator\\\"""
                print(f'\t-> Car.__setattr__({repr(attr)},{repr(value)})')
                if attr == "price"":
                    raise AttributeError("attribute cannot be set")
                elif attr in ("model","engine"):
                    attr = "_" + attr
                    self.__dict__[attr] = value   # avoids looping
            def __delattr__(self,attr):
                \\\"""overloads delete attribute operator\\\"""
                print(f'\t-> Car.__delattr__({repr(attr)})')
                if attr in ("price","engine"):
                    raise AttributeError("attribute cannot be set")
                elif attr == "model":
                    del self.__dict__["_model"]   # avoids looping
            def __repr__(self):
                return 'Car(%r,%r,%r,%r)' % (self.__class__.__name__,self._brand,
                                             self._model, self._engine)
        """)
    class Car:
        """a car class"""
        def __init__(self,brand,model,engine):
            print(f'\t-> Car.__init__({repr(brand)},{repr(model)},{repr(engine)})')
            self._brand  = brand    #    triggers __setattr__!
            self._model  = model    #    triggers __setattr__!
            self._engine = engine   #    triggers __setattr__!
        def __getattr__(self,attr):
            """overloads getattr operator"""
            print(f'\t-> Car.__getattr__({repr(attr)})')
            if attr == "price":
                if self._brand.lower() in ("bmw","mercedes"):
                    price = self._engine*30
                elif self._brand.lower() == 'audi':
                    price = self._engine*25
                elif self._brand.lower() == 'vw':
                    price = self._engine*20
                else:
                    price = self._engine*15
                res = price
            elif attr in ("model","engine"):
                attr = "_" + attr
                res = self.__dict__[attr]    # avoids looping
            return res
        def __setattr__(self,attr,value):
            """overloads setattr operator"""
            print(f'\t-> Car.__setattr__({repr(attr)},{repr(value)})')
            if attr in ("_model","_engine","_brand"):
                self.__dict__[attr] = value   # avoids looping
            elif attr in ("model","engine"):
                attr = "_" + attr
                self.__dict__[attr] = value   # avoids looping
            elif attr == "price":
                raise AttributeError("attribute cannot be set")
        def __delattr__(self,attr):
            """overloads delete attribute operator"""
            print(f'\t-> Car.__delattr__({repr(attr)})')
            if attr == "model":
                del self.__dict__["_model"]   # avoids looping
            elif attr in ("price","engine"):
                raise AttributeError("attribute cannot be set")
        def __repr__(self):
            return 'Car(%r,%r,%r,%r)' % (self.__class__.__name__,self._brand,
                                         self._model, self._engine)
    print("Creating a BMW:\n")
    print(">>> a_bmw = Car('BMW','3 series',2500)")
    a_bmw = Car('BMW','3 series',2500)
    print(">>> a_bmw")
    print(a_bmw)
    print(">>> a._bmw.price")
    print(a_bmw.price)
    print("\nTrying to set the price attribute:\n")
    try:
        print(">>> a_bmw.price = 80000")
        a_bmw.price = 80000
    except AttributeError as exc:
        print(exc.__class__.__name__ + ': ' + str(exc))
    print()
    print("Changing the engine:\n")
    print(">>> a_bmw.engine = 3000")
    a_bmw.engine = 3000
    print(">>> a_bmw")
    print(a_bmw)
    print(">>> a_bmw.price")
    print(a_bmw.price)
    print("\nTrying to delete the engine attribute:\n")
    try:
        print(">>> del a_bmw.engine")
        del a_bmw.engine
    except AttributeError as exc:
        print(exc.__class__.__name__ + ': ' + str(exc))
    print()
    print("Deleting and creating new model attribute:\n")
    print(">>> del a_bmw.model")
    del a_bmw.model
    print(">>> a_bmw.model = '5 series'")
    a_bmw.model = '5 series'
    print(">>> a_bmw")
    print(a_bmw)
    print()
    print(">>> dir(a_bmw)")
    print(dir(a_bmw))
    print('\n.. seealso:: :doc:`Usage of __getattr__ and __getattribute__<feature74>`')
    print(80*'-')