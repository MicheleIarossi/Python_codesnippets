##    Python codesnippets - Basic function decorator
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
# Feature 96
#

"""
Basic function decorator
========================

:py:mod:`codesnippets.feature96`
--------------------------------

A function decorator is a metafunction that manages another function.
Decoration happens only once at the end of the function definition:

.. code-block:: Python

    def decorator(func):
        \"""very basic function decorator\"""
        print(f"	-> inside decorator function...")
        return func

    @decorator
    def myfunction(param_a,param_b):
        \"""decorated function\"""
        print(f"	-> inside myfunction({param_a},{param_b})")

Decoration rebinds the function name and it's equivalent to:

>>> myfunction = decorator(myfunction)
	-> inside decorator function...

>>> myfunction(4,5)
	-> inside myfunction(4,5)
"""

def feature96():
    """Basic function decorator"""
    print('Basic function decorator')
    print('========================\n')
    print(':py:mod:`codesnippets.feature96`')
    print('--------------------------------\n')
    print('A function decorator is a metafunction that manages another function.')
    print('Decoration happens only once at the end of the function definition:\n')
    print('.. code-block:: Python\n')
    print("""    def decorator(func):
        \\\"""very basic function decorator\\\"""
        print(f"\t-> inside decorator function...")
        return func
        """)
    print("""    @decorator
    def myfunction(param_a,param_b):
        \\\"""decorated function\\\"""
        print(f"\t-> inside myfunction({param_a},{param_b})")
        """)
    print("Decoration rebinds the function name and it's equivalent to:\n")
    print(">>> myfunction = decorator(myfunction)")
    def decorator(func):
        """very basic function decorator"""
        print(f"\t-> inside decorator function...")
        return func
    @decorator
    def myfunction(param_a,param_b):
        """decorated function"""
        print(f"\t-> inside myfunction({param_a},{param_b})")
    print("\n>>> myfunction(4,5)")
    myfunction(4,5)
    print(80*'-')
