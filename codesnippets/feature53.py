##    Python codesnippets - Module reload
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
# Feature 53
#

"""
Module reload
=============

:py:mod:`codesnippets.feature53`
--------------------------------

For restoring the attributes of an already imported module, the latter
must be explicitely reloaded.

For example ``module1`` is imported and its attributes printed:

>>> import module1

>>> module1.A_VARIABLE
1
>>> module1.A_LIST
[4, 5, 6]

The following code changes ``module1.A_VARIABLE`` and ``module1.A_LIST`` (a mutable object):

>>> module1.A_VARIABLE = 7

>>> module1.A_LIST[0] = 8
>>> module1.A_LIST
[8, 5, 6]

By reloading ``module1``, its code is rerun:

>>> import importlib
>>> importlib.reload(module1)

The content of ``module1`` attributes has been restored:

>>> module1.A_VARIABLE
1
>>> module1.A_LIST
[4, 5, 6]

.. note:: Notice that if the module itself imports other modules, these are not reloaded!
    If you wish to rerun this example, you need to restart the Python shell.

.. seealso:: :doc:`Side effects when importing modules<feature52>`
"""

import importlib

def feature53():
    """Module reload"""
    print('Module reload')
    print('=============\n')
    print(':py:mod:`codesnippets.feature53`')
    print('--------------------------------\n')
    print('For restoring the attributes of an already imported module, the latter')
    print('must be explicitely reloaded.\n')
    print('For example ``module1`` is imported and its attributes printed:\n')
    print('>>> import module1\n')
    module1 = importlib.import_module('.module1','codesnippets')
    print('>>> module1.A_VARIABLE')
    print(module1.A_VARIABLE)
    print('>>> module1.A_LIST')
    print(module1.A_LIST)
    print("\nThe following code changes ``module1.A_VARIABLE`` and ``module1.A_LIST``"
          " (a mutable object):\n")
    print('>>> module1.A_VARIABLE = 7\n')
    module1.A_VARIABLE = 7
    print('>>> module1.A_LIST[0] = 8')
    module1.A_LIST[0] = 8
    print('>>> module1.A_LIST')
    print(module1.A_LIST)
    print("\nBy reloading ``module1``, its code is rerun:\n")
    print('>>> import importlib')
    print('>>> importlib.reload(module1)\n')
    importlib.reload(module1)
    print("The content of ``module1`` attributes has been restored:\n")
    print('>>> module1.A_VARIABLE')
    print(module1.A_VARIABLE)
    print('>>> module1.A_LIST')
    print(module1.A_LIST)
    print("\n.. note:: Notice that if the module itself imports other modules, "
          "these are not reloaded!\n    If you wish to rerun this example, you need "
          "to restart the Python shell.")
    print('\n.. seealso:: :doc:`Side effects when importing modules<feature52>`')
    print(80*'-')