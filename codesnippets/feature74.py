##    Python codesnippets - Usage of __getattr__ and __getattribute__
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
# Feature 74
#

"""
Usage of ``__getattr__`` and ``__getattribute__``
=================================================

:py:mod:`codesnippets.feature74`
--------------------------------

In the delegation pattern, ``__getattr__`` is used for forwarding
undefined attribute fetches to encapsulated objects:

* ``__getattr__`` is called when the requested attribute is not defined for the current instance
* ``__getattribute__`` is always called on every attribute fetch, irrespective of the requested
  attribute being defined or not for the current instance

Consider the following classes:

.. code-block:: Python

    class ClassA:
        \"""a class\"""
        def __init__(self,val):
            self.data_a = val

    class ClassB:
        \"""another class\"""
        def __init__(self,val):
            self.data_b = val
            self.obj_a  = ClassA(val*10)
        def __getattr__(self,attrstr):
            print('	-> ClassB.__getattr__(self,%s)' % (attrstr))
            return getattr(self.obj_a, attrstr)
        def __getattribute__(self,attrstr):
            print('	-> ClassB.__getattribute__(self,%s)' % (attrstr))
            return object.__getattribute__(self,attrstr)

Given an object of ``ClassB``:

>>> obj_b = ClassB(8)

the following attribute fetch of ``data_b`` is defined for ``obj_b`` and only
``__getattribute__`` is called:

>>> obj_b.data_b
	-> ClassB.__getattribute__(self,data_b)
8

But the following attribute fetch of ``data_a`` is undefined for ``obj_b``:

>>> obj_b.data_a # instance obj_b has no attribute data_a!
	-> ClassB.__getattribute__(self,data_a)
	-> ClassB.__getattr__(self,data_a)
	-> ClassB.__getattribute__(self,obj_a)
80

From the calls above notice that:

* ``__getattribute__`` is called irrespective of ``data_a`` being defined or undefined for ``obj_b``
* ``__getattr__`` is called because ``data_a`` is undefined for ``obj_b``
* ``__getattribute__`` is called again because of the attribute fetch ``self.obj_a``
  inside ``ClassB.__getattr__``
"""

def feature74():
    """Usage of __getattr__ and __getattribute__"""
    print('Usage of ``__getattr__`` and ``__getattribute__``')
    print('=================================================\n')
    print(':py:mod:`codesnippets.feature74`')
    print('--------------------------------\n')
    print('In the delegation pattern, ``__getattr__`` is used for forwarding')
    print('undefined attribute fetches to encapsulated objects:\n')
    print('* ``__getattr__`` is called when the requested attribute is not defined '
          'for the current instance')
    print('* ``__getattribute__`` is always called on every attribute fetch, irrespective '
          'of the requested\n  attribute being defined or not for the current instance\n')
    print('Consider the following classes:\n')
    class ClassA:
        """a class"""
        def __init__(self,val):
            self.data_a = val
    print('.. code-block:: Python\n')
    print("""    class ClassA:
        \\\"""a class\\\"""
        def __init__(self,val):
            self.data_a = val
        """)
    class ClassB:
        """another class"""
        def __init__(self,val):
            self.data_b = val
            self.obj_a  = ClassA(val*10)
        def __getattr__(self,attrstr):
            print('\t-> ClassB.__getattr__(self,%s)' % (attrstr))
            return getattr(self.obj_a, attrstr)
        def __getattribute__(self,attrstr):
            print('\t-> ClassB.__getattribute__(self,%s)' % (attrstr))
            return object.__getattribute__(self,attrstr)
    print("""    class ClassB:
        \\\"""another class\\\"""
        def __init__(self,val):
            self.data_b = val
            self.obj_a  = ClassA(val*10)
        def __getattr__(self,attrstr):
            print('\t-> ClassB.__getattr__(self,%s)' % (attrstr))
            return getattr(self.obj_a, attrstr)
        def __getattribute__(self,attrstr):
            print('\t-> ClassB.__getattribute__(self,%s)' % (attrstr))
            return object.__getattribute__(self,attrstr)
        """)
    print('Given an object of ``ClassB``:\n')
    print('>>> obj_b = ClassB(8)')
    obj_b = ClassB(8)
    print('\nthe following attribute fetch of ``data_b`` is defined for ``obj_b`` and '
          'only\n``__getattribute__`` is called:\n')
    print('>>> obj_b.data_b')
    print(obj_b.data_b)
    print('\nBut the following attribute fetch of ``data_a`` is undefined for ``obj_b``:\n')
    print('>>> obj_b.data_a # instance obj_b has no attribute data_a!')
    print(obj_b.data_a)
    print('\nFrom the calls above notice that:\n')
    print('* ``__getattribute__`` is called irrespective of ``data_a`` being defined '
          'or undefined for ``obj_b``')
    print('* ``__getattr__`` is called because ``data_a`` is undefined '
          'for ``obj_b``')
    print('* ``__getattribute__`` is called again because of the attribute '
          'fetch ``self.obj_a``\n  inside ``ClassB.__getattr__``')
    print(80*'-')