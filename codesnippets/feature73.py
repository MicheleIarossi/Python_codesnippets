##    Python codesnippets - Inheritance attribute lister class
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
# Feature 73
#

"""
Inheritance attribute lister class
==================================

:py:mod:`codesnippets.feature73`
--------------------------------

The class below uses the ``dir()`` function for getting all attributes and names,
and the ``getattr()`` function for retrieving their values:

.. code-block:: Python

    class ClassInspector:
        \"""a self inspecting class\"""
        def __attr_list(self, indent=' '*4):
            \"""provides list of attributes\"""
            result  = 'Interns%s\\n%s%%s\\nOthers%s\\n' % ('-'*120, indent, '-'*120)
            unders = []
            for attr in dir(self):                              # Instance dir()
                if attr[:2] == '__' and attr[-2:] == '__':      # Skip internals
                    unders.append(attr)
                else:
                    display = str(getattr(self, attr))[:120-(len(indent) + len(attr))]
                    result += '%s%s=%s\\n' % (indent, attr, display)
            return result % ', '.join(unders)
        def __str__(self):
            \"""overloading repr operator\"""
            return '<Instance of %s, address 0x%x:\\n%s>' % (
                           self.__class__.__name__,         # My class's name
                           id(self),                        # My address
                           self.__attr_list())              # name=value list
        def __repr__(self):
            \"""overloading repr operator\"""
            return 'ClassInspector()'

The following are some test classes:

.. code-block:: Python

    class Parent:
        \"""a parent class\"""
        def __init__(self):
            self.data_parent = 100
        def parent_method_1(self):
            \"""a method function\"""
            pass
        def parent_method_2(self):
            \"""a method function\"""
            pass

    class Child(Parent, ClassInspector):
        \"""a child class\"""
        def __init__(self):
            Parent.__init__(self)
            self.data_child1 = 200
            self.data_child2 = 201
        def child_method_1(self):
            \"""a method function\"""
            pass
        def child_method_2(self):
            \"""a method function\"""
            pass

A ``Child`` object is created as follows:

>>> a_child = Child()

By invoking the ``print`` function on it, the ``__str__`` method of the ``ClassInspector`` is called:

>>> print(a_child)
<Instance of Child, address 0x7f9b4839d3a0:
Interns--------------------------------------------------------------------------------------------------------
    __class__, __delattr__, __dict__, __dir__, __doc__,
    __eq__, __format__, __ge__, __getattribute__, __gt__, __hash__,
    __init__, __init_subclass__, __le__, __lt__, __module__, __ne__,
    __new__, __reduce__, __reduce_ex__, __repr__, __setattr__, __sizeof__,
    __str__, __subclasshook__, __weakref__
Others---------------------------------------------------------------------------------------------------------
    _ClassInspector__attr_list=<bound method feature73.<locals>.ClassInspector.__attr_list of ClassInspector()>
    child_method_1=<bound method feature73.<locals>.Child.child_method_1 of ClassInspector()>
    child_method_2=<bound method feature73.<locals>.Child.child_method_2 of ClassInspector()>
    data_child1=200
    data_child2=201
    data_parent=100
    parent_method_1=<bound method feature73.<locals>.Parent.parent_method_1 of ClassInspector()>
    parent_method_2=<bound method feature73.<locals>.Parent.parent_method_2 of ClassInspector()>
>

.. seealso:: :doc:`dir() on an integer variable<feature1>`
"""

def feature73():
    """Inheritance attribute lister class"""
    print('Inheritance attribute lister class')
    print('==================================\n')
    print(':py:mod:`codesnippets.feature73`')
    print('--------------------------------\n')
    print('The class below uses the ``dir()`` function for getting all attributes and names,')
    print('and the ``getattr()`` function for retrieving their values:\n')
    class ClassInspector:
        """a self inspecting class"""
        def __attr_list(self, indent=' '*4, count=6):
            """provides list of attributes"""
            result  = 'Interns%s\n%s%%s\nOthers%s\n' % ('-'*104, indent, '-'*105)
            interns = []
            cnt = 0
            for attr in dir(self):                              # Instance dir()
                if attr[:2] == '__' and attr[-2:] == '__':      # Skip internals
                    cnt += 1
                    if cnt == count:
                        attr = '\n' + indent + attr
                        cnt = 0
                    interns.append(attr)
                else:
                    display = str(getattr(self, attr))[:120-(len(indent) + len(attr))]
                    result += '%s%s=%s\n' % (indent, attr, display)
            return result % ', '.join(interns)
        def __str__(self):
            """overloading str operator"""
            return '<Instance of %s, address 0x%x:\n%s>' % (
                           self.__class__.__name__,         # My class's name
                           id(self),                        # My address
                           self.__attr_list())              # name=value list
        def __repr__(self):
            """overloading repr operator"""
            return 'ClassInspector()'
    print('.. code-block:: Python\n')
    print("""    class ClassInspector:
        \\\"""a self inspecting class\\\"""
        def __attr_list(self, indent=' '*4):
            \\\"""provides list of attributes\\\"""
            result  = 'Interns%s\\\\n%s%%s\\\\nOthers%s\\\\n' % ('-'*120, indent, '-'*120)
            interns = []
            for attr in dir(self):                              # Instance dir()
                if attr[:2] == '__' and attr[-2:] == '__':      # Skip internals
                    interns.append(attr)
                else:
                    display = str(getattr(self, attr))[:120-(len(indent) + len(attr))]
                    result += '%s%s=%s\\\\n' % (indent, attr, display)
            return result % ', '.join(interns)
        def __str__(self):
            \\\"""overloading repr operator\\\"""
            return '<Instance of %s, address 0x%x:\\\\n%s>' % (
                           self.__class__.__name__,         # My class's name
                           id(self),                        # My address
                           self.__attr_list())              # name=value list
        def __repr__(self):
            \\\"""overloading repr operator\\\"""
            return 'ClassInspector()'
        """)
    print('The following are some test classes:\n')
    class Parent:
        """a parent class"""
        def __init__(self):
            self.data_parent = 100
        def parent_method_1(self):
            """a method function"""
            pass
        def parent_method_2(self):
            """a method function"""
            pass
    class Child(Parent, ClassInspector):
        """a child class"""
        def __init__(self):
            Parent.__init__(self)
            self.data_child1 = 200
            self.data_child2 = 201
        def child_method_1(self):
            """a method function"""
            pass
        def child_method_2(self):
            """a method function"""
            pass
    print('.. code-block:: Python\n')
    print("""    class Parent:
        \\\"""a parent class\\\"""
        def __init__(self):
            self.data_parent = 100
        def parent_method_1(self):
            \\\"""a method function\\\"""
            pass
        def parent_method_2(self):
            \\\"""a method function\\\"""
            pass
        """)
    print("""    class Child(Parent, ClassInspector):
        \\\"""a child class\\\"""
        def __init__(self):
            Parent.__init__(self)
            self.data_child1 = 200
            self.data_child2 = 201
        def child_method_1(self):
            \\\"""a method function\\\"""
            pass
        def child_method_2(self):
            \\\"""a method function\\\"""
            pass
        """)
    print('A ``Child`` object is created as follows:\n')
    print('>>> a_child = Child()')
    a_child = Child()
    print('\nBy invoking the ``print`` function on it, the ``__str__`` method of '
          'the ``ClassInspector`` is called:\n')
    print('>>> print(a_child)')
    print(a_child)
    print('\n.. seealso:: :doc:`dir() on an integer variable<feature1>`')
    print(80*'-')