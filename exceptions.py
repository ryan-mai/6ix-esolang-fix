"""
VarLang Exception Classes
"""

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