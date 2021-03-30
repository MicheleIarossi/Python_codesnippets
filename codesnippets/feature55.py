##    Python codesnippets - Absolute import from a module package
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
# Feature 55
#

"""
Absolute import from a module package
=====================================

:py:mod:`codesnippets.feature55`
--------------------------------

Intrapackage imports follow the rule of the absolute path import
if relative import is not used!

In the following the ``.`` is the current working directory (CWD):

``./tools.py`` is the ``tools`` module in the CWD; defines ``MY_X = 1``

``./pkg/tools.py`` is the ``tools`` module in the ``./pkg`` folder; defines ``MY_X = 2``

``./pkg/util.py`` is the ``util``  module in the ``./pkg`` folder importing ``tools``
with absolute syntax

The question is which ``tools`` module gets imported when the next import statement is run:

>>> import pkg.util

	This is the ``util`` module inside ``./pkg`` .

	In the following code the ``tools`` module is imported, but
	**absolute** import takes place here:
	the ``tools`` module from the CWD is imported,
	not the one relative to the package ``./pkg/tools.py`` !

		.. code-block:: Python

			import tools  # absolute import syntax

		Ths is the ``tools`` module in the CWD ``.``

		.. code-block:: Python

			MY_X = 1

>>> pkg.util.tools.MY_X
1

.. seealso:: :doc:`Relative import from a module package<feature56>`
"""
import importlib

def feature55():
    """Absolute import from a module package"""
    print('Absolute import from a module package')
    print('=====================================\n')
    print(':py:mod:`codesnippets.feature55`')
    print('--------------------------------\n')
    print('Intrapackage imports follow the rule of the absolute path import')
    print('if relative import is not used!\n')
    print('In the following the ``.`` is the current working directory (CWD):\n')
    print('``./tools.py`` is the ``tools`` module in the CWD; defines ``MY_X = 1``\n')
    print('``./pkg/tools.py`` is the ``tools`` module in the ``./pkg`` folder; defines ``MY_X = 2``\n')
    print('``./pkg/util.py`` is the ``util``  module in the ``./pkg`` folder importing ``tools``'
          '\nwith absolute syntax\n')
    print('The question is which ``tools`` module gets imported when the next '
          'import statement is run:\n')
    print('>>> import pkg.util\n')
    util = importlib.import_module('.util','codesnippets.pkg')
    print(">>> pkg.util.tools.MY_X")
    print(util.tools.MY_X)
    print('\n.. seealso:: :doc:`Relative import from a module package<feature56>`')
    print(80*'-')