from override_kwargs import override_kwargs
from other_module import delegating_function, function
from datetime import datetime
from unittest import TestCase

def function_in_this_module(x=123):
    """hello I'm a docstring"""
    return x

def MyClass(object):
    def method_in_this_module(x=123):
        return x

with override_kwargs('__main__', 'function_in_this_module', {'x': 69}) as f:
    assert function_in_this_module() == 69
    assert function_in_this_module.__doc__ == f.__doc__
    assert function_in_this_module.__name__ == f.__name__
assert function_in_this_module() == 123

# with override_kwargs('__main__', 'MyClass.method_in_this_module', {'x': 69}) as f:
#     assert method_in_this_module() == 69 == f()
#     assert method_in_this_module.__doc__ == f.__doc__
#     assert method_in_this_module.__name__ == f.__name__
# assert method_in_this_module() == 123

with override_kwargs('__main__', 'function', {'x': 69}):
    assert function() == 69
assert function() == 123

with override_kwargs('other_module', 'ClassInOtherModule.method', {'x': 69}):
    assert delegating_function() == 69
assert delegating_function() == 123

with override_kwargs('other_module', 'another_module.another_function', {0: 69}):
    assert delegating_function() == 69
assert delegating_function() == 123

then = datetime(year=1982, month=3, day=19)

with override_kwargs('__main__', 'datetime', {'year': 1982}):
    assert datetime(year=2014, month=3, day=19) == then
