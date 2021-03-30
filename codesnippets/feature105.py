##    Python codesnippets - Call tracer with a class descriptor used as decorator
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
# Feature 105
#

"""
Call tracer with a class descriptor used as decorator
=====================================================

:py:mod:`codesnippets.feature105`
---------------------------------

This is a complex example combining more Python features:

.. code-block:: Python

    class DescTracer:
        \"""a function or method descriptor tracer class\"""
        def __init__(self,func_or_method):
            print(f"	-> DescTracer.__init__() run at decoration time")
            self.calls = 0
            self.func_or_method = func_or_method
        def __call__(self,*args,**kwargs):
            print(f"	-> DescTracer.__call__() run at function or method call")
            self.calls += 1
            print(f"	-> total function calls of {self.func_or_method.__name__}: {self.calls}")
            return self.func_or_method(*args,**kwargs)
        def __get__(self,instance,owner):
            print(f"	-> DescTracer.__get__() run on method attribute fetch of instance of class"
                  f" {instance.__class__.__name__}")
            return Wrapper(self,instance)

    class Wrapper:
        \"""Wrapper class needed for storing the instance whose method call must be counted
           and for routing back the call to the descriptor tracer
        \"""
        def __init__(self,desc_tracer,instance):
            print(f"	-> Wrapper.__init__() run at wrapper creation")
            self.desc_tracer = desc_tracer
            self.instance = instance
        def __call__(self,*args,**kwargs):
            print(f"	-> Wrapper.__call__() run at wrapper call")
            return self.desc_tracer(self.instance,*args,**kwargs

Example of function decoration:

>>> @DescTracer
    def my_func(param_a,param_b)
        \"""my decorated function\"""
        print(f"	-> inside my_func({param_a},{param_b})...")
	-> DescTracer.__init__() run at decoration time

When ``my_func(param_a,param_b)`` is decorated, it gets an instance of the ``DescTracer`` class.
Later on when the function is called, it is the ``__call__()`` method of the descriptor tracer
class that is actually called, and the counter is incremented.

>>> my_func(2,3)
	-> DescTracer.__call__() run at function or method call
	-> total function calls of my_func: 1
	-> inside my_func(2,3)...

>>> my_func(6,7)
	-> DescTracer.__call__() run at function or method call
	-> total function calls of my_func: 2
	-> inside my_func(6,7)...

Example of class method decoration:

>>> class MyClass:
        \"""a class\"""
        def __init__(self,name):
            print(f"	-> inside MyClass.__init__()")
            self._name = name
        @DescTracer
        def my_method(self):
            \"""my decorated method\"""
            print(f"	-> inside MyClass.my_method()")
	-> DescTracer.__init__() run at decoration time

When ``my_method()`` is decorated, it is bound to the descriptor class.
Later on when the method is invoked on the instance, an attribute fetch
happens and the ``__get__()`` method of the descriptor class is triggered.
The ``__get__()`` method returns an instance of the ``Wrapper`` class
storing a pointer to the instance of the descriptor class and
to the instance of ``MyClass``.

Next is the function call, but now it is actually a function
call done on the instance of the ``Wrapper`` class, and the
``__call__()`` method of the ``Wrapper`` class is called.

The latter method reroutes the call to the instance of the descriptor class
by doing a function call, which triggers the method ``__call__()``
of the descriptor class which finally calls the original method
applied on the instance of ``MyClass``.

>>> my_obj_1 = MyClass('Star')
	-> inside MyClass.__init__()

>>> my_obj_1.my_method()
	-> DescTracer.__get__() run on method attribute fetch of instance of class MyClass
	-> Wrapper.__init__() run at wrapper creation
	-> Wrapper.__call__() run at wrapper call
	-> DescTracer.__call__() run at function or method call
	-> total function calls of my_method: 1
	-> inside MyClass.my_method()

>>> my_obj_1.my_method()
	-> DescTracer.__get__() run on method attribute fetch of instance of class MyClass
	-> Wrapper.__init__() run at wrapper creation
	-> Wrapper.__call__() run at wrapper call
	-> DescTracer.__call__() run at function or method call
	-> total function calls of my_method: 2
	-> inside MyClass.my_method()
"""

