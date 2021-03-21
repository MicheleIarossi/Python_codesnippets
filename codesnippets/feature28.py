##    Python codesnippets - Function definitions
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
# Feature 28
#

"""
Function definitions
====================

:py:mod:`codesnippets.feature28`
--------------------------------

Functions are assigned at runtime when the definition header is run!

The following is valid code:

>>> cond = False

>>> if cond:
        def func():
 	       print('Function for True')
    else:
        def func():
 	       print('Function for False')

>>> func()
Function for False
"""

def feature28():
    """Function definitions"""
    print('Function definitions')
    print('====================\n')
    print(':py:mod:`codesnippets.feature28`')
    print('--------------------------------\n')
    print('Functions are assigned at runtime when the definition header is run!\n')
    print('The following is valid code:\n')
    print('>>> cond = False\n')
    print('>>> if cond:')
    print('        def func():')
    print(" 	       print('Function for True')")
    print('    else:')
    print('        def func():')
    print(" 	       print('Function for False')")
    print('\n>>> func()')
    cond = False
    if cond:
        def func():
            print("Function for True")
    else:
        def func():
            print("Function for False")
    func()
    print(80*'-')
