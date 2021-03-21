##    Python codesnippets - Factory function with lambda
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
# Feature 33
#

"""
Factory function with ``lambda``
================================

:py:mod:`codesnippets.feature33`
--------------------------------

This is the same feature as the previous one but it uses ``lambda`` functions:

.. code-block:: Python

    def pow_func_maker(n_value):
        return (lambda alpha: alpha**n_value)

The results are the same:

>>> square = pow_func_maker(2)
>>> cube   = pow_func_maker(3)

>>> square(4)
16

>>> cube(5)
125

.. seealso:: :doc:`Factory function (state retention)<feature32>`,
	:doc:`Lambda functions<feature45>`
"""

def pow_func_maker(n_value):
    """returns a power function with lambda"""
    return lambda alpha: alpha**n_value

def feature33():
    """Factory function with lambda"""
    print('Factory function with ``lambda``')
    print('================================\n')
    print(':py:mod:`codesnippets.feature33`')
    print('--------------------------------\n')
    print('This is the same feature as the previous one but it uses ``lambda`` functions:\n')
    print('.. code-block:: Python\n')
    print('    def pow_func_maker(n_value):')
    print('        return (lambda alpha: alpha**n_value)\n')
    print('The results are the same:\n')
    print('>>> square = pow_func_maker(2)')
    print('>>> cube   = pow_func_maker(3)\n')
    square = pow_func_maker(2)
    cube   = pow_func_maker(3)
    print('>>> square(4)')
    print(square(4))
    print("\n>>> cube(5)")
    print(cube(5))
    print('\n.. seealso:: :doc:`Factory function (state retention)<feature32>`,'
          '\n\t:doc:`Lambda functions<feature45>`')
    print(80*'-')
