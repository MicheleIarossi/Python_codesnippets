##    Python codesnippets - Operator overloading: iteration protocol
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
# Feature 66
#

"""
Operator overloading: iteration protocol
========================================

:py:mod:`codesnippets.feature66`
--------------------------------

In order to support the iteration protocol in a given class, the:

* ``__iter__`` operator needs to be implemented and it must return an iterator class
* ``__next__`` operator needs to be implemented in the iterator class


In the following, the ``MyContainerClass`` from :doc:`Operator overloading: add, sub, and basic
indexing<feature65>` is adapted for supporting the iteration protocol. By implementing the
``__iter__`` operator instead of ``__getitem__`` , the class can return an iterator class instance:

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
            return MyContainerIterator(self._data)
        def __getitem__(self,key):
            print('	-> MyContainer.__getitem__')
            return self._data[key]
        def __setitem__(self,key,value):
            print('	-> MyContainer.__setitem__')
            self._data[key] = value

In the iterator class ``MyContainerIterator`` the ``__next__`` operator is used for scanning
each element one by one. Once the elements are exhausted, the ``StopIteration``
exception is raised:

.. code-block:: Python

    class MyContainerIterator:
        \"""a container iterator class\"""
        def __init__(self,data):
            print('	-> MyContainerIterator.__init__')
            self.data = data
            self.key  = 0
        def __next__(self):
            print('	-> MyContainerIterator.__next__')
            if self.key >= len(self.data):
                raise StopIteration
            value = self.data[self.key]
            self.key += 1
            return value
        def __repr__(self):
            \"""overloads repr operator\"""
            print('	-> MyContainerIterator.__repr__')
            return 'MyContainerIterator(data=%r)' % (self._data)

``MyContainer`` instances are created as usual:

>>> container1 = MyContainer([0,1,2,3,4,5])
	-> MyContainer.__init__
>>> container1
	-> MyContainer.__repr__
MyContainer(data=[0, 1, 2, 3, 4, 5])

The ``iter`` built-in function is applied now to ``container1`` for getting an iterator object back:

>>> iterator_container1 = iter(container1)
	-> MyContainer.__iter__
	-> MyContainerIterator.__init__

>>> next(iterator_container1), next(iterator_container1), next(iterator_container1)
	-> MyContainerIterator.__next__
	-> MyContainerIterator.__next__
	-> MyContainerIterator.__next__
0 1 2

.. seealso:: :doc:`The iteration protocol<feature27>`
"""

def feature66():
    """Operator overloading: iteration protocol"""
    print('Operator overloading: iteration protocol')
    print('========================================\n')
    print(':py:mod:`codesnippets.feature66`')
    print('--------------------------------\n')
    print('In order to support the iteration protocol in a given class, the:\n')
    print('* ``__iter__`` operator needs to be implemented and it must return an iterator class')
    print('* ``__next__`` operator needs to be implemented in the iterator class\n')
    print('\nIn the following, the ``MyContainerClass`` from '
          ':doc:`Operator overloading: add, sub, and\nbasic indexing<feature65>` is adapted for '
          'supporting the iteration protocol. By implementing the\n``__iter__`` '
          'operator instead of ``__getitem__``, the class can return '
          'an iterator class instance:\n')
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
            return MyContainerIterator(self._data)
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
            return MyContainerIterator(self._data)
        def __getitem__(self,key):
            print('\t-> MyContainer.__getitem__')
            return self._data[key]
        def __setitem__(self,key,value):
            print('\t-> MyContainer.__setitem__')
            self._data[key] = value
    print('In the iterator class ``MyContainerIterator`` the ``__next__`` operator is '
          'used for scanning each element one by one. Once the elements are exhausted, '
          'the ``StopIteration`` exception is raised:\n')
    print('.. code-block:: Python\n')
    print("""    class MyContainerIterator:
        \\\"""a container iterator class\\\"""
        def __init__(self,data):
            print('\t-> MyContainerIterator.__init__')
            self.data = data
            self.key  = 0
        def __next__(self):
            print('\t-> MyContainerIterator.__next__')
            if self.key >= len(self.data):
                raise StopIteration
            value = self.data[self.key]
            self.key += 1
            return value
        def __repr__(self):
            \\\"""overloads repr operator\\\"""
            print('\t-> MyContainerIterator.__repr__')
            return 'MyContainerIterator(data=%r)' % (self._data)
        """)
    class MyContainerIterator:
        """a container iterator class"""
        def __init__(self,data):
            print('\t-> MyContainerIterator.__init__')
            self._data = data
            self._key  = 0
        def __next__(self):
            print('\t-> MyContainerIterator.__next__')
            if self._key >= len(self._data):
                raise StopIteration
            value = self._data[self._key]
            self._key += 1
            return value
        def __repr__(self):
            """overloads repr operator"""
            print('\t-> MyContainerIterator.__repr__')
            return 'MyContainerIterator(data=%r)' % (self._data)

    print('``MyContainer`` instances are created as usual:\n')
    print('>>> container1 = MyContainer([0,1,2,3,4,5])')
    container1 = MyContainer([0,1,2,3,4,5])
    print('>>> container1')
    print(container1)
    print('\nThe ``iter`` built-in function is applied now to ``container1`` for getting an '
          'iterator object back:\n')
    print(">>> iterator_container1 = iter(container1)")
    iterator_container1 = iter(container1)
    print("\n>>> next(iterator_container1), next(iterator_container1), next(iterator_container1)")
    print(next(iterator_container1), next(iterator_container1), next(iterator_container1))
    print('\n.. seealso:: :doc:`The iteration protocol<feature27>`')
    print(80*'-')