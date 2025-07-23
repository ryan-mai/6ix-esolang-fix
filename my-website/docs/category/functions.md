---
sidebar_position: 3
---

# Functions

Defining and using functions to get invited to Drake's party 👯‍♂️

## Defining a Function

To define a function in 6ix Esolang, use this syntax:

```
mans <function_name> takes <param1> <param2> ... does
    # function body
    send <value>   # (optional) return value
bet
```

- `mans` starts the function definition.
- `<function_name>` is the name of your function.
- `takes` is followed by a list of parameter names.
- `does` marks the start of the function body.
- `send <value>` returns a value from the function (optional).
- `bet` ends the function definition.

**Example:**

```
mans add takes x y does
    croski result x addy y
    send result
bet
```

## Calling a Function

To call a function, use the `ahlie` keyword:

```
ahlie <function_name> <arg1> <arg2> ...
```

**Example:**

```plaintext
ahlie add 5 7
```

This will output `12`.

## Assigning Function Results to Variables

You can assign the result of a function call to a variable:

```
croski <var_name> ahlie <function_name> <arg1> <arg2> ...
```

**Example:**

```plaintext
croski sum ahlie add 10 20
allow it sum
```

This will output `30`.

## Returning Values

Use `send <value>` inside a function to return a value. If `send` is omitted, the function returns nothing.

## Examples

#### *6ix Esolang*
```plaintext
mans greet takes name does
    croski greeting eh"Hello, {name}"
    send greeting
bet

ahlie greet "World"
```
---
#### *Python*

```py
def greet (name):
    print(f'Hello {name}')
    return
bet

ahlie greet "World"
```

This will output `Hello, World`. <br /><br />

#### *6ix Esolang*
```plaintext
mans greet takes name does
    croski greeting eh"Hello, {name}"
    send greeting
bet

ahlie greet "World"
```
---
#### *Python*

```py
def greet (name):
    print(f'Hello {name}')
    return
bet

ahlie greet "World"
```

This will output `Hello, World`.


## Notes

- Functions can access and modify variables.
- Arguments are passed by value.
- You can use math and string operations inside functions.

For more details, see the [interpreter source code](../../../interpreter.py).