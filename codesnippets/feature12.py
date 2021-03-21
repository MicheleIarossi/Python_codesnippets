##    Python codesnippets - Sorting items of a dictionary
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
# Feature 12
#

"""
Sorting items of a dictionary
=============================

:py:mod:`codesnippets.feature12`
--------------------------------

>>> a_dict = dict(mike=5,john=2,mary=9,arnold=1)
>>> a_dict
{'mike': 5, 'john': 2, 'mary': 9, 'arnold': 1}

We use the ``sorted()`` function and a ``lambda`` function for specifying the key
for sorting on the dictionary values:

>>> sorted(a_dict.items(),key=lambda x: x[1])
[('arnold', 1), ('john', 2), ('mike', 5), ('mary', 9)]

Same but now sorting on the dictionary keys:

>>> sorted(a_dict.items(),key=lambda x: x[0])
[('arnold', 1), ('john', 2), ('mary', 9), ('mike', 5)]

.. seealso:: :doc:`Lambda functions<feature45>`
"""

def feature12():
    """Sorting items of a dictionary"""
    print("Sorting items of a dictionary")
    print('=============================\n')
    print(':py:mod:`codesnippets.feature12`')
    print('--------------------------------\n')
    print(">>> a_dict = dict(mike=5,john=2,mary=9,arnold=1)")
    a_dict = dict(mike=5,john=2,mary=9,arnold=1)
    print(">>> a_dict")
    print(a_dict)
    print("\nWe use the ``sorted()`` function and a ``lambda`` function for specifying the key")
    print("for sorting on the dictionary values:\n")
    print(">>> sorted(a_dict.items(),key=lambda x: x[1])")
    print(sorted(a_dict.items(),key=lambda x: x[1]))
    print("\nSame but now sorting on the dictionary keys:\n")
    print(">>> sorted(a_dict.items(),key=lambda x: x[0])")
    print(sorted(a_dict.items(),key=lambda x: x[0]))
    print('\n.. seealso:: :doc:`Lambda functions<feature45>`')
    print(80*'-')
