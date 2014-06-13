from contextlib import contextmanager
from functools import wraps
import importlib
from itertools import izip

@contextmanager
def override_kwargs(module_name, target, dict_):
    """
    A context handler to override arguments, useful in test code.  Patch the function/method where it gets imported, 
    this is not (necessarily) where it is defined.
    """

    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            positionals = sorted(k for k, v in dict_.iteritems() if isinstance(k, int))
            args = list(args)
            for position in positionals:
                args[position] = dict_.pop(position)
            kwargs.update(dict_)
            return fn(*args, **kwargs)
        return wrapper

    module = importlib.import_module(module_name)
    function = reduce(getattr, target.split('.'), module)
    if '.' in target:
        function_parent_name, function_name = target.rsplit('.', 1)
        function_parent = reduce(getattr, function_parent_name.split('.'), module)
    else:
        function_name = target
        function_parent = module

    old_method = function
    new_method = decorator(old_method)
    try:
        setattr(function_parent, function_name, new_method)
        yield new_method
    finally:
        setattr(function_parent, function_name, old_method)
