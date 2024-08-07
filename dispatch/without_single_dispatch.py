# A dictionary to store functions based on their argument types
function_map = {}

def dispatch(arg):
    # Get the type of the argument
    arg_type = type(arg)

    # If a function is registered for this type, call it
    if arg_type in function_map:
        return function_map[arg_type](arg)
    else:
        # If no function is registered for this type, raise an error
        raise TypeError(f"No function registered for argument of type {arg_type}")


def register(param_type):
    # Decorator to register a function for a specific type
    def decorator(func):
        # If a function is already registered for this type, raise an error
        if param_type in function_map:
            raise ValueError(f"Function already registered for type {param_type}")
        # Otherwise, register the function
        function_map[param_type] = func
        return func

    return decorator
