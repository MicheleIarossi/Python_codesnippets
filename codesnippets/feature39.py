##    Python codesnippets - Arbitrary arguments
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
# Feature 39
#

"""
Arbitrary arguments
===================

:py:mod:`codesnippets.feature39`
--------------------------------

The ``*`` collects an arbitrary number of positional arguments into a tuple.\n
The ``**`` collects an arbitrary number of keyword arguments into a dictionary.

.. code-block:: Python

    def func(*pargs,a_value=0,**kwargs):
        print(f'Arbitrary positional arguments: pargs   = {pargs}')
        print(f'Positional parameter:           a_value = {a_value}')
        print(f'Arbitrary keyword arguments:    kwargs  = {kwargs}')

>>> func(2,3,4,5,alfa=3,beta=5,gamma=10)
Arbitrary positional arguments: pargs   = (2, 3, 4, 5)
Positional parameter:           a_value = 0
Arbitrary keyword arguments:    kwargs  = {'alfa': 3, 'beta': 5, 'gamma': 10}

>>> func(3,4,5,alfa=3,beta=5,gamma=10)
Arbitrary positional arguments: pargs   = (3, 4, 5)
Positional parameter:           a_value = 0
Arbitrary keyword arguments:    kwargs  = {'alfa': 3, 'beta': 5, 'gamma': 10}

>>> func(4,alfa=3,beta=5,gamma=10)
Arbitrary positional arguments: pargs   = (4,)
Positional parameter:           a_value = 0
Arbitrary keyword arguments:    kwargs  = {'alfa': 3, 'beta': 5, 'gamma': 10}

>>> func(alfa=3,beta=5,gamma=10)
Arbitrary positional arguments: pargs   = ()
Positional parameter:           a_value = 0
Arbitrary keyword arguments:    kwargs  = {'alfa': 3, 'beta': 5, 'gamma': 10}
"""

def func(*pargs,a_value=0,**kwargs):
    """uses positional, arbitrary positional and keyword arguments"""
    print(f'Arbitrary positional arguments: pargs   = {pargs}')
    print(f'Positional parameter:           a_value = {a_value}')
    print(f'Arbitrary keyword arguments:    kwargs  = {kwargs}')

def feature39():
    """Arbitrary arguments"""
    print('Arbitrary arguments')
    print('===================\n')
    print(':py:mod:`codesnippets.feature39`')
    print('--------------------------------\n')
    print('The ``*`` collects an arbitrary number of positional arguments into a tuple.\\n')
    print('The ``**`` collects an arbitrary number of keyword arguments into a dictionary.\n')
    print('.. code-block:: Python\n')
    print('    def func(*pargs,a_value=0,**kwargs):')
    print("        print(f'Arbitrary positional arguments: pargs   = {pargs}')")
    print("        print(f'Positional parameter:           a_value = {a_value}')")
    print("        print(f'Arbitrary keyword arguments:    kwargs  = {kwargs}')\n")
    print(">>> func(2,3,4,5,alfa=3,beta=5,gamma=10)")
    func(2,3,4,5,alfa=3,beta=5,gamma=10)
    print("\n>>> func(3,4,5,alfa=3,beta=5,gamma=10)")
    func(3,4,5,alfa=3,beta=5,gamma=10)
    print("\n>>> func(4,alfa=3,beta=5,gamma=10)")
    func(4,alfa=3,beta=5,gamma=10)
    print("\n>>> func(alfa=3,beta=5,gamma=10)")
    func(alfa=3,beta=5,gamma=10)
    print(80*'-')
