import another_module        


def function(x=123):
    return x


def delegating_function():
    return ClassInOtherModule().method(x=123)


class ClassInOtherModule(object):
    def method(hello, x=123):
        """hello I'm a method"""
        import another_module        
        return another_module.another_function(x)
