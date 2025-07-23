"""
VarLang Statement Handlers
"""

from exceptions import throw_error, VarLangError
from operations import MATH_OPERATIONS, COMPARISON_OPERATIONS, LOGICAL_OPERATIONS, IDENTITY_OPERATIONS
from utils import parse_value, parse_expression
from state import variables, functions

def handle_assignment(tokens):
    try:
        var_name = tokens[1]

        if len(tokens) >= 5 and tokens[2] == "money" and tokens[3] == "up":
            operator = "money up"
            value = ' '.join(tokens[4:])
            parsed_value = parse_value(value)  
        elif len(tokens) >= 5 and tokens[2] == "funny" and tokens[3] == "up":
            operator = "funny up"
            value = ' '.join(tokens[4:])
            parsed_value = parse_value(value)  
        else:
            operator = tokens[2]
            value_tokens = tokens[3:]

            if len(value_tokens) >= 3 and any(token in MATH_OPERATIONS for token in value_tokens):
                parsed_value = parse_expression(value_tokens)
            else:
                value = ' '.join(value_tokens)
                parsed_value = parse_value(value)

        if parsed_value is None:
            throw_error(f"Invalid value: {value}", "variable")

        if operator == "fax": 
            variables[var_name] = parsed_value
        elif operator == "money up": 
            if var_name in variables:
                variables[var_name] = MATH_OPERATIONS["addy"](variables[var_name], parsed_value)
            else:
                throw_error(f"Variable '{var_name}' not defined", "variable")
        elif operator == "funny up": 
            if var_name in variables:
                variables[var_name] = MATH_OPERATIONS["chopped"](variables[var_name], parsed_value)
            else:
                throw_error(f"Variable '{var_name}' not defined", "variable")
        elif operator == "cheesed": 
            if var_name in variables:
                variables[var_name] = MATH_OPERATIONS["hella"](variables[var_name], parsed_value)
            else:
                throw_error(f"Variable '{var_name}' not defined", "variable")
        elif operator == "mandem": 
            if var_name in variables:
                variables[var_name] = MATH_OPERATIONS["yute"](variables[var_name], parsed_value)
            else:
                throw_error(f"Variable '{var_name}' not defined", "variable")
        elif operator == "steeze": 
            if var_name in variables:
                variables[var_name] = MATH_OPERATIONS["nize"](variables[var_name], parsed_value)
            else:
                throw_error(f"Variable '{var_name}' not defined", "variable")
        elif operator == "dun": 
            if var_name in variables:
                variables[var_name] = MATH_OPERATIONS["mans"](variables[var_name], parsed_value)
            else:
                throw_error(f"Variable '{var_name}' not defined", "variable")
        elif operator == "bucktee": 
            if var_name in variables:
                variables[var_name] = MATH_OPERATIONS["two-twos"](variables[var_name], parsed_value)
            else:
                throw_error(f"Variable '{var_name}' not defined", "variable")
        else:
            throw_error(f"Unknown assignment operator: {operator}", "variable")
    except Exception as e:
        if isinstance(e, VarLangError):
            raise
        throw_error(f"Assignment failed: {e}", "variable")

def handle_comparison(tokens):
    try:
        if len(tokens) != 5 or tokens[1] != "sh":
            throw_error(f"Invalid comparison syntax, expected 5 tokens, got {len(tokens)}", "generic")

        left = tokens[2]
        op = tokens[3]
        right = tokens[4]

        left_val = variables[left] if left in variables else parse_value(left)
        right_val = variables[right] if right in variables else parse_value(right)

        if left_val is None or right_val is None:
            throw_error("Invalid comparison operands", "generic")

        try:
            if (isinstance(left_val, (int, float)) or (isinstance(left_val, str) and left_val.replace('.', '', 1).lstrip('-').isdigit())) and \
               (isinstance(right_val, (int, float)) or (isinstance(right_val, str) and right_val.replace('.', '', 1).lstrip('-').isdigit())):
                left_val = float(left_val)
                right_val = float(right_val)

                if left_val.is_integer():
                    left_val = int(left_val)
                if right_val.is_integer():
                    right_val = int(right_val)
        except Exception:
            pass

        if op in COMPARISON_OPERATIONS:
            try:
                result = COMPARISON_OPERATIONS[op](left_val, right_val)
                print(result)
            except TypeError:
                throw_error(f"Can't compare {type(left_val).__name__} and {type(right_val).__name__}", "generic")
        else:
            throw_error(f"Unknown comparison operator: {op}", "generic")
    except Exception as e:
        if isinstance(e, VarLangError):
            raise
        throw_error(f"Comparison failed: {e}", "generic")

