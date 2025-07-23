variables = {}
functions = {}
error_handlers = {}  

MATH_OPERATIONS = {
    "addy": lambda x, y: x + y,      
    "chopped": lambda x, y: x - y,   
    "hella": lambda x, y: x * y,     
    "yute": lambda x, y: x / y,      
    "nize": lambda x, y: x % y,      
    "mans": lambda x, y: x ** y,     
    "two-twos": lambda x, y: x // y  
}

COMPARISON_OPERATIONS = {
    "word": lambda x, y: x == y,
    "fam": lambda x, y: x != y,
    "wallahi": lambda x, y: x < y,
    "reach": lambda x, y: x <= y,
    "bussin": lambda x, y: x > y,
    "lick": lambda x, y: x >= y,
}

LOGICAL_OPERATIONS = {
    "based": lambda x, y: bool(x) and bool(y),
    "ratio": lambda x, y: bool(x) or bool(y),
    "mid": lambda x: not bool(x),
}

IDENTITY_OPERATIONS = {
    "like": lambda x, y: x is y,
    "aint": lambda x, y: x is not y,
}

class VarLangError(Exception):
    """Base exception class for VarLang errors"""
    def __init__(self, message, error_type="generic"):
        self.message = message
        self.error_type = error_type
        super().__init__(self.message)

class VarLangMathError(VarLangError):
    """Math operation errors"""
    def __init__(self, message):
        super().__init__(message, "math")

class VarLangVariableError(VarLangError):
    """Variable-related errors"""
    def __init__(self, message):
        super().__init__(message, "variable")

class VarLangFunctionError(VarLangError):
    """Function-related errors"""
    def __init__(self, message):
        super().__init__(message, "function")

def throw_error(message, error_type="generic"):
    """Throw a VarLang error"""
    if error_type == "math":
        raise VarLangMathError(message)
    elif error_type == "variable":
        raise VarLangVariableError(message)
    elif error_type == "function":
        raise VarLangFunctionError(message)
    else:
        raise VarLangError(message, error_type)

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
            throw_error("Invalid variable syntax", "variable")
    except Exception as e:
        if isinstance(e, VarLangError):
            raise
        throw_error(f"Variable operation failed: {e}", "variable")

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
                    throw_error(f"Cannot print function: {var_name}", "generic")
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
                throw_error(f"Invalid print expression: {left} {op} {right}", "generic")
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
                throw_error("Invalid print syntax", "generic")
    except Exception as e:
        if isinstance(e, VarLangError):
            raise
        throw_error(f"Print operation failed: {e}", "generic")

def handle_operators(tokens):
    try:
        if len(tokens) != 5 or tokens[1] != "sh":
            throw_error(f"Invalid operator syntax, expected 5 tokens, got {len(tokens)}", "generic")

        def is_number(s):
            return s.isdigit() or s.replace('.', '', 1).isdigit()

        if not (is_number(tokens[2]) and is_number(tokens[4])):
            throw_error("Operator requires numeric operands", "math")

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
            throw_error(f"Unknown operator: {operator}", "math")
    except Exception as e:
        if isinstance(e, VarLangError):
            raise
        throw_error(f"Operator failed: {e}", "math")

def handle_function_definition(tokens):
    """Handle function definition: 'mans <name> takes <param1> <param2> ... does' followed by function body"""
    try:
        if len(tokens) < 5 or tokens[2] != "takes":
            throw_error("Invalid function syntax: 'mans <name> takes <params> does'", "function")

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
        throw_error(f"Broski wasnt invited to the function: {e}", "pull up to the function")

def handle_function_call(tokens):
    """Handle function call: 'ahlie <func_name> <args>'"""
    try:
        if len(tokens) < 2:
            throw_error("Two two my word fam you need a new name", "pull up to the function")

        func_name = tokens[1]
        args = tokens[2:] if len(tokens) > 2 else []

        if func_name not in functions:
            throw_error(f"Highkey '{func_name}' is wildin", "pull up to the function")

        func_def = functions[func_name]

        if len(args) != len(func_def['params']):
            throw_error(f"Croski fr pullin up to the function with '{func_name}'...twin {len(func_def['params'])} opps, got {len(args)}", "pull up to the function")

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

                execute_line(line)

        variables.clear()
        variables.update(saved_vars)

        return return_value
    except Exception as e:
        if isinstance(e, VarLangError):
            raise
        throw_error(f"Function call failed: {e}", "function")

