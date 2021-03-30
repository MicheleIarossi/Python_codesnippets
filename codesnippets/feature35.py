##    Python codesnippets - Factory function with lambda and defaults
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
# Feature 35
#

"""
Factory function with ``lambda`` and defaults
=============================================

:py:mod:`codesnippets.feature35`
--------------------------------

The following function is a factory function that returns a list of power functions:

:math:`f(x) = x^k` where :math:`k=0,1,...,n-1`.

.. code-block:: Python

    def pow_funcs_maker(n_value):
        funcs = []
        for exp_val in range(n_value):
            funcs.append((lambda x_value, pow_val=exp_val: x_value**pow_val))
        return funcs

It uses ``lambda`` function syntax with a default parameter ``exp_value`` that is evaluated
at function definition (not later when the function is called!) and
set equal to the index ``exp_val`` of the loop.

>>> pow_funcs = pow_funcs_maker(3)

>>> pow_funcs[0](2)
1
>>> pow_funcs[1](2)
2
>>> pow_funcs[2](2)
4

Without a default parameter in the ``lambda`` function definitions, when
the power functions are later called, they would all
retain the value of the index variable ``exp_val`` at the end of the loop: all
power functions would be the same!

.. code-block:: Python

    def wrong_pow_funcs_maker(n_value):
        funcs = []
        for exp_val in range(n_value):
            funcs.append((lambda x_value: x_value**exp_val))
        return funcs

>>> pow_funcs = wrong_pow_funcs_maker(3)

>>> pow_funcs[0](2)
4
>>> pow_funcs[1](2)
4
>>> pow_funcs[2](2)
4

.. note:: All the ``lambda`` functions keep a reference to the loop variable ``exp_val``.
    When the functions are later called, due to state retention, they all reference ``exp_val``
    with the last value reached in the loop!

.. seealso:: :doc:`Lambda functions<feature46>`
"""

def pow_funcs_maker(n_value):
    """returns a list of power functions"""
    funcs = []
    for exp_val in range(n_value):
        funcs.append((lambda x_value,pow_val=exp_val: x_value**pow_val))
    return funcs

def wrong_pow_funcs_maker(n_value):
    """returns a list of power functions (wrong version)"""
    funcs = []
    for exp_val in range(n_value):
        funcs.append((lambda x_value: x_value**exp_val))
    return funcs

def feature35():
    """Factory function with lambda and defaults"""
    print('Factory function with ``lambda`` and defaults')
    print('=============================================\n')
    print(':py:mod:`codesnippets.feature35`')
    print('--------------------------------\n')
    print('The following function is a factory function that returns a list of power functions:\n')
    print(':math:`f(x) = x^k` where :math:`k=0,1,...,n-1`.\n')
    print('.. code-block:: Python\n')
    print('    def pow_funcs_maker(n_value):')
    print('        funcs = []')
    print('        for exp_val in range(n_value):')
    print('            funcs.append((lambda x_value, pow_val=exp_val: x_value**pow_val))')
    print('        return funcs\n')
    print('It uses ``lambda`` function syntax with a default parameter ``exp_value``'
          'that is evaluated')
    print('at function definition (not later when the function is called!) and')
    print('set equal to the index ``exp_val`` of the loop.\n')
    print('>>> pow_funcs = pow_funcs_maker(3)\n')
    pow_funcs = pow_funcs_maker(3)
    print('>>> pow_funcs[0](2)')
    print(pow_funcs[0](2))
    print('>>> pow_funcs[1](2)')
    print(pow_funcs[1](2))
    print('>>> pow_funcs[2](2)')
    print(pow_funcs[2](2))
    print('\nWithout a default parameter in the ``lambda`` function definitions, when')
    print('the power functions are later called, they would all')
    print('retain the value of the index variable ``exp_val`` at the end of the loop: all')
    print('power functions would be the same!\n')
    print('.. code-block:: Python\n')
    print('    def wrong_pow_funcs_maker(n_value):')
    print('        funcs = []')
    print('        for exp_val in range(n_value):')
    print('            funcs.append((lambda x_value: x_value**exp_val))')
    print('        return funcs\n')
    print('>>> pow_funcs = wrong_pow_funcs_maker(3)\n')
    pow_funcs = wrong_pow_funcs_maker(3)
    print('>>> pow_funcs[0](2)')
    print(pow_funcs[0](2))
    print('>>> pow_funcs[1](2)')
    print(pow_funcs[1](2))
    print('>>> pow_funcs[2](2)')
    print(pow_funcs[2](2))
    print('\n.. note:: All the ``lambda`` functions keep a reference to the loop variable'
          ' ``exp_val``.\n    When the functions are later called, due to state retention, '
          'they all reference ``exp_val``\n    with the last value reached in the loop!\n')
    print('.. seealso:: :doc:`Lambda functions<feature46>`')
    print(80*'-')