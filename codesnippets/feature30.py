##    Python codesnippets - Accessing global variables
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
# Feature 30
#

"""
Accessing global variables
==========================

:py:mod:`codesnippets.feature30`
--------------------------------

There are 3 possibilities:

#. via ``global`` declaration,
#. via attribute and module import,
#. via attribute and module object.

The following code has to run inside a file: ::

    import sys\n
    global_counter = 321\n
    def func_only_reads():
        \"""only reads the global counter\"""
        # Read access possible: LEGB rule applies!
        local_counter = global_counter\n
    def func_writes():
        \"""writes the global counter\"""
        # Required for write access
        global global_counter
        global_counter += 1
        # global can even create a new global variable
        global new_global_counter
        new_global_counter = 2\n
    def func_import():
        \"""accesses the global counter as an attribute of the module\"""
        import codesnippets.feature30
        # Access as attribute of the module
        codesnippets.feature30.global_counter = 350\n
    def func_mod_obj():
        \"""accesses the global counter via the 'sys.modules' dictionary\"""
        modobj = sys.modules['codesnippets.feature30']
        # Access as attribute of a module object
        modobj.global_counter = 370

Global scope gives read access:

>>> func_only_reads()
>>> global_counter
321

``global`` declaration needed for write access:

>>> func_writes()
>>> global_counter
322

Access as attribute of an imported module:

>>> func_import()
>>> global_counter
350

Access as attribute of a module object:

>>> func_mod_obj()
>>> global_counter
370

.. note:: ``func_writes()`` creates a new global variable via the ``global`` declaration:

>>> NEW_global_counter
2

.. seealso:: :doc:`The LEGB rule (nested scopes) <feature31>`
"""

import sys

global_counter = 321
def func_only_reads():
    """only reads the global counter"""
    # Read access possible: LEGB rule applies!
    local_counter = global_counter
def func_writes():
    """writes the global counter"""
    # Required for write access
    global global_counter
    global_counter += 1
    # global can even create a new global variable
    global new_global_counter
    new_global_counter = 2
def func_import():
    """accesses the global counter as an attribute of the module"""
    import codesnippets.feature30
    # Access as attribute of the module
    codesnippets.feature30.global_counter = 350
def func_mod_obj():
    """accesses the global counter via the 'sys.modules' dictionary"""
    modobj = sys.modules['codesnippets.feature30']
    # Access as attribute of a module object
    modobj.global_counter = 370

def feature30():
    """Accessing global variables"""
    print('Accessing global variables')
    print('==========================\n')
    print(':py:mod:`codesnippets.feature30`')
    print('--------------------------------\n')
    print('There are 3 possibilities:\n')
    print('#. via ``global`` declaration,')
    print('#. via attribute and module import,')
    print('#. via attribute and module object.\n')
    print('The following code has to run inside a file: ::\n')
    print('    import sys\\n')
    print('    global_counter = 321\\n')
    print('    def func_only_reads():')
    print("        \\\"\"\"only reads the global counter\\\"\"\"")
    print('        # Read access possible: LEGB rule applies!')
    print('        local_counter = global_counter\\n')
    print('    def func_writes():')
    print("        \\\"\"\"writes the global counter\\\"\"\"")
    print('        # Required for write access')
    print('        global global_counter')
    print('        global_counter += 1')
    print('        # global can even create a new global variable')
    print('        global new_global_counter')
    print('        new_global_counter = 2\\n')
    print('    def func_import():')
    print("        \\\"\"\"accesses the global counter as an attribute of the module\\\"\"\"")
    print('        import codesnippets.feature30')
    print('        # Access as attribute of the module')
    print('        codesnippets.feature30.global_counter = 350\\n')
    print('    def func_mod_obj():')
    print("        \\\"\"\"accesses the global counter via the 'sys.modules' dictionary\\\"\"\"")
    print("        modobj = sys.modules['codesnippets.feature30']")
    print('        # Access as attribute of a module object')
    print('        modobj.global_counter = 370')
    print('\nGlobal scope gives read access:\n')
    print('>>> func_only_reads()')
    print('>>> global_counter')
    func_only_reads()
    print(global_counter)
    print('\n``global`` declaration needed for write access:\n')
    print('>>> func_writes()')
    func_writes()
    print('>>> global_counter')
    print(global_counter)
    print('\nAccess as attribute of an imported module:\n')
    print('>>> func_import()')
    func_import()
    print('>>> global_counter')
    print(global_counter)
    print('\nAccess as attribute of a module object:\n')
    print('>>> func_mod_obj()')
    func_mod_obj()
    print('>>> global_counter')
    print(global_counter)
    print("\n.. note:: ``func_writes()`` creates a new global variable via the ``global`` "
          "declaration:\n")
    print('>>> new_global_counter')
    print(new_global_counter)
    print('\n.. seealso:: :doc:`The LEGB rule (nested scopes) <feature31>`')
    print(80*'-')