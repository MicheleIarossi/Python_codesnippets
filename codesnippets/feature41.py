##    Python codesnippets - Keyword only arguments
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
# Feature 41
#

"""
Keyword only arguments
======================

:py:mod:`codesnippets.feature41`
--------------------------------

Keyword only arguments are used for providing optional configuration
parameters. They must be coded after ``*pargs`` and before ``**kwargs``!

.. code-block:: Python

    def func(*pargs,a_value=1,b_value=2,**kwargs):
        print(f'Arbitrary positional arguments: pargs   = {pargs}')
        print(f'Positional parameter:           a_value = {a_value}')
        print(f'Positional parameter:           b_value = {b_value}')
        print(f'Arbitrary keyword arguments:    kwargs  = {kwargs}')

Here the arguments ``a_value`` and ``b_value`` get their default values:

>>> func(*(3,4,5),**{'alfa':3,'beta':5,'gamma':10})
Arbitrary positional arguments: pargs   = (3, 4, 5)
Positional parameter:           a_value = 1
Positional parameter:           b_value = 2
Arbitrary keyword arguments:    kwargs  = {'alfa': 3, 'beta': 5, 'gamma': 10}

Here the arguments ``a_value`` and ``b_value`` are given as keyword arguments:

>>> func(*(3,4,5),a_value=5,b_value=6,**{'alfa':3,'beta':5,'gamma':10})
Arbitrary positional arguments: pargs   = (3, 4, 5)
Positional parameter:           a_value = 5
Positional parameter:           b_value = 6
Arbitrary keyword arguments:    kwargs  = {'alfa': 3, 'beta': 5, 'gamma': 10}
"""

def func(*pargs,a_value=1,b_value=2,**kwargs):
    """uses positional, arbitrary positional and keyword arguments"""
    print(f'Arbitrary positional arguments: pargs   = {pargs}')
    print(f'Positional parameter:           a_value = {a_value}')
    print(f'Positional parameter:           b_value = {b_value}')
    print(f'Arbitrary keyword arguments:    kwargs  = {kwargs}')

def feature41():
    """Keyword only arguments"""
    print('Keyword only arguments')
    print('======================\n')
    print(':py:mod:`codesnippets.feature41`')
    print('--------------------------------\n')
    print('Keyword only arguments are used for providing optional configuration')
    print('parameters. They must be coded after ``*pargs`` and before ``**kwargs``!\n')
    print('.. code-block:: Python\n')
    print('    def func(*pargs,a_value=1,b_value=2,**kwargs):')
    print("        print(f'Arbitrary positional arguments: pargs   = {pargs}')")
    print("        print(f'Positional parameter:           a_value = {a_value}')")
    print("        print(f'Positional parameter:           b_value = {b_value}')")
    print("        print(f'Arbitrary keyword arguments:    kwargs  = {kwargs}')\n")
    print("Here the arguments ``a_value`` and ``b_value`` get their default values:\n")
    print(">>> func(*(3,4,5),**{'alfa':3,'beta':5,'gamma':10})")
    func(*(3,4,5),**{'alfa':3,'beta':5,'gamma':10})
    print("\nHere the arguments ``a_value`` and ``b_value`` are given as keyword arguments:\n")
    print(">>> func(*(3,4,5),a_value=5,b_value=6,**{'alfa':3,'beta':5,'gamma':10})")
    func(*(3,4,5),a_value=5,b_value=6,**{'alfa':3,'beta':5,'gamma':10})
    print(80*'-')
