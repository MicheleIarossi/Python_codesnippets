##    Python codesnippets - Exception handling
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
# Feature 85
#

"""
Exception handling
==================

:py:mod:`codesnippets.feature85`
--------------------------------

``try`` -> ``except`` -> ``else`` -> ``finally``

The ``else`` part is run ONLY if no exception occurs,
and the ``finally`` part is run in any case.

.. note:: Exceptions always catch (and raise!) a class instance object.

>>> a_str = 'test'

>>> try:
        a_chr = a_str[5]
        print('selected a_chr = ' + a_chr)
    except IndexError as exc:
        print('-> Exception: ' + str(exc))
        print(dir(exc))
    else:
        print('-> else: no exception')
    finally:
        print('-> finally: leaving the try statement')
-> Exception: string index out of range
-> finally: leaving the try statement

>>> try:
        a_chr = a_str[3]
        print('selected a_chr = ' + a_chr)
    except IndexError as exc:
        print('-> Exception: ' + str(exc))
        print(dir(exc))
    else:
        print('-> else: no exception')
    finally:
        print('-> finally: leaving the try statement')
selected a_chr = t
-> else: no exception
-> finally: leaving the try statement
"""

def feature85():
    """Exception handling"""
    print('Exception handling')
    print('==================\n')
    print(':py:mod:`codesnippets.feature85`')
    print('--------------------------------\n')
    print("``try`` -> ``except`` -> ``else`` -> ``finally``\n")
    print("The ``else`` part is run ONLY if no exception occurs,")
    print("and the ``finally`` part is run in any case.\n")
    print(".. note:: Exceptions always catch (and raise!) a class instance object.\n")
    print(">>> a_str = 'test'\n")
    a_str = 'test'
    print(""">>> try:
        a_chr = a_str[5]
        print('selected a_chr = ' + a_chr)
    except IndexError as exc:
        print('-> Exception: ' + str(exc))
        print(dir(exc))
    else:
        print('-> else: no exception')
    finally:
        print('-> finally: leaving the try statement')""")
    try:
        a_chr = a_str[5]
        print('selected a_chr = ' + a_chr)
    except IndexError as exc:
        print('-> Exception: ' + str(exc))
    else:
        print('-> else: no exception')
    finally:
        print('-> finally: leaving the try statement\n')
    print(""">>> try:
        a_chr = a_str[3]
        print('selected a_chr = ' + a_chr)
    except IndexError as exc:
        print('-> Exception: ' + str(exc))
        print(dir(exc))
    else:
        print('-> else: no exception')
    finally:
        print('-> finally: leaving the try statement')""")
    try:
        a_chr = a_str[3]
        print('selected a_chr = ' + a_chr)
    except IndexError as exc:
        print('-> Exception: ' + str(exc))
    else:
        print('-> else: no exception')
    finally:
        print('-> finally: leaving the try statement')
    print(80*'-')