##    Python codesnippets - Module import information
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
# Feature 49
#

"""
Module import information
=========================

:py:mod:`codesnippets.feature49`
--------------------------------

The ``sys`` module provides important information concerning for example:

* the path used for searching Python modules,
* the dictonary of imported modules.

>>> import sys

The path used for searching Python modules is given by ``sys.path``:

>>> sys.path
['/Users/miia/Programming/LearningPython/Python_codesnippets',
'/Library/Frameworks/Python.framework/Versions/3.9/bin', '/Users/miia/Programming/LearningPython',
'/Library/Frameworks/Python.framework/Versions/3.9/lib/python39.zip',
'/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9',
'/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/lib-dynload',
'/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages']

The dictionary of imported modules is given by ``sys.modules`` (only 10 items are shown here):

>>> list(sys.modules.items())[:10]
[('sys', <module 'sys' (built-in)>), ('builtins', <module 'builtins' (built-in)>),
('_frozen_importlib', <module 'importlib._bootstrap' (frozen)>),
('_imp', <module '_imp' (built-in)>),
('_thread', <module '_thread' (built-in)>), ('_warnings', <module '_warnings' (built-in)>),
('_weakref', <module '_weakref' (built-in)>),
('_frozen_importlib_external', <module 'importlib._bootstrap_external' (frozen)>),
('posix', <module 'posix' (built-in)>), ('_io', <module 'io' (built-in)>)]

.. seealso:: :doc:`Module attribute access<feature56>`
"""

import sys

def feature49():
    """Module import information"""
    print('Module import information')
    print('=========================\n')
    print(':py:mod:`codesnippets.feature49`')
    print('--------------------------------\n')
    print('The ``sys`` module provides important information concerning for example:\n')
    print('* the path used for searching Python modules,')
    print('* the dictonary of imported modules.\n')
    print('>>> import sys\n')
    print('The path used for searching Python modules is given by ``sys.path``:\n')
    print('>>> sys.path')
    print(sys.path)
    print('\nThe dictionary of imported modules is given by ``sys.modules`` (only 10 items '
          'are shown here):\n')
    print('>>> list(sys.modules.items())[:10]')
    print(list(sys.modules.items())[:10])
    print('\n.. seealso:: :doc:`Module attribute access<feature56>`')
    print(80*'-')
