from dispatch import register, dispatch
from dispatch import register_wrapper, dispatch_wrapper

# Examples for Implementation: #1
@register_wrapper
def sample(x: float):
    print(f"Should Print Float: {x}")

@register_wrapper
def sample(x: int):
    print(f"Handling int: {x}")


# Examples for Implementation: #2
@register(float)
def float_handler(x: float):
    print(f"Should Print Float: {x}")

class SampleClass(str): ...
@register(SampleClass)
def sample_class_handler(x: SampleClass):
    print(f"Should Print SampleClass: {x}")

@register(int)
def int_handler(x: int):
    print(f"Should Print int: {x}")



if __name__ == '__main__':
    # Examples for Implementation: #1 (With Single Dispatcher)
    dispatch_wrapper(1.0)
    dispatch_wrapper(1)

    # Examples for Implementation: #2 (Without Single Dispatcher)
    float_handler(1.0)
    sample_class_handler(SampleClass("SampleClass"))
    int_handler(1)

    try:
        dispatch([1, 2, 3])
    except TypeError as e:
        print(e)  # Expected output: No function registered for argument of type <class 'list'>

    try:
        @register(int)
        def int_handler_duplicate(x: int):
            print(f"Should Print int: {x}")
    except Exception as e:
        print(e)  # Expected output: Function Already Registered
