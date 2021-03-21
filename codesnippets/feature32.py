##    Python codesnippets - Factory function (state retention)
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
# Feature 32
#

"""
Factory function (state retention)
==================================

:py:mod:`codesnippets.feature32`
--------------------------------

The following function is a factory function which remembers the value
of the input parameter ``n_value`` provided:

.. code-block:: Python

    def pow_func_maker(n_value):
        def pow_x_to_n(x_value):
            return x_value**n_value
        return pow_x_to_n

Given the parameter ``n`` it returns the power function :math:`f(x) = x^n`

>>> square = pow_func_maker(2)
>>> cube   = pow_func_maker(3)

>>> square(4)
16

>>> cube(5)
125
"""

def pow_func_maker(n_value):
    """returns a power function"""
    def pow_x_to_n(x_value):
        """power function"""
        return x_value**n_value
    return pow_x_to_n

def feature32():
    """Factory function (state retention)"""
    print('Factory function (state retention)')
    print('==================================\n')
    print(':py:mod:`codesnippets.feature32`')
    print('--------------------------------\n')
    print('The following function is a factory function which remembers the value')
    print('of the input parameter ``n_value`` provided:\n')
    print('.. code-block:: Python\n')
    print('    def pow_func_maker(n_value):')
    print('        def pow_x_to_n(x_value):')
    print('            return x_value**n_value')
    print('        return pow_x_to_n\n')
    print('Given the parameter ``n`` it returns the power function :math:`f(x) = x^n`\n')
    print('>>> square = pow_func_maker(2)')
    print('>>> cube   = pow_func_maker(3)\n')
    square = pow_func_maker(2)
    cube   = pow_func_maker(3)
    print('>>> square(4)')
    print(square(4))
    print('\n>>> cube(5)')
    print(cube(5))
    print(80*'-')
