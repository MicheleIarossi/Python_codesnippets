##    Python codesnippets - Relative import from a module package
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
# Feature 56
#

"""
Relative import from a module package
=====================================

:py:mod:`codesnippets.feature56`
--------------------------------

Intrapackage imports work if the relative import syntax is used.

In the following the ``.`` is the current working directory (CWD):

``./tools.py`` is the ``tools`` module in the CWD; defines ``MY_X = 1``

``./pkg/tools.py`` is the ``tools`` module in the ``./pkg`` folder; defines ``MY_X = 2``

``./pkg/utilr.py`` is the ``utilr``  module in the ``./pkg`` folder importing ``tools``
with relative syntax

The question is which ``tools`` module gets imported when the next import statement is run:

>>> import pkg.utilr

	This is the ``utilr`` module inside ``./pkg`` .

	In the following code the ``tools`` module is imported, but
	**relative** import takes place here:
	the ``tools`` module from the ``./pkg`` directory is imported,
	not the one in the CWD ``./tool.py`` !

		.. code-block:: Python

			from . import tools    # relative import syntax

		This is the ``tools`` module inside ``./pkg``

		.. code-block:: Python

			MY_X = 2

>>> pkg.utilr.tools.MY_X
2

.. seealso:: :doc:`Absolute import from a module package<feature55>`
"""

import importlib

def feature56():
    """Relative import from a module package"""
    print('Relative import from a module package')
    print('=====================================\n')
    print(':py:mod:`codesnippets.feature56`')
    print('--------------------------------\n')
    print('Intrapackage imports work if the relative import syntax is used.\n')
    print('In the following the ``.`` is the current working directory (CWD):\n')
    print('``./tools.py`` is the ``tools`` module in the CWD; defines ``MY_X = 1``\n')
    print('``./pkg/tools.py`` is the ``tools`` module in the ``./pkg`` folder; defines ``MY_X = 2``\n')
    print('``./pkg/utilr.py`` is the ``utilr``  module in the ``./pkg`` folder importing ``tools``'
          '\nwith relative syntax\n')
    print('The question is which ``tools`` module gets imported when the next '
          'import statement is run:\n')
    print('>>> import pkg.utilr\n')
    utilr = importlib.import_module('.utilr','codesnippets.pkg')
    print(">>> pkg.utilr.tools.MY_X")
    print(utilr.tools.MY_X)
    print('\n.. seealso:: :doc:`Absolute import from a module package<feature55>`')
    print(80*'-')