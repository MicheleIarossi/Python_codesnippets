##    Python codesnippets - Operator overloading: add, sub, and basic indexing
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
# Feature 64
#

"""
Operator overloading: add, sub, and basic indexing
==================================================

:py:mod:`codesnippets.feature64`
--------------------------------

This is an example of a container class that implements also the:

* ``__add__`` operator, which is called when class instances are added ``+``
* ``__sub__`` operator, which is called when class instances are subtracted ``-``
* ``__getitem__``, ``__setitem__`` operators, which are called when class
  instances are indexed ``[]``

.. code-block:: Python

    class MyContainer:
        \"""my container class\"""
        def __init__(self,data):
            print('	-> MyContainer.__init__')
            self._data = data[:]
        def __repr__(self):
            print('	-> MyContainer.__repr__')
            return 'MyContainer(data=%r)' % (self._data)
        def __add__(self,other):
            print('	-> MyContainer.__add__')
            data = [x_val+y_val for (x_val,y_val) in zip(self._data,other._data)]
            return MyContainer(data)
        def __sub__(self,other):
            print('	-> MyContainer.__sub__')
            data = [x_val-y_val for (x_val,y_val) in zip(self._data,other._data)]
            return MyContainer(data)
        def __getitem__(self,key):
            print('	-> MyContainer.__getitem__')
            return self._data[key]
        def __setitem__(self,key,value):
            print('	-> MyContainer.__setitem__')
            self._data[key] = value

``MyContainer`` instances are created as usual:

>>> container1 = MyContainer([0,1,2,3,4,5])
	-> MyContainer.__init__
>>> container1
	-> MyContainer.__repr__
MyContainer(data=[0, 1, 2, 3, 4, 5])

>>> container2 = MyContainer([8,3,14,5,10,19])
	-> MyContainer.__init__
>>> container2
	-> MyContainer.__repr__
MyContainer(data=[8, 3, 14, 5, 10, 19])

Containers can be added:

>>> container3 = container1 + container2
	-> MyContainer.__add__
	-> MyContainer.__init__
>>> container3
	-> MyContainer.__repr__
MyContainer(data=[8, 4, 16, 8, 14, 24])

Containers can be subtracted:

>>> container3 = container2 - container1
	-> MyContainer.__sub__
	-> MyContainer.__init__
>>> container3
	-> MyContainer.__repr__
MyContainer(data=[8, 2, 12, 2, 6, 14])

Containers can be indexed (read and write):

>>> container3[5] = 31
	-> MyContainer.__setitem__
>>> container3
	-> MyContainer.__repr__
MyContainer(data=[8, 2, 12, 2, 6, 31])

>>> container3[2]
	-> MyContainer.__getitem__
12

.. note:: Index operators are also used in all iteration context.

For example:

* membership test

>>> 31 in container3
	-> MyContainer.__getitem__
	-> MyContainer.__getitem__
	-> MyContainer.__getitem__
	-> MyContainer.__getitem__
	-> MyContainer.__getitem__
	-> MyContainer.__getitem__
True

* list comprehension

>>> [elem for elem in container3]
	-> MyContainer.__getitem__
	-> MyContainer.__getitem__
	-> MyContainer.__getitem__
	-> MyContainer.__getitem__
	-> MyContainer.__getitem__
	-> MyContainer.__getitem__
	-> MyContainer.__getitem__
[8, 2, 12, 2, 6, 31]

* ``map`` call

>>> list(map(str,container3))
	-> MyContainer.__getitem__
	-> MyContainer.__getitem__
	-> MyContainer.__getitem__
	-> MyContainer.__getitem__
	-> MyContainer.__getitem__
	-> MyContainer.__getitem__
	-> MyContainer.__getitem__
['8', '2', '12', '2', '6', '31']

* sequence assignments

>>> (a_val,b_val,c_val,d_val,e_val,f_val) = container3
	-> MyContainer.__getitem__
	-> MyContainer.__getitem__
	-> MyContainer.__getitem__
	-> MyContainer.__getitem__
	-> MyContainer.__getitem__
	-> MyContainer.__getitem__
	-> MyContainer.__getitem__
>>> a_val,b_val,d_val,e_val,f_val
(8, 2, 12, 2, 6, 31)

* ``list()``, ``tuple()``, etc.

>>> list(container3), tuple(container3)
	-> MyContainer.__getitem__
	-> MyContainer.__getitem__
	-> MyContainer.__getitem__
	-> MyContainer.__getitem__
	-> MyContainer.__getitem__
	-> MyContainer.__getitem__
	-> MyContainer.__getitem__
	-> MyContainer.__getitem__
	-> MyContainer.__getitem__
	-> MyContainer.__getitem__
	-> MyContainer.__getitem__
	-> MyContainer.__getitem__
	-> MyContainer.__getitem__
	-> MyContainer.__getitem__
([8, 2, 12, 2, 6, 31], (8, 2, 12, 2, 6, 31))

"""

