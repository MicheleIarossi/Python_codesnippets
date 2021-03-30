##    Python codesnippets - Unbound and bound methods
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
# Feature 72
#

"""
Unbound and bound methods
=========================

:py:mod:`codesnippets.feature72`
--------------------------------

Since everything in Python is an object, methods of classes and instances
can be used as callback functions, but bound methods do not need an explicit
reference to an instance:

.. code-block:: Python

    class MyClass:
        \"""a class\"""
        def __init__(self,name):
            self._name = name
            print('<Object %s>' % (self._name))
        def function(self,val):
            \"""a method function\"""
            print('<Object %s>.function(%s)' % (self._name,val)
        def __repr__(self):
            \"""overloads repr operator\"""
            return 'MyClass(name=%r)' % (self._name)

The following objects are 2 instances of the class ``MyClass`` above:

>>> obj1 = MyClass('obj1')
<Object obj1>

>>> obj2 = MyClass('obj2')
<Object obj2>

The variable ``f1_func`` saves a reference to the bound method of the instance ``obj1``:

>>> f1_func = obj1.function     # Bound method to the instance obj1

On the contrary, the variable ``f2_func`` saves a reference to the
unbound method of the class ``MyClass``:

>>> f2_func = MyClass.function  # Unbound method to the class AClass

The function references above can be called in other contexts:

* ``f1_func`` works directly because already bound to ``obj1``

>>> f1_func(5)
<Object obj1>.function(5)

* ``f2_func`` still needs a reference to an object because unbound

>>> f2_func(obj2,5)
<Object obj2>.function(5)
"""

def feature72():
    """Unbound and bound methods"""
    print('Unbound and bound methods')
    print('=========================\n')
    print(':py:mod:`codesnippets.feature72`')
    print('--------------------------------\n')
    print('Since everything in Python is an object, methods of classes and instances')
    print('can be used as callback functions, but bound methods do not need an explicit')
    print('reference to an instance:\n')
    class MyClass:
        """a class"""
        def __init__(self,name):
            self._name = name
            print('<Object %s>' % (self._name))
        def function(self,val):
            """a method function"""
            print('<Object %s>.function(%s)' % (self._name,val))
        def __repr__(self):
            """overloads repr operator"""
            return 'MyClass(name=%r)' % (self._name)
    print('.. code-block:: Python\n')
    print("""    class MyClass:
        \\\"""a class\\\"""
        def __init__(self,name):
            self._name = name
            print('<Object %s>' % (self._name))
        def function(self,val):
            \\\"""a method function\\\"""
            print('<Object %s>.function(%s)' % (self._name,val)
        def __repr__(self):
            \\\"""overloads repr operator\\\"""
            return 'MyClass(name=%r)' % (self._name)
        """)
    print('The following objects are 2 instances of the class ``MyClass`` above:\n')
    print(">>> obj1 = MyClass('obj1')")
    obj1 = MyClass('obj1')
    print("\n>>> obj2 = MyClass('obj2')")
    obj2 = MyClass('obj2')
    print('\nThe variable ``f1_func`` saves a reference to the bound method of '
          'the instance ``obj1``:\n')
    print('>>> f1_func = obj1.function    # Bound method to the instance obj1')
    f1_func = obj1.function
    print('\nOn the contrary, the variable ``f2_func`` saves a reference to the\n'
          'unbound method of the class ``MyClass``:\n')
    print('>>> f2_func = MyClass.function  # Unbound method to the class AClass')
    f2_func = MyClass.function
    print('\nThe function references above can be called in other contexts:')
    print('\n* ``f1_func`` works directly because already bound to ``obj1``\n')
    print('>>> f1_func(5)')
    f1_func(5)
    print('\n* ``f2_func`` still needs a reference to an object because unbound\n')
    print('>>> f2_func(obj2,5)')
    f2_func(obj2,5)
    print(80*'-')