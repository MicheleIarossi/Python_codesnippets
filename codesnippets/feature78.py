##    Python codesnippets - Tracing instance attributes
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
# Feature 78
#

"""
Tracing instance attributes
===========================

:py:mod:`codesnippets.feature78`
--------------------------------

The class attribute ``__mro__`` can be used for tracing the attributes of an instance:

.. code-block:: Python

    def trace_attributes(an_obj):
        \"""prints all the attributes of an instance\"""
        allattr  = dir(an_obj)
        attrtree = (an_obj,) + an_obj.__class__.__mro__
        for attr in allattr:
            for obj in attrtree:
                if hasattr(obj,'__dict__') and attr in getattr(obj,'__dict__'):
                    if attr[:2] == attr[-2:] == '__':
                        print('%20s : %s' % (attr,obj))
                    else:
                        print('%20s : %s (%s)' % (attr,obj,getattr(an_obj,attr)))
                    break

Given the following hierarchy of classes:

.. code-block:: Python

    class ClassA:
        \"""a class\"""
        a_val = 1
        def __init__(self):
            self.b_val  = 2
            self.c_val  = 3
            self.d_val  = 4
        def __repr__(self):
            return 'ClassA()'

    class ClassB(ClassA):
        \"""a derived class\"""
        e_val  = 5
        def __init__(self):
            ClassA.__init__(self)
            self.f_val  = 6
            self.g_val  = 7
        def __repr__(self):
            return 'ClassB()'

    class ClassC(ClassA):
        \"""another derived class\"""
        h_val  = 8
        def __init__(self):
            ClassA.__init__(self)
            self.i_val  = 9
            self.j_val  = 10
        def __repr__(self):
            return 'ClassC()'

    class ClassD(ClassB,ClassC):
        \"""multiple inheritance class\"""
        k_val  = 11
        def __init__(self):
            ClassB.__init__(self)
            ClassC.__init__(self)
            self.l_val  = 12
            self.m_val  = 13
        def __repr__(self):
            return 'ClassD()'

and an instance of ``ClassD``:

>>> obj_d = ClassD()

>>> dir(obj_d)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
'__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
'__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
'__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'a_val', 'b_val', 'c_val', 'd_val',
'e_val', 'f_val', 'g_val', 'h_val', 'i_val', 'j_val', 'k_val', 'l_val', 'm_val']

>>> obj_d.__dict__
{'b_val': 2, 'c_val': 3, 'd_val': 4, 'f_val': 6, 'g_val': 7,
'i_val': 9, 'j_val': 10, 'l_val': 12, 'm_val': 13}

>>> obj_d.__class__.__mro__
<class 'codesnippets.feature78.feature78.<locals>.ClassD'>,
<class 'codesnippets.feature78.feature78.<locals>.ClassB'>,
<class 'codesnippets.feature78.feature78.<locals>.ClassC'>,
<class 'codesnippets.feature78.feature78.<locals>.ClassA'>,
<class 'object'>)

its attributes are traced by invoking the function ``trace_attributes``:

>>> trace_attributes(obj_d)
           __class__ : <class 'object'>
         __delattr__ : <class 'object'>
            __dict__ : <class 'codesnippets.feature78.feature78.<locals>.ClassA'>
             __dir__ : <class 'object'>
             __doc__ : <class 'codesnippets.feature78.feature78.<locals>.ClassD'>
              __eq__ : <class 'object'>
          __format__ : <class 'object'>
              __ge__ : <class 'object'>
    __getattribute__ : <class 'object'>
              __gt__ : <class 'object'>
            __hash__ : <class 'object'>
            __init__ : <class 'codesnippets.feature78.feature78.<locals>.ClassD'>
   __init_subclass__ : <class 'object'>
              __le__ : <class 'object'>
              __lt__ : <class 'object'>
          __module__ : <class 'codesnippets.feature78.feature78.<locals>.ClassD'>
              __ne__ : <class 'object'>
             __new__ : <class 'object'>
          __reduce__ : <class 'object'>
       __reduce_ex__ : <class 'object'>
            __repr__ : <class 'codesnippets.feature78.feature78.<locals>.ClassD'>
         __setattr__ : <class 'object'>
          __sizeof__ : <class 'object'>
             __str__ : <class 'object'>
    __subclasshook__ : <class 'object'>
         __weakref__ : <class 'codesnippets.feature78.feature78.<locals>.ClassA'>
               a_val : <class 'codesnippets.feature78.feature78.<locals>.ClassA'> (1)
               b_val : ClassD() (2)
               c_val : ClassD() (3)
               d_val : ClassD() (4)
               e_val : <class 'codesnippets.feature78.feature78.<locals>.ClassB'> (5)
               f_val : ClassD() (6)
               g_val : ClassD() (7)
               h_val : <class 'codesnippets.feature78.feature78.<locals>.ClassC'> (8)
               i_val : ClassD() (9)
               j_val : ClassD() (10)
               k_val : <class 'codesnippets.feature78.feature78.<locals>.ClassD'> (11)
               l_val : ClassD() (12)
               m_val : ClassD() (13)

Notice how only the class attributes belong to their respective classes, and all the
other attributes belong to the instance.

.. seealso:: :doc:`Method resolution order (MRO)<feature77>`
"""

