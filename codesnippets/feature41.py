##    Python codesnippets - Unpacking arguments
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
Unpacking arguments
===================

:py:mod:`codesnippets.feature41`
--------------------------------

The ``*`` unpacks a tuple into positional arguments.\n
The ``**`` unpacks a dictionary into an arbitrary number of keyword arguments.

.. code-block:: Python

    def func(*pargs,a_value=0,**kwargs):
        print(f'Arbitrary positional arguments: pargs   = {pargs}')
        print(f'Positional parameter:           a_value = {a_value}')
        print(f'Arbitrary keyword arguments:    kwargs  = {kwargs}')

>>> func(*(3,4,5),2,**{'alfa':3,'beta':5,'gamma':10})
Arbitrary positional arguments: pargs   = (3, 4, 5, 2)
Positional parameter:           a_value = 0
Arbitrary keyword arguments:    kwargs  = {'alfa': 3, 'beta': 5, 'gamma': 10}
"""

def func(*pargs,a_value=0,**kwargs):
    """uses positional, arbitrary positional and keyword arguments"""
    print(f'Arbitrary positional arguments: pargs   = {pargs}')
    print(f'Positional parameter:           a_value = {a_value}')
    print(f'Arbitrary keyword arguments:    kwargs  = {kwargs}')

def feature41():
    """Unpacking arguments"""
    print('Unpacking arguments')
    print('===================\n')
    print(':py:mod:`codesnippets.feature41`')
    print('--------------------------------\n')
    print('The ``*`` unpacks a tuple into positional arguments.\\n')
    print('The ``**`` unpacks a dictionary into an arbitrary number of keyword arguments.\n')
    print('.. code-block:: Python\n')
    print('    def func(*pargs,a_value=0,**kwargs):')
    print("        print(f'Arbitrary positional arguments: pargs   = {pargs}')")
    print("        print(f'Positional parameter:           a_value = {a_value}')")
    print("        print(f'Arbitrary keyword arguments:    kwargs  = {kwargs}')\n")
    print(">>> func(*(3,4,5),2,**{'alfa':3,'beta':5,'gamma':10})")
    func(*(3,4,5),2,**{'alfa':3,'beta':5,'gamma':10})
    print(80*'-')