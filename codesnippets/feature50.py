##    Python codesnippets - Module import
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
# Feature 50
#

"""
Module import
=============

:py:mod:`codesnippets.feature50`
--------------------------------

When an ``import`` statement is run, the module is compiled and the module code is run:

>>> import module1

A module object is created:

>>> module1
<module 'codesnippets.module1'
from '/Users/miia/Programming/LearningPython/Python_codesnippets/codesnippets/module1.py'>

Its global variables become its attributes:

>>> module1.A_VARIABLE
1

The attributes can be changed:

>>> module1.A_VARIABLE = 2
>>> module1.A_VARIABLE
2

But when an ``import`` statement is rerun, the module is NOT imported again:

>>> import module1

The attribute ``A_VARIABLE`` is unchanged, the module code has not been rerun!

>>> module1.A_VARIABLE
2

Module namespaces are stored internally as dictionary objects, e.g. ``module1.__dict__`` :

>>> list(name for name in module1.__dict__ if not name.startswith('__'))
['a_function', 'A_VARIABLE', 'A_LIST']

>>> dir(module1)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__',
'__package__', '__spec__', 'a_function', 'A_VARIABLE', 'A_LIST']

.. note:: If you wish to rerun this example, you need to restart the Python shell.

.. seealso:: :doc:`dir() on an integer variable<feature1>`
"""

import importlib

def feature50():
    """Module import"""
    print('Module import')
    print('=============\n')
    print(':py:mod:`codesnippets.feature50`')
    print('--------------------------------\n')
    print("When an ``import`` statement is run, the module is compiled and the module "
          "code is run:\n")
    print('>>> import module1')
    module1 = importlib.import_module('.module1','codesnippets')
    print("\nA module object is created:\n")
    print('>>> module1')
    print(module1)
    print("\nIts global variables become its attributes:\n")
    print('>>> module1.A_VARIABLE')
    print(module1.A_VARIABLE)
    print("\nThe attributes can be changed:\n")
    print(">>> module1.A_VARIABLE = 2")
    module1.A_VARIABLE = 2
    print('>>> module1.A_VARIABLE')
    print(module1.A_VARIABLE)
    print("\nBut when an ``import`` statement is rerun, the module is NOT imported again:\n")
    print('>>> import module1')
    module1 = importlib.import_module('.module1','codesnippets')
    print("\nThe attribute ``A_VARIABLE`` is unchanged, the module code has not been rerun!\n")
    print(">>> module1.A_VARIABLE")
    print(module1.A_VARIABLE)
    print("\nModule namespaces are stored internally as dictionary "
          "objects, e.g. ``module1.__dict__`` :\n")
    print(">>> list(name for name in module1.__dict__ if not name.startswith('__'))")
    print(list(name for name in module1.__dict__ if not name.startswith('__')))
    print("\n>>> dir(module1)")
    print(dir(module1))
    print("\n.. note:: If you wish to rerun this example, you need to restart the Python shell.")
    print('\n.. seealso:: :doc:`dir() on an integer variable<feature1>`')
    print(80*'-')
