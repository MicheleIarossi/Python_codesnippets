##    Python codesnippets - Dictionary-based C-type switch
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
# Feature 19
#

"""
Dictionary-based C-type switch
==============================

:py:mod:`codesnippets.feature19`
--------------------------------

A dictionary can be used for emulating a simple switch.

Below different values are selected for different names:

>>> dict_switch = {'mike': 0.23, 'maria': 2.12, 'carl': 1.45}

>>> input_name  = 'maria'

>>> if input_name in dict_switch:
        print(f'{dict_switch[input_name]}')
else:
        print('default case')
2.12

Now the default case is triggered:

>>> input_name  = 'bob'

>>> if input_name in dict_switch:
        print(f'{dict_switch[input_name]}')
else:
        print('default case')
default case
"""

def feature19():
    """Dictionary-based C-type switch"""
    print('Dictionary-based C-type switch')
    print('==============================\n')
    print(':py:mod:`codesnippets.feature19`')
    print('--------------------------------\n')
    print('A dictionary can be used for emulating a simple switch.\n')
    print('Below different values are selected for different names:\n')
    print(">>> dict_switch = {'mike': 0.23, 'maria': 2.12, 'carl': 1.45}")
    print("\n>>> input_name  = 'maria'")
    print("\n>>> if input_name in dict_switch:")
    print("        print(f'{dict_switch[input_name]}')")
    print("else:")
    print("        print('default case')")
    dict_switch = {'mike': 0.23, 'maria': 2.12, 'carl': 1.45}
    input_name  = 'maria'
    if input_name in dict_switch:
        print(f'{dict_switch[input_name]}')
    else:
        print('default case')
    print('\nNow the default case is triggered:\n')
    print(">>> input_name  = 'bob'")
    print("\n>>> if input_name in dict_switch:")
    print("        print(f'{dict_switch[input_name]}')")
    print("else:")
    print("        print('default case')")
    input_name  = 'bob'
    if input_name in dict_switch:
        print(f'{dict_switch[input_name]}')
    else:
        print('default case')
    print(80*'-')