def feature105():
    """Call tracer with a class descriptor used as decorator"""
    print('Call tracer with a class descriptor used as decorator')
    print('=====================================================\n')
    print(':py:mod:`codesnippets.feature105`')
    print('---------------------------------\n')
    print('This is a complex example combining more Python features:\n')
    print('.. code-block:: Python\n')
    print("""    class DescTracer:
        \\\"""a function or method descriptor tracer class\\\"""
        def __init__(self,func_or_method):
            print(f"\t-> DescTracer.__init__() run at decoration time")
            self.calls = 0
            self.func_or_method = func_or_method
        def __call__(self,*args,**kwargs):
            print(f"\t-> DescTracer.__call__() run at function or method call")
            self.calls += 1
            print(f"\t-> total function calls of {self.func_or_method.__name__}: {self.calls}")
            return self.func_or_method(*args,**kwargs)
        def __get__(self,instance,owner):
            print(f"\t-> DescTracer.__get__() run on method attribute fetch of instance of class"
                  f" {instance.__class__.__name__}")
            return Wrapper(self,instance)
        """)
    print("""    class Wrapper:
        \\\"""Wrapper class needed for storing the instance whose method call must be counted
           and for routing back the call to the descriptor tracer
        \\\"""
        def __init__(self,desc_tracer,instance):
            print(f"\t-> Wrapper.__init__() run at wrapper creation")
            self.desc_tracer = desc_tracer
            self.instance = instance
        def __call__(self,*args,**kwargs):
            print(f"\t-> Wrapper.__call__() run at wrapper call")
            return self.desc_tracer(self.instance,*args,**kwargs
        """)
    class DescTracer:
        """a function or method descriptor tracer class"""
        def __init__(self,func_or_method):
            print(f"\t-> DescTracer.__init__() run at decoration time")
            self.calls = 0
            self.func_or_method = func_or_method
        def __call__(self,*args,**kwargs):
            print(f"\t-> DescTracer.__call__() run at function or method call")
            self.calls += 1
            print(f"\t-> total function calls of {self.func_or_method.__name__}: {self.calls}")
            return self.func_or_method(*args,**kwargs)
        def __get__(self,instance,owner):
            print(f"\t-> DescTracer.__get__() run on method attribute fetch of instance of class"
                  f" {instance.__class__.__name__}")
            return Wrapper(self,instance)
    class Wrapper:
        """Wrapper class needed for storing the instance whose method call must be counted
           and for routing back the call to the descriptor tracer
        """
        def __init__(self,desc_tracer,instance):
            print(f"\t-> Wrapper.__init__() run at wrapper creation")
            self.desc_tracer = desc_tracer
            self.instance = instance
        def __call__(self,*args,**kwargs):
            print(f"\t-> Wrapper.__call__() run at wrapper call")
            return self.desc_tracer(self.instance,*args,**kwargs)

    print("Example of function decoration:\n")
    print(""">>> @DescTracer
    def my_func(param_a,param_b):
        \\\"""my decorated function\\\"""
        print(f"\t-> inside my_func({param_a},{param_b})...")""")
    @DescTracer
    def my_func(param_a,param_b):
        """my decorated function"""
        print(f"\t-> inside my_func({param_a},{param_b})...")
    print()
    print("When ``my_func(param_a,param_b)`` is decorated, it gets an instance of"
          " the ``DescTracer`` class.")
    print("Later on when the function is called, it is the ``__call__()``"
          " method of the descriptor tracer")
    print("class that is actually called, and the counter is incremented.")
    print()
    print(">>> my_func(2,3)")
    my_func(2,3)
    print()
    print(">>> my_func(6,7)")
    my_func(6,7)
    print()
    print("Example of class method decoration:\n")
    print(""">>> class MyClass:
        \\\"""a class\\\"""
        def __init__(self,name):
            print(f"\t-> inside MyClass.__init__()")
            self._name = name
        @DescTracer
        def my_method(self):
            \\\"""my decorated method\\\"""
            print(f"\t-> inside MyClass.my_method()")""")
    class MyClass:
        """a class"""
        def __init__(self,name):
            print(f"\t-> inside MyClass.__init__()")
            self._name = name
        @DescTracer
        def my_method(self):
            """my decorated method"""
            print(f"\t-> inside MyClass.my_method()")
    print()
    print("When ``my_method()`` is decorated, it is bound to the descriptor class.")
    print("Later on when the method is invoked on the instance, an attribute fetch")
    print("happens and the ``__get__()`` method of the descriptor class is triggered.")
    print("The ``__get__()`` method returns an instance of the ``Wrapper`` class")
    print("storing a pointer to the instance of the descriptor class and")
    print("to the instance of ``MyClass``.\n")
    print("Next is the function call, but now it is actually a function")
    print("call done on the instance of the ``Wrapper`` class, and the")
    print("``__call__()`` method of the ``Wrapper`` class is called.\n")
    print("The latter method reroutes the call to the instance of the descriptor class")
    print("by doing a function call, which triggers the method ``__call__()``")
    print("of the descriptor class which finally calls the original method")
    print("applied on the instance of ``MyClass``.")
    print()
    print(">>> my_obj_1 = MyClass('Star')")
    my_obj_1 = MyClass('Star')
    print()
    print(">>> my_obj_1.my_method()")
    my_obj_1.my_method()
    print()
    print(">>> my_obj_1.my_method()")
    my_obj_1.my_method()
    print(80*'-')