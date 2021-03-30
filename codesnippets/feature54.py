##    Python codesnippets - Module packages
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
# Feature 54
#

"""
Module packages
===============

:py:mod:`codesnippets.feature54`
--------------------------------

Packages work like modules but the path must be given as well.
A file ``__init__.py`` must be located in all the subdirectories.
This file is loaded and run the very first time a package is included:

>>> import system1.utilities
>>> import system2.utilities

>>> system1.utilities.print_string('Hello')
Hello
>>> system2.utilities.print_string('Hello')
Hello
"""

import codesnippets.system1.utilities
import codesnippets.system2.utilities

def feature54():
    """Module packages"""
    print('Module packages')
    print('===============\n')
    print(':py:mod:`codesnippets.feature54`')
    print('--------------------------------\n')
    print('Packages work like modules but the path must be given as well.')
    print('A file ``__init__.py`` must be located in all the subdirectories.')
    print('This file is loaded and run the very first time a package is included:\n')
    print('>>> import system1.utilities')
    print('>>> import system2.utilities\n')
    print(">>> system1.utilities.print_string('Hello')")
    codesnippets.system1.utilities.print_string('Hello')
    print(">>> system2.utilities.print_string('Hello')")
    codesnippets.system2.utilities.print_string('Hello')
    print(80*'-')