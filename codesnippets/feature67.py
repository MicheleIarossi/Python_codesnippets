##    Python codesnippets - Operator overloading: iteration protocol via function generator
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
# Feature 67
#

"""
Operator overloading: iteration protocol via function generator
===============================================================

:py:mod:`codesnippets.feature67`
--------------------------------

In the following, the ``MyContainerClass`` from :doc:`Operator overloading:
add, sub, and basic indexing<feature65>` is adapted for supporting the
iteration protocol via function generators. By implementing the ``__iter__`` operator
and by returning a function generator, which is an iterator, the class
can still use the iteration protocol:

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

The ``iter`` built-in function is applied now to ``container1`` for getting
a function generator back:

>>> iterator_container1 = iter(container1)

>>> next(iterator_container1), next(iterator_container1), next(iterator_container1)
	-> MyContainer.__iter__
0 1 2

.. seealso:: :doc:`Function generators<feature48>`
"""

def feature67():
    """Operator overloading: iteration protocol via function generator"""
    print('Operator overloading: iteration protocol via function generator')
    print('===============================================================\n')
    print(':py:mod:`codesnippets.feature67`')
    print('--------------------------------\n')
    print('In the following, the ``MyContainerClass`` from '
          ':doc:`Operator overloading:\nadd, sub, and basic indexing<feature65>` is adapted for '
          'supporting the\niteration protocol via function generators.'
          'By implementing the ``__iter__`` operator\nand by returning a function '
          'generator, which is an iterator, the class\ncan still use the iteration protocol:\n')
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
    print('\nThe ``iter`` built-in function is applied now to ``container1`` for getting\n'
          'a function generator back:\n')
    iterator_container1 = iter(container1)
    print(">>> iterator_container1 = iter(container1)")
    print("\n>>> next(iterator_container1), next(iterator_container1), next(iterator_container1)")
    print(next(iterator_container1), next(iterator_container1), next(iterator_container1))
    print('\n.. seealso:: :doc:`Function generators<feature48>`')
    print(80*'-')