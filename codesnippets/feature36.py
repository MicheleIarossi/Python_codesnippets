##    Python codesnippets - Accessing non-local variables
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
Accessing non-local variables
=============================

:py:mod:`codesnippets.feature36`
--------------------------------

With ``nonlocal`` a nested function can get write access to variables
of enclosing scopes.
Such variables must be already existing variables: it is not possible
to create a local variable as ``global`` does for module scope variables!

.. code-block:: Python

    def enclosing_func(n_value,s_str):
        c_value = n_value # local variable initilized here
        def enclosed_func1(s1_str):
            def enclosed_func2(s2_str):
                nonlocal c_value # refers to the nonlocal 'c_value' variable
                c_value += 1 # write access!
                print(s1_str + ':' + s2_str+ ' ' + str(c_value))
            return enclosed_func2
        return enclosed_func1(s_str)

>>> hello_func = enclosing_func(33,'Hello')
>>> bye_func = enclosing_func(100,'Bye')

>>> hello_func('a')
Hello:a 34
>>> hello_func('b')
Hello:b 35
>>> hello_func('c')
Hello:c 36

>>> bye_func('e')
Bye:e 101
>>> bye_func('f')
Bye:f 102
>>> bye_func('g')
Bye:g 103

.. seealso:: :doc:`Accessing global variables<feature30>`
"""

def enclosing_func(n_value,s_str):
    """factory function returning an enclosed function accessing a nonlocal variable"""
    c_value = n_value # local variable initilized here
    def enclosed_func1(s1_str):
        """first level of enclosed function"""
        def enclosed_func2(s2_str):
            """function accessing nonlocal variable"""
            nonlocal c_value # refers to the nonlocal 'c_value' variable
            c_value += 1 # write access!
            print(s1_str + ":" + s2_str + " " + str(c_value))
        return enclosed_func2
    return enclosed_func1(s_str)

def feature36():
    """Accessing non-local variables"""
    print('Accessing non-local variables')
    print('=============================\n')
    print(':py:mod:`codesnippets.feature36`')
    print('--------------------------------\n')
    print("With ``nonlocal`` a nested function can get write access to variables")
    print('of enclosing scopes.')
    print('Such variables must be already existing variables: it is not possible')
    print('to create a local variable as ``global`` does for module scope variables!\n')
    print('.. code-block:: Python\n')
    print('    def enclosing_func(n_value,s_str):')
    print('        c_value = n_value # local variable initilized here')
    print('        def enclosed_func1(s1_str):')
    print('            def enclosed_func2(s2_str):')
    print("                nonlocal c_value # refers to the nonlocal 'c_value' variable")
    print('                c_value += 1 # write access!')
    print("                print(s1_str + ':' + s2_str+ ' ' + str(c_value))")
    print('            return enclosed_func2')
    print('        return enclosed_func1(s_str)\n')
    print(">>> hello_func = enclosing_func(33,'Hello')")
    hello_func = enclosing_func(33,"Hello")
    print(">>> bye_func = enclosing_func(100,'Bye')\n")
    bye_func = enclosing_func(100,"Bye")
    print(">>> hello_func('a')")
    hello_func("a")
    print(">>> hello_func('b')")
    hello_func("b")
    print(">>> hello_func('c')")
    hello_func("c")
    print("\n>>> bye_func('e')")
    bye_func("e")
    print(">>> bye_func('f')")
    bye_func("f")
    print(">>> bye_func('g')")
    bye_func("g")
    print('\n.. seealso:: :doc:`Accessing global variables<feature30>`')
    print(80*'-')