def handle_logical(tokens):
    try:
        if len(tokens) == 5 and tokens[1] == "sh":
            left = tokens[2]
            op = tokens[3]
            right = tokens[4]
            left_val = variables[left] if left in variables else parse_value(left)
            right_val = variables[right] if right in variables else parse_value(right)
            if left_val is None or right_val is None:
                throw_error("Invalid logical operands", "generic")
            if op in LOGICAL_OPERATIONS and op != "mid":
                result = LOGICAL_OPERATIONS[op](left_val, right_val)
                print(result)
            else:
                throw_error(f"Unknown logical operator: {op}", "generic")
        elif len(tokens) == 4 and tokens[1] == "sh" and tokens[2] == "mid":
            value = tokens[3]
            val = variables[value] if value in variables else parse_value(value)
            if val is None:
                throw_error("Invalid logical operand for 'mid'", "generic")
            print(LOGICAL_OPERATIONS["mid"](val))
        else:
            throw_error(f"Invalid logical syntax, got {len(tokens)} tokens", "generic")
    except Exception as e:
        if isinstance(e, VarLangError):
            raise
        throw_error(f"Logical operation failed: {e}", "generic")

def handle_identity(tokens):
    try:
        if len(tokens) == 5 and tokens[1] == "sh":
            left = tokens[2]
            op = tokens[3]
            right = tokens[4]
            left_val = variables[left] if left in variables else parse_value(left)
            right_val = variables[right] if right in variables else parse_value(right)
            if left_val is None or right_val is None:
                throw_error("Invalid identity operands", "generic")
            if op in IDENTITY_OPERATIONS:
                result = IDENTITY_OPERATIONS[op](left_val, right_val)
                print(result)
            else:
                throw_error(f"Unknown identity operator: {op}", "generic")
        else:
            throw_error("Invalid identity syntax", "generic")
    except Exception as e:
        if isinstance(e, VarLangError):
            raise
        throw_error(f"Identity operation failed: {e}", "generic")

def handle_variable(tokens):
    try:
        if len(tokens) >= 3:
            is_assignment = False
            if len(tokens) >= 4 and tokens[2] in ["fax", "cheesed", "mandem", "steeze", "dun", "bucktee"]:
                is_assignment = True
            elif len(tokens) >= 5 and tokens[2] == "money" and tokens[3] == "up":
                is_assignment = True
            elif len(tokens) >= 5 and tokens[2] == "funny" and tokens[3] == "up":
                is_assignment = True

            if is_assignment:
                handle_assignment(tokens)
                return

            if len(tokens) >= 5 and any(token in MATH_OPERATIONS for token in tokens[3:]):
                var_name = tokens[1]
                expression_tokens = tokens[2:]
                result = parse_expression(expression_tokens)
                if result is not None:
                    variables[var_name] = result
                    return

            if len(tokens) >= 4 and tokens[2] == "ahlie":
                var_name = tokens[1]
                from functions import handle_function_call
                func_result = handle_function_call(tokens[2:])
                if func_result is not None:
                    variables[var_name] = func_result
                    return

            var_name = tokens[1]
            value = ' '.join(tokens[2:])

            if value.startswith('ting(') and value.endswith(')'):
                inner_value = value[5:-1]

                if inner_value in variables:
                    actual_value = variables[inner_value]
                else:
                    if inner_value.isdigit():
                        actual_value = int(inner_value)
                    elif inner_value.replace('.', '', 1).isdigit():
                        actual_value = float(inner_value)
                    elif inner_value.startswith('"') and inner_value.endswith('"'):
                        actual_value = inner_value[1:-1]
                    else:
                        actual_value = inner_value

                if isinstance(actual_value, int):
                    result_type = "int"
                elif isinstance(actual_value, float):
                    result_type = "float"
                elif isinstance(actual_value, str):
                    result_type = "str"
                else:
                    result_type = "wasteman"

                variables[var_name] = result_type
            elif value.isdigit():
                variables[var_name] = int(value)
            elif value.replace('.', '', 1).isdigit():
                variables[var_name] = float(value)
            elif value.startswith('"') and value.endswith('"'):
                variables[var_name] = value[1:-1]
            else:
                parsed_val = parse_value(value)
                if parsed_val is not None:
                    variables[var_name] = parsed_val
                else:
                    throw_error(f"Invalid value: {value}", "variable")
        else:
<<<<<<< HEAD
            throw_error("Invalid variable syntax", "variable")
    except Exception as e:
        if isinstance(e, VarLangError):
            raise
        throw_error(f"Variable operation failed: {e}", "variable")
=======
            throw_error("Croski dont know what variable he saying", "variable")
    except Exception as e:
        if isinstance(e, VarLangError):
            raise
        throw_error(f"Variable sh failed: {e}", "variable")
>>>>>>> e1c1f4a89b85d9d4f7630d921559f2eb950a1181

