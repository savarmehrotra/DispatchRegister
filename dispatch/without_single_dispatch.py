from typing import Callable, Dict, Type, Any

# A dictionary to store functions based on their argument types
function_map: Dict[Type, Callable] = {}

# For Custom Functions
def dispatch(arg: Any) -> Any:
    # Get the type of the argument
    arg_type = type(arg)

    # If a function is registered for this type, call it
    if arg_type in function_map:
        # Retrieve the function associated with this type
        func = function_map[arg_type]
        # Call the function with the argument
        result = func(arg)
        return result
    else:
        # If no function is registered for this type, raise an error
        raise TypeError(f"No function registered for argument of type {arg_type}")


def register(param_type: Type) -> Callable:
    # Decorator to register a function for a specific type
    def decorator(func: Callable) -> Callable:

        if param_type in function_map:
            raise ValueError(f"Function already registered for type {param_type}")
        function_map[param_type] = func
        return func

    return decorator
