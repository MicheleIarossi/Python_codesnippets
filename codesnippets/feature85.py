##    Python codesnippets - Exception hierarchies
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
Exception hierarchies
=====================

:py:mod:`codesnippets.feature85`
--------------------------------

Exception hierarchies can be created by inheriting from
the ``Exception`` base class, and in turn by inheriting from
specialized exception classes:

.. code-block:: Python

    class MotorError(Exception):
        \"""a motor exception class\"""
        def __str__(self):
            exc_str = Exception.__str__(self)
            return "Exception -> MotorError. " + exc_str

    class IgnitionError(MotorError):
        \"""an ignition motor exception class\"""
        def __str__(self):
            exc_str = Exception.__str__(self)
            return "Exception -> IgnitionError. " + exc_str

    class TransmissionError(MotorError):
        \"""a transmission motor exception class\"""
        def __str__(self):
            exc_str = Exception.__str__(self)
            return "Exception -> TransmissionError. " + exc_str

With the base exception, a family of exceptions can be caught.
The call to ``sys.exc_info()`` returns a list of the exception class,
the exception instance itself, and the traceback:

>>> import sys
>>> try:
        raise TransmissionError('Error transmitting data!') # Needs an istance!
    except MotorError as exc:
        print(sys.exc_info())
        print(exc)
    finally:
        print("End of the try block...")
(<class 'codesnippets.feature85.feature85.<locals>.TransmissionError'>,
TransmissionError('Error transmitting data!'),
<traceback object at 0x7fcead50f200>)
Exception -> TransmissionError. Error transmitting data!
End of the try block...

With the specialized exceptions, specific error causes are cought.
They have to precede the base exception in the exception list:

>>> import sys
>>> try:
        raise IgnitionError('Error motor ignition!') # Needs an istance!
    except IgnitionError as exc:
        print(exc)
    except MotorError as exc:
        print(sys.exc_info())
        print(exc)
    finally:
        print("End of the try block...")
Exception -> IgnitionError. Error motor ignition!
End of the try block...
"""

import sys

def feature85():
    """Exception hierarchies"""
    print('Exception hierarchies')
    print('=====================\n')
    print(':py:mod:`codesnippets.feature85`')
    print('--------------------------------\n')
    print("Exception hierarchies can be created by inheriting from")
    print("the ``Exception`` base class, and in turn by inheriting from")
    print("specialized exception classes:\n")
    print('.. code-block:: Python\n')
    print("""    class MotorError(Exception):
        \\\"""a motor exception class\\\"""
        def __str__(self):
            exc_str = Exception.__str__(self)
            return "Exception -> MotorError. " + exc_str
          """)
    class MotorError(Exception):
        """a motor exception class"""
        def __str__(self):
            exc_str = Exception.__str__(self)
            return "Exception -> MotorError. " + exc_str
    print("""    class IgnitionError(MotorError):
        \\\"""an ignition motor exception class\\\"""
        def __str__(self):
            exc_str = Exception.__str__(self)
            return "Exception -> IgnitionError. " + exc_str
          """)
    class IgnitionError(MotorError):
        """an ignition motor exception class"""
        def __str__(self):
            exc_str = Exception.__str__(self)
            return "Exception -> IgnitionError. " + exc_str
    print("""    class TransmissionError(MotorError):
        \\\"""a transmission motor exception class\\\"""
        def __str__(self):
            exc_str = Exception.__str__(self)
            return "Exception -> TransmissionError. " + exc_str
          """)
    class TransmissionError(MotorError):
        """a transmission motor exception class"""
        def __str__(self):
            exc_str = Exception.__str__(self)
            return "Exception -> TransmissionError. " + exc_str
    print("With the base exception, a family of exceptions can be caught.")
    print("The call to ``sys.exc_info()`` returns a list of the exception class,")
    print("the exception instance itself, and the traceback:\n")
    print(">>> import sys")
    print(""">>> try:
        raise TransmissionError('Error transmitting data!') # Needs an istance!
    except MotorError as exc:
        print(sys.exc_info())
        print(exc)
    finally:
        print("End of the try block...")""")
    try:
        raise TransmissionError('Error transmitting data!') # Needs an istance!
    except MotorError as exc:
        print(sys.exc_info())
        print(exc)
    finally:
        print("End of the try block...")
    print()
    print("With the specialized exceptions, specific error causes are cought.")
    print("They have to precede the base exception in the exception list:\n")
    print(">>> import sys")
    print(""">>> try:
        raise IgnitionError('Error motor ignition!') # Needs an istance!
    except IgnitionError as exc:
        print(exc)
    except MotorError as exc:
        print(sys.exc_info())
        print(exc)
    finally:
        print("End of the try block...")""")
    try:
        raise IgnitionError('Error motor ignition!') # Needs an istance!
    except IgnitionError as exc:
        print(exc)
    except MotorError as exc:
        print(sys.exc_info())
        print(exc)
    finally:
        print("End of the try block...")
    print(80*'-')
