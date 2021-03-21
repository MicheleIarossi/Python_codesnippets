##    Python codesnippets - State retention using mutable list
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
# Feature 36
#

"""
State retention using mutable list
==================================

:py:mod:`codesnippets.feature36`
--------------------------------

The function below calls methods of a ``list`` to perform in-place changes.

.. note:: In-place object changes do not classify as local.

.. code-block:: Python

    def func_factory(start):
        def nested_func(label):
            print(label, state[0])
            # hack: in-place object changes do not classify as local
            state[0] += 1
        # defines a mutable list
        state = [start]
        return nested_func

>>> func = func_factory(23)

>>> func('one')
one 23
>>> func('two')
two 24

>>> new_func = func_factory(46)

>>> new_func('three')
three 46
>>> new_func('four')
four 47

.. seealso:: :doc:`Accessing non-local variables<feature35>`
"""

def func_factory(start):
    """factory function returning a function working on a mutable list"""
    def nested_func(label):
        """nested function increasing the state"""
        print(label, state[0])
        # hack: in-place object changes do not classify as local
        state[0] += 1
    # defines a mutable list
    state = [start]
    return nested_func

def feature36():
    """State retention using mutable list"""
    print('State retention using mutable list')
    print('==================================\n')
    print(':py:mod:`codesnippets.feature36`')
    print('--------------------------------\n')
    print('The function below calls methods of a ``list`` to perform in-place changes.\n')
    print('.. note:: In-place object changes do not classify as local.\n')
    print('.. code-block:: Python\n')
    print('    def func_factory(start):')
    print('        def nested_func(label):')
    print('            print(label, state[0])')
    print('            # hack: in-place object changes do not classify as local')
    print('            state[0] += 1')
    print('        # defines a mutable list')
    print('        state = [start]')
    print('        return nested_func')
    print()
    print('>>> func = func_factory(23)\n')
    func = func_factory(23)
    print(">>> func('one')")
    func('one')
    print(">>> func('two')")
    func('two')
    print('\n>>> new_func = func_factory(46)\n')
    new_func = func_factory(46)
    print(">>> new_func('three')")
    new_func("three")
    print(">>> new_func('four')")
    new_func("four")
    print('\n.. seealso:: :doc:`Accessing non-local variables<feature35>`')
    print(80*'-')