def handle_print(tokens):
    try:
        if len(tokens) == 3 and tokens[1] == "it":
            var_name = tokens[2]

            if var_name.startswith('"') and var_name.endswith('"'):
                print(var_name[1:-1])
                return

            if var_name in variables:
                print(variables[var_name])
                return

            try:
                val = parse_value(var_name)
                if var_name in functions:
<<<<<<< HEAD
                    throw_error(f"Cannot print function: {var_name}", "generic")
=======
                    throw_error(f"Strugglin to allow it fam: {var_name}", "generic")
>>>>>>> e1c1f4a89b85d9d4f7630d921559f2eb950a1181
                else:
                    print(val)
            except Exception:
                throw_error(f"Unknown variable: {var_name}", "variable")

        elif len(tokens) == 5 and tokens[1] == "it" and tokens[3] in MATH_OPERATIONS:
            left = tokens[2]
            op = tokens[3]
            right = tokens[4]
            left_val = variables[left] if left in variables else parse_value(left)
            right_val = variables[right] if right in variables else parse_value(right)
            if left_val is None or right_val is None:
<<<<<<< HEAD
                throw_error(f"Invalid print expression: {left} {op} {right}", "generic")
=======
                throw_error(f"Bro allow it saying wrong sh: {left} {op} {right}", "generic")
>>>>>>> e1c1f4a89b85d9d4f7630d921559f2eb950a1181
            if op == "addy":
                if isinstance(left_val, str) or isinstance(right_val, str):
                    print(str(left_val) + str(right_val))
                else:
                    print(MATH_OPERATIONS[op](left_val, right_val))
            else:
                print(MATH_OPERATIONS[op](left_val, right_val))
        else:
            if len(tokens) >= 3 and tokens[1] == "it":
                if len(tokens) == 3 and tokens[2] in variables:
                    print(variables[tokens[2]])
                else:
                    print(' '.join(tokens[2:]))
            else:
<<<<<<< HEAD
                throw_error("Invalid print syntax", "generic")
    except Exception as e:
        if isinstance(e, VarLangError):
            raise
        throw_error(f"Print operation failed: {e}", "generic")
=======
                throw_error("Bro not from here like allow it fam", "generic")
    except Exception as e:
        if isinstance(e, VarLangError):
            raise
        throw_error(f"Nah allow it failed: {e}", "generic")
>>>>>>> e1c1f4a89b85d9d4f7630d921559f2eb950a1181

def handle_operators(tokens):
    try:
        if len(tokens) != 5 or tokens[1] != "sh":
<<<<<<< HEAD
            throw_error(f"Invalid operator syntax, expected 5 tokens, got {len(tokens)}", "generic")
=======
            throw_error(f"Two two my word fam operator, expected 5 sh, got {len(tokens)}", "generic")
>>>>>>> e1c1f4a89b85d9d4f7630d921559f2eb950a1181

        def is_number(s):
            return s.isdigit() or s.replace('.', '', 1).isdigit()

        if not (is_number(tokens[2]) and is_number(tokens[4])):
<<<<<<< HEAD
            throw_error("Operator requires numeric operands", "math")
=======
            throw_error("Operator requires yo digits not yo funny up", "math")
>>>>>>> e1c1f4a89b85d9d4f7630d921559f2eb950a1181

        if '.' in tokens[2]:
            value_1 = float(tokens[2])
        else:
            value_1 = int(tokens[2])

        if '.' in tokens[4]:
            value_2 = float(tokens[4])
        else:
            value_2 = int(tokens[4])

        operator = tokens[3]

        if operator in MATH_OPERATIONS:
            result = MATH_OPERATIONS[operator](value_1, value_2)
            print(result)
        else:
<<<<<<< HEAD
            throw_error(f"Unknown operator: {operator}", "math")
=======
            throw_error(f"Bro aint no operator: {operator}", "math")
>>>>>>> e1c1f4a89b85d9d4f7630d921559f2eb950a1181
    except Exception as e:
        if isinstance(e, VarLangError):
            raise
        throw_error(f"Operator failed: {e}", "math")

def handle_throw(tokens):
<<<<<<< HEAD
    """Handle throwing errors: 'waste <message>' or 'waste <error_type> <message>'"""
    if len(tokens) < 2:
        throw_error("Throw statement missing message", "generic")
=======
    if len(tokens) < 2:
        throw_error("Gyatt statement missin message", "generic")
>>>>>>> e1c1f4a89b85d9d4f7630d921559f2eb950a1181

    if len(tokens) == 2:
        message = parse_value(tokens[1])
        throw_error(str(message), "generic")
    else:
        error_type = tokens[1]
        message = parse_value(' '.join(tokens[2:]))
        throw_error(str(message), error_type)