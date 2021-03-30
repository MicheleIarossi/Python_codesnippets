##    Python codesnippets - Function generators
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
# Feature 48
#

"""
Function generators
===================

:py:mod:`codesnippets.feature48`
--------------------------------

A function generator returns results one at a time:

.. code-block:: Python

    def func_gen_numbers(n_value):
        for a_value in range(n_value):
           yield a_value

>>> g_func = func_gen_numbers(5)

A function generator is its own iterator:

>>> iter(g_func) is g_func
True

By calling ``next()`` it provides results one at a time:


>>> next(g_func)
0
>>> next(g_func)
1
>>> next(g_func)
2
>>> next(g_func)
3

Assignment unpacking can be used as well:

>>> first, second, *rest = func_gen_numbers(7)

>>> first, second, rest
(0, 1, [2, 3, 4, 5, 6])

.. seealso:: :doc:`The iteration protocol<feature27>`, :doc:`More assignment unpacking<feature16>`
"""

def func_gen_numbers(n_value):
    """function generator"""
    for a_value in range(n_value):
        yield a_value


def feature48():
    """Function generators"""
    print('Function generators')
    print('===================\n')
    print(':py:mod:`codesnippets.feature48`')
    print('--------------------------------\n')
    print('A function generator returns results one at a time:\n')
    print('.. code-block:: Python\n')
    print('    def func_gen_numbers(n_value):')
    print('        for a_value in range(n_value):')
    print('           yield a_value\n')
    print('>>> g_func = func_gen_numbers(5)\n')
    g_func = func_gen_numbers(5)
    print('A function generator is its own iterator:\n')
    print('>>> iter(g_func) is g_func')
    print(iter(g_func) is g_func)
    print('\nBy calling ``next()`` it provides results one at a time:\n')
    print('\n>>> next(g_func)')
    print(next(g_func))
    print('>>> next(g_func)')
    print(next(g_func))
    print('>>> next(g_func)')
    print(next(g_func))
    print('>>> next(g_func)')
    print(next(g_func))
    print("\nAssignment unpacking can be used as well:\n")
    first, second, *rest = func_gen_numbers(7)
    print('>>> first, second, *rest = func_gen_numbers(7)\n')
    print('>>> first, second, rest')
    print((first, second, rest))
    print('\n.. seealso:: :doc:`The iteration protocol<feature27>`, '
          ':doc:`More assignment unpacking<feature16>`')
    print(80*'-')