def trace_attributes(an_obj):
    """prints all the attributes of an instance"""
    allattr  = dir(an_obj)
    attrtree = (an_obj,) + an_obj.__class__.__mro__
    for attr in allattr:
        for obj in attrtree:
            if hasattr(obj,'__dict__') and attr in getattr(obj,'__dict__'):
                if attr[:2] == attr[-2:] == '__':
                    print('%20s : %s' % (attr,obj))
                else:
                    print('%20s : %s (%s)' % (attr,obj,getattr(an_obj,attr)))
                break

def feature78():
    """Tracing instance attributes"""
    print('Tracing instance attributes')
    print('===========================\n')
    print(':py:mod:`codesnippets.feature78`')
    print('--------------------------------\n')
    print('The class attribute ``__mro__`` can be used for tracing the'
          ' attributes of an instance:\n')
    print('.. code-block:: Python\n')
    print("""    def trace_attributes(an_obj):
        \\\"""prints all the attributes of an instance\\\"""
        allattr  = dir(an_obj)
        attrtree = (an_obj,) + an_obj.__class__.__mro__
        for attr in allattr:
            for obj in attrtree:
                if hasattr(obj,'__dict__') and attr in getattr(obj,'__dict__'):
                    if attr[:2] == attr[-2:] == '__':
                        print('%20s : %s' % (attr,obj))
                    else:
                        print('%20s : %s (%s)' % (attr,obj,getattr(an_obj,attr)))
                    break
        """)
    print('Given the following hierarchy of classes:\n')
    print('.. code-block:: Python\n')
    print("""    class ClassA:
        \\\"""a class\\\"""
        a_val = 1
        def __init__(self):
            self.b_val  = 2
            self.c_val  = 3
            self.d_val  = 4
        def __repr__(self):
            return 'ClassA()'
        """)
    class ClassA:
        """a class"""
        a_val = 1
        def __init__(self):
            self.b_val  = 2
            self.c_val  = 3
            self.d_val  = 4
        def __repr__(self):
            """overloads repr operator"""
            return 'ClassA()'
    print("""    class ClassB(ClassA):
        \\\"""a derived class\\\"""
        e_val  = 5
        def __init__(self):
            ClassA.__init__(self)
            self.f_val  = 6
            self.g_val  = 7
        def __repr__(self):
            return 'ClassB()'
        """)
    class ClassB(ClassA):
        """a derived class"""
        e_val  = 5
        def __init__(self):
            ClassA.__init__(self)
            self.f_val  = 6
            self.g_val  = 7
        def __repr__(self):
            """overloads repr operator"""
            return 'ClassB()'
    print("""    class ClassC(ClassA):
        \\\"""another derived class\\\"""
        h_val  = 8
        def __init__(self):
            ClassA.__init__(self)
            self.i_val  = 9
            self.j_val  = 10
        def __repr__(self):
            return 'ClassC()'
        """)
    class ClassC(ClassA):
        """another derived class"""
        h_val  = 8
        def __init__(self):
            ClassA.__init__(self)
            self.i_val  = 9
            self.j_val  = 10
        def __repr__(self):
            """overloads repr operator"""
            return 'ClassC()'
    print("""    class ClassD(ClassB,ClassC):
        \\\"""multiple inheritance class\\\"""
        k_val  = 11
        def __init__(self):
            ClassB.__init__(self)
            ClassC.__init__(self)
            self.l_val  = 12
            self.m_val  = 13
        def __repr__(self):
            return 'ClassD()'
        """)
    class ClassD(ClassB,ClassC):
        """multiple inheritance class"""
        k_val  = 11
        def __init__(self):
            ClassB.__init__(self)
            ClassC.__init__(self)
            self.l_val  = 12
            self.m_val  = 13
        def __repr__(self):
            """overloads repr operator"""
            return 'ClassD()'
    print('and an instance of ``ClassD``:\n')
    print('>>> obj_d = ClassD()')
    obj_d = ClassD()
    print('\n>>> dir(obj_d)')
    print(dir(obj_d))
    if hasattr(obj_d,'__dict__'):
        print('\n>>> obj_d.__dict__')
        print(obj_d.__dict__)
    if hasattr(obj_d,'__slots__'):
        print('\n>>> obj_d.__slots__')
        print(obj_d.__slots__)
    print('\n>>> obj_d.__class__.__mro__')
    print(obj_d.__class__.__mro__)
    print('\nits attributes are traced by invoking the function ``trace_attributes``:\n')
    print('>>> trace_attributes(obj_d)')
    trace_attributes(obj_d)
    print()
    print('Notice how only the class attributes belong to their '
          'respective classes, and all\nthe other attributes '
          'belong to the instance')
    print('\n.. seealso:: :doc:`Method resolution order (MRO)<feature77>`')
    print(80*'-')