def handle_throw(tokens):
    """Handle throwing errors: 'waste <message>' or 'waste <error_type> <message>'"""
    if len(tokens) < 2:
        throw_error("Holy fam nah trust you wildin", "mid ah")

    if len(tokens) == 2:

        message = parse_value(tokens[1])
        throw_error(str(message), "mid ah")
    else:

        error_type = tokens[1]
        message = parse_value(' '.join(tokens[2:]))
        throw_error(str(message), error_type)

def handle_try_catch(lines, start_index):
    """Handle try-catch blocks: 'trust' ... 'nah' ... 'safe'"""
    try_body = []
    catch_body = []
    current_section = "try"
    i = start_index + 1

    while i < len(lines):
        line = lines[i].strip()
        if not line or line.startswith('#'):
            i += 1
            continue

        tokens = line.split()
        if not tokens:
            i += 1
            continue

        if tokens[0] == "nah":
            current_section = "catch"
            i += 1
            continue
        elif tokens[0] == "safe":
            break

        if current_section == "try":
            try_body.append(line)
        elif current_section == "catch":
            catch_body.append(line)

        i += 1

    try:
        for line in try_body:
            execute_line(line)
    except VarLangError as e:

        variables['error_message'] = e.message
        variables['error_type'] = e.error_type
        for line in catch_body:
            execute_line(line)

    return i

def execute_line(line):
    """Execute a single line of code"""
    tokens = line.split()
    if not tokens:
        return

    cmd = tokens[0]
    if cmd == "croski":
        handle_variable(tokens)
    elif cmd == "allow":
        handle_print(tokens)
    elif cmd == "real":

        if len(tokens) == 5 and tokens[3] in COMPARISON_OPERATIONS:
            handle_comparison(tokens)
        elif len(tokens) == 5 and tokens[3] in LOGICAL_OPERATIONS and tokens[3] != "mid":
            handle_logical(tokens)
        elif len(tokens) == 4 and tokens[2] == "mid":
            handle_logical(tokens)
        elif len(tokens) == 5 and tokens[3] in IDENTITY_OPERATIONS:
            handle_identity(tokens)
        else:
            handle_operators(tokens)
    elif cmd == "ahlie":
        result = handle_function_call(tokens)
        if result is not None:
            print(result)
    elif cmd == "waste":
        handle_throw(tokens)

def run_varlang(code):
    lines = code.strip().split('\n')
    current_function = None
    i = 0

    while i < len(lines):
        line = lines[i].strip()
        if not line or line.startswith('#'):
            i += 1
            continue

        tokens = line.split()
        if not tokens:
            i += 1
            continue

        cmd = tokens[0]

        if cmd == "trust":
            i = handle_try_catch(lines, i)
            i += 1
            continue

        if cmd == "mans":
            current_function = handle_function_definition(tokens)
            i += 1
            continue

        if cmd == "bet" and current_function:
            current_function = None
            i += 1
            continue

        if current_function:
            functions[current_function]['body'].append(line)
            i += 1
            continue

        try:
            if cmd == "croski":
                handle_variable(tokens)
            elif cmd == "allow":
                handle_print(tokens)
            elif cmd == "real":

                if len(tokens) == 5 and tokens[3] in COMPARISON_OPERATIONS:
                    handle_comparison(tokens)
                elif len(tokens) == 5 and tokens[3] in LOGICAL_OPERATIONS and tokens[3] != "mid":
                    handle_logical(tokens)
                elif len(tokens) == 4 and tokens[2] == "mid":
                    handle_logical(tokens)
                elif len(tokens) == 5 and tokens[3] in IDENTITY_OPERATIONS:
                    handle_identity(tokens)
                else:
                    handle_operators(tokens)
            elif cmd == "ahlie":
                result = handle_function_call(tokens)
                if result is not None:
                    print(result)
            elif cmd == "waste":
                handle_throw(tokens)
            else:
                throw_error(f"Twin wyd fam no cap bizzy bap: {line}", "common mid ah")
        except VarLangError as e:
            print(f"You gerbert [{e.error_type}]: {e.message}")

        i += 1

test_error_handling = """
trust
    croski x fax 10
    croski y fax 0
    croski result x yute y
    allow it result
nah
    allow it "Caught error:"
    allow it error_message
    allow it error_type
safe
"""

if __name__ == "__main__":
    run_varlang(test_error_handling)