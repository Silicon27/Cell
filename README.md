# Cell Programming Language

### Basics
Cell, alike all other languages, has a **global scope**. However, unlike other languages, the global scope is refered as the "*root*", by which all other nested scopes within the root can access **root variables**. 

The root can be defined by creating a parenthesis around the whole file:
```lisp
(
    (print["Hello, World!"])
)
```
> `Hello, World!`

Creating a variable with the `root` keyword would make it accessible everywhere:
```lisp
(
    (root var myvar:int = 123)
    (print[myvar])
)
```
> `123`

Another crucial part to Cell is that every statement has its own scope.

Consider the following:
```lisp
(
    (print["hello"])
)
```
> `hello`

In that case, Cell would consider a scoped structure somewhat of the following:
```py
{
    "root": {
        "within": "(print['hello'])"
        "nested": {"scope1": {
            "within": "print['hello']"
            "nested": ""
        }
        }
    }

}
```
Every previous scope's user-defined values (i.e., variables, functions, etc) are accessible to the scopes nested within.

 Meaning, when defining a variable from root without the `root` keyword, other scopes in the root are not able to access it as the variable is defined in its own scope:
 ```lisp
(
    (var myvar:int = 123)
    (print[myvar])
)
```
> `Definable 'myvar' is undefined.`
