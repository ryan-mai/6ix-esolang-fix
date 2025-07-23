"""
VarLang Utilities and Parsing Functions
"""

from state import variables
from exceptions import throw_error

def parse_value(value):
    """Parse a value string into the appropriate type"""
    if isinstance(value, (int, float)):
        return value
    if str(value).isdigit():
        return int(value)
    elif str(value).replace('.', '', 1).isdigit():
        return float(value)
    elif str(value).startswith('eh"') and str(value).endswith('"'):
        expr = str(value)[3:-1]  
        try:
            return eval(f'f"""{expr}"""', {}, variables)
        except Exception as e:
            throw_error(f"String interpolation failed: {e}", "generic")
    elif str(value).startswith('"') and str(value).endswith('"'):
        return str(value)[1:-1]
    elif str(value) in variables:
        return variables[str(value)]
    else:
        return value

def parse_expression(tokens):
    """Parse and evaluate an expression with operators"""
    from operations import MATH_OPERATIONS
    
    try:
        if len(tokens) == 1:
            return parse_value(tokens[0])

        if len(tokens) >= 3:
            if tokens[1] in MATH_OPERATIONS:
                left = parse_value(tokens[0])
                op = tokens[1]

                if len(tokens) == 3:
                    right = parse_value(tokens[2])
                    if op == "addy":
                        if isinstance(left, str) or isinstance(right, str):
                            return str(left) + str(right)
                        else:
                            return MATH_OPERATIONS[op](left, right)
                    else:
                        return MATH_OPERATIONS[op](left, right)
                else:
                    result = left
                    i = 1
                    while i < len(tokens) - 1:
                        if tokens[i] in MATH_OPERATIONS:
                            operator = tokens[i]
                            right_val = parse_value(tokens[i + 1])

                            if operator == "addy":
                                if isinstance(result, str) or isinstance(right_val, str):
                                    result = str(result) + str(right_val)
                                else:
                                    result = MATH_OPERATIONS[operator](result, right_val)
                            else:
                                result = MATH_OPERATIONS[operator](result, right_val)
                            i += 2
                        else:
                            i += 1
                    return result

        return None
    except ZeroDivisionError:
        throw_error("no bizzy bap croski dem error is you divided by 0 you gebert", "math")
    except (TypeError, ValueError) as e:
        throw_error(f"Broski can't do simple tings: {e}", "math") 