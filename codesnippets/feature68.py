##    Python codesnippets - Operator overloading: __call__, __len__, __bool__
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
# Feature 68
#

"""
Operator overloading: ``__call__`` , ``__len__`` , ``__bool__``
===============================================================

:py:mod:`codesnippets.feature68`
--------------------------------

The following operators are also available for classes to be overloaded:

* ``__call__`` is used on instance invocation
* ``__len__`` provides the length of an instance
* ``__bool__`` is called when a boolean equivalent value of the instance is needed

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
        def __contains__(self, value):
            print('	-> MyContainer.__contains__')
            return value in self._data
        def __iter__(self):
            print('	-> MyContainer.__iter__')
            for v_val in self._data:
                yield v_val
        def __getitem__(self,key):
            print('	-> MyContainer.__getitem__')
            return self._data[key]
        def __setitem__(self,key,value):
            print('	-> MyContainer.__setitem__')
            self._data[key] = value
        def __call__(self,value):
            print('	-> MyContainer.__call__')
            data = [x_val*value for x_val in self._data]
            return MyContainer(data)
        def __len__(self):
            print('	-> MyContainer.__len__')
            return len(self._data)
        def __bool__(self):
            print('	-> MyContainer.__bool__')
            return sum(self._data) > 0

``MyContainer`` instances are created as usual:

>>> container1 = MyContainer([0,1,2,3,4,5])
	-> MyContainer.__init__
>>> container1
	-> MyContainer.__repr__
MyContainer(data=[0, 1, 2, 3, 4, 5])

Instances can be called like functions and the behaviour can be coded in the ``__call__`` operator:

>>> container1(3)
	-> MyContainer.__call__
	-> MyContainer.__init__
	-> MyContainer.__repr__
MyContainer(data=[0, 3, 6, 9, 12, 15])

If a length of an instance is needed, this can be coded inside ``__len__``:

>>> len(container1)
	-> MyContainer.__len__
6

A boolean value is generated by calling ``__bool__``:

>>> bool(container1)
	-> MyContainer.__bool__
True

.. note:: If no ``__bool__`` operator is overloaded, Python calls ``__len__`` to infer a boolean
    value of the object: positive length means the instance is true.
"""

def feature68():
    """Operator overloading: __call__, __len__, __bool__"""
    print('Operator overloading: ``__call__`` , ``__len__`` , ``__bool__``')
    print('===============================================================\n')
    print(':py:mod:`codesnippets.feature68`')
    print('--------------------------------\n')
    print('The following operators are also available for classes to be overloaded:\n')
    print('* ``__call__`` is used on instance invocation')
    print('* ``__len__`` provides the length of an instance')
    print('* ``__bool__`` is called when a boolean equivalent value of the instance is needed\n')
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
        def __contains__(self, value):
            print('\t-> MyContainer.__contains__')
            return value in self._data
        def __iter__(self):
            print('\t-> MyContainer.__iter__')
            for v_val in self._data:
                yield v_val
        def __getitem__(self,key):
            print('\t-> MyContainer.__getitem__')
            return self._data[key]
        def __setitem__(self,key,value):
            print('\t-> MyContainer.__setitem__')
            self._data[key] = value
        def __call__(self,value):
            print('\t-> MyContainer.__call__')
            data = [x_val*value for x_val in self._data]
            return MyContainer(data)
        def __len__(self):
            print('\t-> MyContainer.__len__')
            return len(self._data)
        def __bool__(self):
            print('\t-> MyContainer.__bool__')
            return sum(self._data) > 0
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
        def __contains__(self, value):
            print('\t-> MyContainer.__contains__')
            return value in self._data
        def __iter__(self):
            print('\t-> MyContainer.__iter__')
            for v_val in self._data:
                yield v_val
        def __getitem__(self,key):
            print('\t-> MyContainer.__getitem__')
            return self._data[key]
        def __setitem__(self,key,value):
            print('\t-> MyContainer.__setitem__')
            self._data[key] = value
        def __call__(self,value):
            print('\t-> MyContainer.__call__')
            data = [x_val*value for x_val in self._data]
            return MyContainer(data)
        def __len__(self):
            print('\t-> MyContainer.__len__')
            return len(self._data)
        def __bool__(self):
            print('\t-> MyContainer.__bool__')
            return sum(self._data) > 0
    print('``MyContainer`` instances are created as usual:\n')
    print('>>> container1 = MyContainer([0,1,2,3,4,5])')
    container1 = MyContainer([0,1,2,3,4,5])
    print('>>> container1')
    print(container1)
    print('\nInstances can be called like functions and the behaviour can be '
          'coded in the ``__call__`` operator:\n')
    print(">>> container1(3)")
    print(container1(3))
    print('\nIf a length of an instance is needed, this can be coded inside ``__len__``:\n')
    print(">>> len(container1)")
    print(len(container1))
    print('\nA boolean value is generated by calling ``__bool__``:\n')
    print(">>> bool(container1)")
    print(bool(container1))
    print('\n.. note:: If no ``__bool__`` operator is overloaded, Python calls ``__len__`` to '
          'infer a boolean\n    value of the object: positive length means the instance is true.')
    print(80*'-')