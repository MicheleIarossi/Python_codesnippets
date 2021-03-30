##    Python codesnippets - Operator overloading: specific membership with __contains__
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
Operator overloading: specific membership with ``__contains__``
===============================================================

:py:mod:`codesnippets.feature68`
--------------------------------

Specific class membership requires the class to overload the ``__contains__``  operator.
In the following, the ``MyContainerClass`` from :doc:`Operator overloading: iteration
protocol via function generator<feature67>` is extended  to support specific membership testing:

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

``MyContainer`` instances are created as usual:

>>> container1 = MyContainer([0,1,2,3,4,5])
	-> MyContainer.__init__
>>> container1
	-> MyContainer.__repr__
MyContainer(data=[0, 1, 2, 3, 4, 5])

When membership of an element is tested, the ``__contains__`` operator of ``MyContainer`` is called:

>>> 9 in container1
	-> MyContainer.__contains__
False
>>> 3 in container1
	-> MyContainer.__contains__
True
"""

def feature68():
    """Operator overloading: specific membership with __contains__"""
    print('Operator overloading: specific membership with ``__contains__``')
    print('===============================================================\n')
    print(':py:mod:`codesnippets.feature68`')
    print('--------------------------------\n')
    print('Specific class membership requires the class to overload the ``__contains__`` '
          ' operator.\nIn the following, the ``MyContainerClass`` from '
          ':doc:`Operator overloading: iteration\nprotocol via function'
          ' generator<feature67>` is extended to support specific membership testing:\n')
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
    print('``MyContainer`` instances are created as usual:\n')
    print('>>> container1 = MyContainer([0,1,2,3,4,5])')
    container1 = MyContainer([0,1,2,3,4,5])
    print('>>> container1')
    print(container1)
    print('\nWhen membership of an element is tested, the ``__contains__`` operator'
          ' of ``MyContainer`` is called:\n')
    print('>>> 9 in container1')
    print(9 in container1)
    print('>>> 3 in container1')
    print(3 in container1)
    print(80*'-')