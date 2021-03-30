##    Python codesnippets - Module imports with importlib
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
# Feature 58
#

"""
Module imports with ``importlib``
=================================

:py:mod:`codesnippets.feature58`
--------------------------------

The library ``importlib`` lets us import modules via its function ``import_module``:

>>> import importlib

>>> modname = 'module1'

>>> module1 = importlib.import_module(modname)

>>> module1.A_LIST
[4, 5, 6]
"""

import importlib

def feature58():
    """Module imports with importlib"""
    print('Module imports with ``importlib``')
    print('=================================\n')
    print(':py:mod:`codesnippets.feature58`')
    print('--------------------------------\n')
    print('The library ``importlib`` lets us import modules via its function ``import_module``:\n')
    print(">>> import importlib\n")
    print(">>> modname = 'module1'\n")
    modname = 'module1'
    print(">>> module1 = importlib.import_module(modname)\n")
    module1 = importlib.import_module(modname)
    print(">>> module1.A_LIST")
    print(module1.A_LIST)
    print(80*'-')