##    Python codesnippets - Class interface techniques
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
Class interface techniques
==========================

:py:mod:`codesnippets.feature64`
--------------------------------

There are different inheritance patterns available for adding new features to derived classes:

* Inheritor,
* Replacer,
* Extender,
* Provider.

Given the following base class:

.. code-block:: Python

    class Super:
        \"""a base class\"""
        def method(self):
            \"""a default method\"""
            print(f'	-> In Super.method')           # Default behavior
        def delegate(self):
            \"""another method\"""
            self.action()                      # Expected to be defined

This is the default behaviour of the base class above:

>>> sup = Super()
>>> sup.method()
	-> In Super.method

The ``Inheritor`` just derives the methods from the base class as they are:

.. code-block:: Python

>>> class Inheritor(Super):                    # Inherit method verbatim
        \"""a derived class\"""
        pass

The behaviour is the same as the ``Super`` class:

>>> inh = Inheritor()
>>> inh.method()
	-> In Super.method

The ``Replacer`` redefines methods from the base class:

.. code-block:: Python

    class Replacer(Super):                     # Replace method completely
        \"""derived class replacing a method\"""
        def method(self):
            \"""new method\"""
            print(f'	-> In Replacer.method')

The ``method`` call is completely replaced by ``Replacer``:

>>> rep = Replacer()
>>> rep.method()
	-> In Replacer.method

The ``Extender`` extends methods from the base class:

.. code-block:: Python

    class Extender(Super):                     # Extend method behavior
        \"""extends the base class\"""
        def method(self):
            \"""extends base method function\"""
            print(f'	-> Starting Extender.method')
            Super.method(self)
            print(f'	-> Ending Extender.method')

The ``method`` call references ``Super.method()`` and extends it:

>>> ext = Extender()
>>> ext.method()
	-> Starting Extender.method
	-> In Super.method
	-> Ending Extender.method

Finally, the ``Provider`` provides the missing method in the base class:

.. code-block:: Python

    class Provider(Super):                     # Fill in a required method
        \"""provides missing method in the base class\"""
        def action(self):
            \"""missing method\"""
            print(f'	-> In Provider.action')

The method ``Super.delegate()`` needs an ``action()`` method provided by the ``Provider`` class:

>>> pro = Provider()
>>> pro.delegate()
	-> In Provider.action
"""

def feature64():
    """Class interface techniques"""
    print('Class interface techniques')
    print('==========================\n')
    print(':py:mod:`codesnippets.feature64`')
    print('--------------------------------\n')
    print('There are different inheritance patterns available for adding new'
          ' features to derived classes:\n')
    print('* Inheritor,')
    print('* Replacer,')
    print('* Extender,')
    print('* Provider.\n')
    print('Given the following base class:\n')
    print('.. code-block:: Python\n')
    print("""    class Super:
        \\\"""a base class\\\"""
        def method(self):
            \\\"""a default method\\\"""
            print(f'\t-> In Super.method')           # Default behavior
        def delegate(self):
            \\\"""another method\\\"""
            self.action()                      # Expected to be defined
        """)
    class Super:
        """a base class"""
        def method(self):
            """a default method"""
            print(f'\t-> In Super.method')           # Default behavior
        def delegate(self):
            """another method"""
            self.action()                      # Expected to be defined
    print('This is the default behaviour of the base class above:\n')
    print(">>> sup = Super()")
    sup = Super()
    print(">>> sup.method()")
    sup.method()
    print('\nThe ``Inheritor`` just derives the methods from the base class as they are:\n')
    print('.. code-block:: Python\n')
    print(""">>> class Inheritor(Super):                    # Inherit method verbatim
        \\\"""a derived class\\\"""
        pass
        """)
    class Inheritor(Super):                    # Inherit method verbatim
        """a derived class"""
        pass
    print('The behaviour is the same as the ``Super`` class:\n')
    print(">>> inh = Inheritor()")
    inh = Inheritor()
    print(">>> inh.method()")
    inh.method()
    print('\nThe ``Replacer`` redefines methods from the base class:\n')
    print('.. code-block:: Python\n')
    print("""    class Replacer(Super):                     # Replace method completely
        \\\"""derived class replacing a method\\\"""
        def method(self):
            \\\"""new method\\\"""
            print(f'\t-> In Replacer.method')
        """)

    class Replacer(Super):                     # Replace method completely
        """derived class replacing a method"""
        def method(self):
            """new method"""
            print(f'\t-> In Replacer.method')
    print('The ``method`` call is completely replaced by ``Replacer``:\n')
    print(">>> rep = Replacer()")
    rep = Replacer()
    print(">>> rep.method()")
    rep.method()
    print('\nThe ``Extender`` extends methods from the base class:\n')
    print('.. code-block:: Python\n')
    print("""    class Extender(Super):                     # Extend method behavior
        \\\"""extends the base class\\\"""
        def method(self):
            \\\"""extends base method function\\\"""
            print(f'\t-> Starting Extender.method')
            Super.method(self)
            print(f'\t-> Ending Extender.method')
        """)
    class Extender(Super):                     # Extend method behavior
        """extends the base class"""
        def method(self):
            """extends base method function"""
            print(f'\t-> Starting Extender.method')
            Super.method(self)
            print(f'\t-> Ending Extender.method')
    print('The ``method`` call references ``Super.method()`` and extends it:\n')
    print(">>> ext = Extender()")
    ext = Extender()
    print(">>> ext.method()")
    ext.method()
    print('\nFinally, the ``Provider`` provides the missing method in the base class:\n')
    print('.. code-block:: Python\n')
    print("""    class Provider(Super):                     # Fill in a required method
        \\\"""provides missing method in the base class\\\"""
        def action(self):
            \\\"""missing method\\\"""
            print(f'\t-> In Provider.action')
        """)
    class Provider(Super):                     # Fill in a required method
        """provides missing method in the base class"""
        def action(self):
            """missing method"""
            print(f'\t-> In Provider.action')
    print('The method ``Super.delegate()`` needs an ``action()`` method '
          'provided by the ``Provider`` class:\n')
    print(">>> pro = Provider()")
    pro = Provider()
    print(">>> pro.delegate()")
    pro.delegate()
    print(80*'-')