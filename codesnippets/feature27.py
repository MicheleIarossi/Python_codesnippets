##    Python codesnippets - List comprehension on a file
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
# Feature 27
#

"""
List comprehension on a file
============================

:py:mod:`codesnippets.feature27`
--------------------------------

Opens, reads the file line by line and
closes it too (garbage collected because the stream is not assigned):

>>> lines = [a_line.rstrip() for a_line in open('examples.py')]

First lines read from the file ``examples.py``:

>>> '\\n'.join(lines[:10])
##    Python codesnippets runner
##    Copyright (C) 2021  Michele Iarossi
##
##    This program is free software: you can redistribute it and/or modify
##    it under the terms of the GNU General Public License as published by
##    the Free Software Foundation, either version 3 of the License, or
##    (at your option) any later version.
##
##    This program is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
"""

def feature27():
    """List comprehension on a file"""
    print('List comprehension on a file')
    print('============================\n')
    print(':py:mod:`codesnippets.feature27`')
    print('--------------------------------\n')
    print('Opens, reads the file line by line and')
    print('closes it too (garbage collected because the stream is not assigned):\n')
    print(">>> lines = [a_line.rstrip() for a_line in open('examples.py')]")
    lines = [a_line.rstrip() for a_line in open('examples.py')]
    print("\nFirst lines read from the file ``examples.py``:\n")
    print(">>> '\\\n'.join(lines[:10])")
    print('\n'.join(lines[:10]))
    print(80*'-')
