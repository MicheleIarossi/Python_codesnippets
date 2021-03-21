##    Python codesnippets - lambda functions
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
# Feature 45
#

"""
``lambda`` functions
====================

:py:mod:`codesnippets.feature45`
--------------------------------

``lambda`` functions return a value which is a function.
They are limited to one line expression and should be used only
for coding simple expressions or logic.
Default arguments can also be used.

.. note:: ``lambda`` functions are expressions and not statements like ``def``.

>>> func = lambda alpha=1,beta=1,gamma=1: alpha+beta+gamma
>>> func(3,4,5)
12
>>> func()
3

if-then-else logic can also be coded:

>>> lower = lambda alpha,beta : alpha if alpha>beta else beta
>>> lower('aa','bb')
bb
>>> lower('bb','aa')
bb

Loops can be coded by means of list comprehension:

>>> printall = lambda s_str: [print(sigma) for sigma in s_str]
>>> printall(['Hello','Pippo','Bye']
Hello
Pippo
Bye

``lambda`` can be nested as well and the same scope rules apply:

>>> (lambda alpha: (lambda beta: alpha+beta))(99)(4)
103
"""

def feature45():
    """Lambda functions"""
    print('``Lambda functions``')
    print('====================\n')
    print(':py:mod:`codesnippets.feature45`')
    print('--------------------------------\n')
    print('``lambda`` functions return a value which is a function.')
    print('They are limited to one line expression and should be used only')
    print('for coding simple expressions or logic.')
    print('Default arguments can also be used.\n')
    print('.. note:: ``lambda`` functions are expressions and not statements like ``def``.\n')
    print('>>> func = lambda alpha=1,beta=1,gamma=1: alpha+beta+gamma')
    func = lambda alpha=1,beta=1,gamma=1: alpha+beta+gamma
    print('>>> func(3,4,5)')
    print(func(3,4,5))
    print('>>> func()')
    print(func())
    print('\nif-then-else logic can also be coded:\n')
    print('>>> lower = lambda alpha,beta : alpha if alpha>beta else beta')
    lower = lambda alpha,beta : alpha if alpha>beta else beta
    print(">>> lower('aa','bb')")
    print(lower('aa','bb'))
    print(">>> lower('bb','aa')")
    print(lower('bb','aa'))
    print('\nLoops can be coded by means of list comprehension:\n')
    print('>>> printall = lambda s_str: [print(sigma) for sigma in s_str]')
    printall = lambda s_str: [print(sigma) for sigma in s_str]
    print(">>> printall(['Hello','Pippo','Bye']")
    printall(['Hello','Pippo','Bye'])
    print('\n``lambda`` s can be nested as well and the same scope rules apply:\n')
    print('>>> (lambda alpha: (lambda beta: alpha+beta))(99)(4)')
    print((lambda alpha: (lambda beta: alpha+beta))(99)(4))
    print(80*'-')
