##    Python codesnippets - Expression generators
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
Expression generators
=====================

:py:mod:`codesnippets.feature49`
--------------------------------

An expression generator returns results one at a time.
It must be coded inside parentheses:

>>> g_expr = (x_var**2 for x_var in range(5))

An expression generator is its own iterator:

>>> iter(g_expr) is g_expr
True

By calling ``next()`` it provides results one at a time:

>>> next(g_expr)
0
>>> next(g_expr)
1
>>> next(g_expr)
4
>>> next(g_expr)
9

.. seealso:: :doc:`The iteration protocol<feature27>`
"""

def feature49():
    """Expression generators"""
    print('Expression generators')
    print('=====================\n')
    print(':py:mod:`codesnippets.feature49`')
    print('--------------------------------\n')
    print('An expression generator returns results one at a time.')
    print('It must be coded inside parentheses:\n')
    print('>>> g_expr = (x_var**2 for x_var in range(5))')
    g_expr = (x_var**2 for x_var in range(5))
    print('\nAn expression generator is its own iterator:\n')
    print('>>> iter(g_expr) is g_expr')
    print(iter(g_expr) is g_expr)
    print('\nBy calling ``next()`` it provides results one at a time:\n')
    print('>>> next(g_expr)')
    print(next(g_expr))
    print('>>> next(g_expr)')
    print(next(g_expr))
    print('>>> next(g_expr)')
    print(next(g_expr))
    print('>>> next(g_expr)')
    print(next(g_expr))
    print('\n.. seealso:: :doc:`The iteration protocol<feature27>`')
    print(80*'-')