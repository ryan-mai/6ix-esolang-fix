# 6ix Esolang Interpreter

[Official Documentation](https://6ix-esolang-docs.vercel.app/)
[Official Interpreter](https://sixix-esolang-interpreter.onrender.com/)


## Project Structure

```
slang_lang/
├── main.py              # Main entry point
├── interpreter.py       # Core interpreter logic
├── exceptions.py        # Exception classes
├── operations.py        # Operation mappings
├── state.py            # Global state management
├── handlers.py         # Command handlers
├── functions.py        # Function handling
├── utils.py            # Utility functions
└── README.md           # This file
```

## Usage

### Interactive Mode
Run the interpreter in interactive mode:
```bash
python main.py
```

### File Mode
Run a VarLang file:
```bash
python main.py your_file.vl
=======
Run a 6ix Esolang file:
```bash
python main.py your_file.six

```

## Module Descriptions

### main.py
- Entry point for the interpreter
- Handles command-line arguments
- Provides interactive mode
- Manages file execution

### interpreter.py
- Core interpreter logic
- Main execution loop
- Try-catch block handling
- Line-by-line execution

### exceptions.py
- `VarLangError` class for error handling
- Multiple error types: `VarLangMathError`, `VarLangVariableError`, `VarLangFunctionError`
- `throw_error()` function for error handling

### operations.py
- Operation mappings with lambda functions:
  - Math operations: `addy`, `chopped`, `hella`, `yute`, `nize`, `mans`, `two-twos`
  - Comparison operations: `word`, `fam`, `wallahi`, `reach`, `bussin`, `lick`
  - Logical operations: `based`, `ratio`, `mid`
  - Identity operations: `like`, `aint`

### state.py
- Global variables storage
- Global functions storage
- Error handlers storage

### handlers.py
- Command handlers for all 6ix Esolang operations:

  - Variable assignment (`croski`)
  - Print statements (`allow it`)
  - Comparisons (`real sh`)
  - Logical operations
  - Arithmetic operations
  - Error throwing (`waste`)

### functions.py
- Function definition handling (`mans ... takes ... does`)
- Function call handling (`ahlie`)
- Function body execution with return values (`send`)

### utils.py
- Value parsing functions
- Expression evaluation
- String interpolation support

## 6ix Esolang Syntax Examples

```varlang
# Variable assignment
croski x fax 10
croski y fax 20

# Print statements
allow it x
allow it "Hello World"

# Arithmetic operations
croski sum x addy y
allow it sum

croski product x hella y
allow it product

# Comparisons
real sh x wallahi y
real sh x bussin y

# Logical operations
real sh x based y
real sh mid x

# Functions
mans add_numbers takes a b does
    croski result a addy b
    send result
bet

# Function calls
ahlie add_numbers 5 15

# Try-catch blocks
trust
    croski z fax 0
    croski result x yute z
    allow it result
nah
    allow it "Caught error:"
    allow it error_message
    allow it error_type
safe

# Error throwing
waste "Something went wrong"
waste math "Division by zero"
```

## Error Handling
- `math`: Math operation errors 👨‍🔬
- `variable`: Variable-related errors ❓
- `function`: Function-related errors 🎊
- `generic`: General errors 🧬

## Slang Syntax Reference

### Variables
- `croski var_name fax value` - Basic assignment (`=`)
- `croski var_name money up value` - Add to existing variable (`+=`)
- `croski var_name funny up value` - Subtract from existing variable (`-=`)
- `croski var_name cheesed value` - Multiply with existing variable (`*=`)
- `croski var_name mandem value` - Divide existing variable (`/=`)
- `croski var_name steeze value` - Modulo with existing variable (`%=`)
- `croski var_name dun value` - Power with existing variable (`**=`)
- `croski var_name bucktee value` - Floor division with existing variable (`//=`)

### Math Operations
- `addy` - Addition
- `chopped` - Subtraction  
- `hella` - Multiplication
- `yute` - Division
- `nize` - Modulo
- `mans` - Power
- `two-twos` - Floor division

### Comparisons
- `word` - Equal to
- `fam` - Not equal to
- `wallahi` - Less than
- `reach` - Less than or equal to
- `bussin` - Greater than
- `lick` - Greater than or equal to

### Math Operations
- `addy` - Addition (`+`)
- `chopped` - Subtraction (`-`)
- `hella` - Multiplication (`*`)
- `yute` - Division (`/`)
- `nize` - Modulo (`%`)
- `mans` - Power (`**`)
- `two-twos` - Floor division (`//`)

### Comparisons
- `word` - Equal to (`==`)
- `fam` - Not equal to (`!=`)
- `wallahi` - Less than (`>`)
- `reach` - Less than or equal to (`>=`)
- `bussin` - Greater than (`<`)
- `lick` - Greater than or equal to (`<=`)

### Logical Operations
- `based` - AND
- `ratio` - OR
- `mid` - NOT

### Functions
- `mans func_name takes param1 param2 does` - Function definition
- `ahlie func_name arg1 arg2` - Function call
- `send value` - Return value from function

### Control Flow
- `trust ... nah ... safe` - Try-catch blocks
- `waste message` - Throw errors 
