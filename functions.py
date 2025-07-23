"""
VarLang Function Handling
"""

from exceptions import VarLangError, throw_error
from state import variables, functions
from utils import parse_value

def handle_function_definition(tokens):
<<<<<<< HEAD
    """Handle function definition: 'mans <name> takes <param1> <param2> ... does' followed by function body"""
    try:
        if len(tokens) < 5 or tokens[2] != "takes":
            throw_error("Invalid function syntax: 'mans <name> takes <params> does'", "function")
=======
    try:
        if len(tokens) < 5 or tokens[2] != "takes":
            throw_error("Fam what are you yappin about this the lingo: 'mans <name> takes <params> does'", "function")
>>>>>>> e1c1f4a89b85d9d4f7630d921559f2eb950a1181

        func_name = tokens[1]

        does_index = -1
        for i, token in enumerate(tokens):
            if token == "does":
                does_index = i
                break

        if does_index == -1:
            throw_error("Function definition missing 'does'", "function")

        params = tokens[3:does_index]

        functions[func_name] = {
            'params': params,
            'body': []
        }

        return func_name
    except Exception as e:
        if isinstance(e, VarLangError):
            raise
        throw_error(f"Function definition failed: {e}", "function")

def handle_function_call(tokens):
    """Handle function call: 'ahlie <func_name> <args>'"""
    try:
        if len(tokens) < 2:
<<<<<<< HEAD
            throw_error("Function call missing name", "function")
=======
            throw_error("Function dem missin them name", "function")
>>>>>>> e1c1f4a89b85d9d4f7630d921559f2eb950a1181

        func_name = tokens[1]
        args = tokens[2:] if len(tokens) > 2 else []

        if func_name not in functions:
<<<<<<< HEAD
            throw_error(f"Function '{func_name}' not found", "function")
=======
            throw_error(f"Where the function '{func_name}'...Where the function", "function")
>>>>>>> e1c1f4a89b85d9d4f7630d921559f2eb950a1181

        func_def = functions[func_name]

        if len(args) != len(func_def['params']):
<<<<<<< HEAD
            throw_error(f"Function '{func_name}' expects {len(func_def['params'])} args, got {len(args)}", "function")
=======
            throw_error(f"Function '{func_name}' t-dot {len(func_def['params'])} fly, told {len(args)}", "function")
>>>>>>> e1c1f4a89b85d9d4f7630d921559f2eb950a1181

        saved_vars = variables.copy()

        for param, arg in zip(func_def['params'], args):
            arg_val = parse_value(arg)

            if isinstance(arg_val, str):
                if arg_val.isdigit():
                    arg_val = int(arg_val)
                elif arg_val.replace('.', '', 1).isdigit():
                    arg_val = float(arg_val)
            variables[param] = arg_val

        return_value = None
        for line in func_def['body']:
            tokens = line.split()
            if tokens and tokens[0] == "send":
                if len(tokens) > 1:
                    return_expr = ' '.join(tokens[1:])
                    return_value = parse_value(return_expr)
                    break
                else:
                    return_value = None
                    break
            else:
                # Import here to avoid circular import
                from interpreter import execute_line
                execute_line(line)

        variables.clear()
        variables.update(saved_vars)

        return return_value
    except Exception as e:
        if isinstance(e, VarLangError):
            raise
<<<<<<< HEAD
        throw_error(f"Function call failed: {e}", "function") 
=======
        throw_error(f"Bro was not invited to the function: {e}", "function") 
>>>>>>> e1c1f4a89b85d9d4f7630d921559f2eb950a1181
