##    Python codesnippets - Side effects when importing modules
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
# Feature 51
#

"""
Side effects when importing modules
===================================

:py:mod:`codesnippets.feature51`
--------------------------------

Subtle side effects might occur when ``from`` is used:

>>> from module1 import A_VARIABLE,A_LIST

``from`` performs an implicit assignment, but ``A_VARIABLE`` is an immutable type and
it is not shared with ``module1``, whereas ``A_LIST`` is mutable and the
reference is shared with ``module1``:

>>> A_VARIABLE
1
>>> A_LIST
[4, 5, 6]

The following code changes ``A_VARIABLE`` and ``A_LIST`` (a mutable object):

>>> A_VARIABLE = 7

>>> A_LIST[0] = 8
>>> A_LIST
[8, 5, 6]

By importing again the module, the module's code is **not** rerun:

>>> import module1

Here ``module1.A_VARIABLE`` is a different object than ``A_VARIABLE``:

>>> module1.A_VARIABLE
1

But ``module1.A_LIST`` and ``A_LIST`` share the same object and the same
referenced object was changed before!

>>> module1.A_LIST
[8, 5, 6]

.. note:: If you wish to rerun this example, you need to restart the Python shell.

.. seealso:: :doc:`Side effects in assignments<feature18>`
"""

import importlib
from codesnippets.module1 import A_VARIABLE,A_LIST

def feature51():
    """Side effects when importing modules"""
    global A_VARIABLE
    global A_LIST
    print('Side effects when importing modules')
    print('===================================\n')
    print(':py:mod:`codesnippets.feature51`')
    print('--------------------------------\n')
    print("Subtle side effects might occur when ``from`` is used:\n")
    print('>>> from module1 import A_VARIABLE,A_LIST\n')
    print("``from`` performs an implicit assignment, but ``A_VARIABLE`` is an immutable type and\n"
          "it is not shared with ``module1``, whereas ``A_LIST`` is mutable and the"
          "\nreference is shared with ``module1``:\n")
    print('>>> A_VARIABLE')
    print(A_VARIABLE)
    print('>>> A_LIST')
    print(A_LIST)
    print("\nThe following code changes ``A_VARIABLE`` and ``A_LIST`` (a mutable object):\n")
    print('>>> A_VARIABLE = 7\n')
    A_VARIABLE = 7
    print('>>> A_LIST[0] = 8')
    A_LIST[0] = 8
    print('>>> A_LIST')
    print(A_LIST)
    print("\nBy importing again the module, the module's code is **not** rerun:\n")
    print('>>> import module1')
    module1 = importlib.import_module('.module1','codesnippets')
    print("\nHere ``module1.A_VARIABLE`` is a different object than ``A_VARIABLE``:\n")
    print(">>> module1.A_VARIABLE")
    print(module1.A_VARIABLE)
    print("\nBut ``module1.A_LIST`` and ``A_LIST`` share the same object and the same"
          "\nreferenced object was changed before!\n")
    print(">>> module1.A_LIST")
    print(module1.A_LIST)
    print("\n.. note:: If you wish to rerun this example, you need to restart the Python shell.")
    print('\n.. seealso:: :doc:`Side effects in assignments<feature18>`')
    print(80*'-')
