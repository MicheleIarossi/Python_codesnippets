##    Python codesnippets - Decorator nesting
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
# Feature 102
#

"""
Decorator nesting
=================

:py:mod:`codesnippets.feature102`
---------------------------------

Allows to add multiple layers of wrapper logic:

.. code-block:: Python

    def decorator_1(func):
        \"""very basic function decorator\"""
        print(f"\t-> inside decorator_1...")
        return func

    def decorator_2(func):
        \"""very basic function decorator\"""
        print(f"\t-> inside decorator_2...")
        return func

    def decorator_3(func):
        \"""very basic function decorator\"""
        print(f"\t-> inside decorator_3...")
        return func

>>> @decorator1
    @decorator2
    @decorator3
    def myfunction(param_a,param_b):
        \"""decorated function\"""
        print(f"\t-> inside myfunction({param_a},{param_b})")
	-> inside decorator_3...
	-> inside decorator_2...
	-> inside decorator_1...

This is equivalent to:

>>> myfunction = decorator1(decorato2(decorator3(myfunction))))

>>> myfunction(4,5)
	-> inside myfunction(4,5)
"""

def feature102():
    """Decorator nesting"""
    print('Decorator nesting')
    print('=================\n')
    print(':py:mod:`codesnippets.feature102`')
    print('---------------------------------\n')
    print('Allows to add multiple layers of wrapper logic:\n')
    print('.. code-block:: Python\n')
    print("""    def decorator_1(func):
        \\\"""very basic function decorator\\\"""
        print(f"\\t-> inside decorator_1...")
        return func
        """)
    print("""    def decorator_2(func):
        \\\"""very basic function decorator\\\"""
        print(f"\\t-> inside decorator_2...")
        return func
        """)
    print("""    def decorator_3(func):
        \\\"""very basic function decorator\\\"""
        print(f"\\t-> inside decorator_3...")
        return func
        """)
    def decorator_1(func):
        """very basic function decorator"""
        print(f"\t-> inside decorator_1...")
        return func
    def decorator_2(func):
        """very basic function decorator"""
        print(f"\t-> inside decorator_2...")
        return func
    def decorator_3(func):
        """very basic function decorator"""
        print(f"\t-> inside decorator_3...")
        return func
    print(""">>> @decorator1
    @decorator2
    @decorator3
    def myfunction(param_a,param_b):
        \\\"""decorated function\\\"""
        print(f"\\t-> inside myfunction({param_a},{param_b})") """)
    @decorator_1
    @decorator_2
    @decorator_3
    def myfunction(param_a,param_b):
        """decorated function"""
        print(f"\t-> inside myfunction({param_a},{param_b})")
    print("\nThis is equivalent to:\n")
    print(">>> myfunction = decorator1(decorato2(decorator3(myfunction))))\n")
    print(">>> myfunction(4,5)")
    myfunction(4,5)
    print(80*'-')