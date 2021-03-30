##    Python codesnippets - Module attribute access
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
# Feature 57
#

"""
Module attribute access
========================

:py:mod:`codesnippets.feature57`
--------------------------------

There are several ways to access module attibutes.

>>> import module1

Via direct module attribute:

>>> module1.A_LIST
[4, 5, 6]

Via module dictionary attribute:

>>> module1.__dict__['A_LIST']
[4, 5, 6]

Via ``sys.modules``:

>>> import sys
>>> sys.modules['module1'].A_LIST
[4, 5, 6]

Via the ``getattr`` built-in function:

>>> getattr(module1, 'A_LIST')
[4, 5, 6]

.. seealso:: :doc:`Module import information<feature50>`
"""

import sys
import module1

def feature57():
    """Module attribute access"""
    print('Module attribute access')
    print('========================\n')
    print(':py:mod:`codesnippets.feature57`')
    print('--------------------------------\n')
    print('There are several ways to access module attibutes.\n')
    print(">>> import module1")
    print('\nVia direct module attribute:\n')
    print(">>> module1.A_LIST")
    print(module1.A_LIST)
    print('\nVia module dictionary attribute:\n')
    print(">>> module1.__dict__['A_LIST']")
    print(module1.__dict__['A_LIST'])
    print('\nVia ``sys.modules``:\n')
    print(">>> import sys")
    print(">>> sys.modules['module1'].A_LIST")
    print(sys.modules['module1'].A_LIST)
    print('\nVia the ``getattr`` built-in function:\n')
    print(">>> getattr(module1, 'A_LIST')")
    print(getattr(module1, 'A_LIST'))
    print('\n.. seealso:: :doc:`Module import information<feature50>`')
    print(80*'-')