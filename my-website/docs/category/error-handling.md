---
sidebar_position: 4
---

# Error Handling

Try/Catch handling to catch all my opps on Jane n' Finch 🐱‍👤

```slang
trust
    # code that might throw
nah
    # code to run if an error occurs
safe
```

## Example

```slang
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
```

- `trust` starts the try block.
- `nah` starts the catch block.
- `safe` ends the error handling block.
- `error_message` and `error_type` are available in the catch block.

Also the above example will print the following:
```slang
"Caught error:"
Division by zero, fam!
math
```
`trust > x = 10 > y = 0 > result = x/y`
Since `10/0` is a Division by zero error

You can also throw custom errors:

```slang
waste "Something went wrong!"
waste math "Division by zero"
```

- `waste <message>` throws a generic error.
- `waste <type> <message>` throws a typed error (`math`, `variable`, etc).