def feature64():
    """Operator overloading: add, sub, and basic indexing"""
    print('Operator overloading: add, sub, and basic indexing')
    print('==================================================\n')
    print(':py:mod:`codesnippets.feature64`')
    print('--------------------------------\n')
    print('This is an example of a container class that implements also the:\n')
    print('* ``__add__`` operator, which is called when class instances are added ``+``')
    print('* ``__sub__`` operator, which is called when class instances are subtracted ``-``')
    print('* ``__getitem__``, ``__setitem__`` operators, which are called when\n  class '
          'instances are indexed ``[]``\n')
    print('.. code-block:: Python\n')
    print("""    class MyContainer:
        \\\"""my container class\\\"""
        def __init__(self,data):
            print('\t-> MyContainer.__init__')
            self._data = data[:]
        def __repr__(self):
            print('\t-> MyContainer.__repr__')
            return 'MyContainer(data=%r)' % (self._data)
        def __add__(self,other):
            print('\t-> MyContainer.__add__')
            data = [x_val+y_val for (x_val,y_val) in zip(self._data,other._data)]
            return MyContainer(data)
        def __sub__(self,other):
            print('\t-> MyContainer.__sub__')
            data = [x_val-y_val for (x_val,y_val) in zip(self._data,other._data)]
            return MyContainer(data)
        def __getitem__(self,key):
            print('\t-> MyContainer.__getitem__')
            return self._data[key]
        def __setitem__(self,key,value):
            print('\t-> MyContainer.__setitem__')
            self._data[key] = value
    """)
    class MyContainer:
        """my container class"""
        def __init__(self,data):
            print('\t-> MyContainer.__init__')
            self._data = data[:]
        def __repr__(self):
            print('\t-> MyContainer.__repr__')
            return 'MyContainer(data=%r)' % (self._data)
        def __add__(self,other):
            print('\t-> MyContainer.__add__')
            data = [x_val+y_val for (x_val,y_val) in zip(self._data,other._data)]
            return MyContainer(data)
        def __sub__(self,other):
            print('\t-> MyContainer.__sub__')
            data = [x_val-y_val for (x_val,y_val) in zip(self._data,other._data)]
            return MyContainer(data)
        def __getitem__(self,key):
            print('\t-> MyContainer.__getitem__')
            return self._data[key]
        def __setitem__(self,key,value):
            print('\t-> MyContainer.__setitem__')
            self._data[key] = value
    print('``MyContainer`` instances are created as usual:\n')
    print('>>> container1 = MyContainer([0,1,2,3,4,5])')
    container1 = MyContainer([0,1,2,3,4,5])
    print('>>> container1')
    print(container1)
    print('\n>>> container2 = MyContainer([8,3,14,5,10,19])')
    container2 = MyContainer([8,3,14,5,10,19])
    print('>>> container2')
    print(container2)
    print('\nContainers can be added:\n')
    print('>>> container3 = container1 + container2')
    container3 = container1+container2
    print('>>> container3')
    print(container3)
    print('\nContainers can be subtracted:\n')
    print('>>> container3 = container2 - container1')
    container3 = container2 - container1
    print('>>> container3')
    print(container3)
    print('\nContainers can be indexed (read and write):\n')
    print('>>> container3[5] = 31')
    container3[5] = 31
    print('>>> container3')
    print(container3)
    print('\n>>> container3[2]')
    print(container3[2])
    print('\n.. note:: Index operators are also used in all iteration context.\n')
    print('For example:')
    print('\n* membership test\n')
    print('>>> 31 in container3')
    print(31 in container3)
    print('\n* list comprehension\n')
    print('>>> [elem for elem in container3]')
    print([elem for elem in container3])
    print('\n* ``map`` call\n')
    print('>>> list(map(str,container3))')
    print(list(map(str,container3)))
    print('\n* sequence assignments\n')
    print('>>> (a_val,b_val,c_val,d_val,e_val,f_val) = container3')
    (a_val,b_val,c_val,d_val,e_val,f_val) = container3
    print('>>> a_val,b_val,d_val,e_val,f_val')
    print((a_val,b_val,c_val,d_val,e_val,f_val))
    print('\n* ``list()``, ``tuple()``, etc.\n')
    print('>>> list(container3), tuple(container3)')
    print((list(container3), tuple(container3)))
    print(80*'-')
