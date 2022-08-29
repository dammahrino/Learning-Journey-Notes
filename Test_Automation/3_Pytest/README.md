# Pytest

Pytest does not require a directory named tests, but most Python projects use it.

Features:
- Test cases are written as functions.
- Naming conventions are important for pytest.
- Both the module and the function must contain `test_`
- When Pytest runs, it will discover tests from its current directory down.
- By default, any functions named **test_** in any modules named **test_**, will be identified and executed as Test Cases. *(this behavior can be overriden with pytest config files)*

To execute the test suite, position in the root folder of the project and run:

`python3 -m pytest`

You can run as well `pytest` alone, but with the previous command it will discover the modules contained in the project, which is why it's recommended to execute the longer version.

## Assertion introspection

When running test cases, if one of them fails, thanks for *assertion introspection* we can see what values our function
had at the moment it failed, as shown below:

```shell
________________ test_one_plus_two _________________

    def test_one_plus_two():
        a = 1
        b = 2
        c = 0
>       assert a + b == c
E       assert (1 + 2) == 0

tests/test_math.py:21: AssertionError
=========================================
```

If a test fails because an Assertion is not being satisfied, **although** it can also fail for any *unhandled* error.


## Verifying exception handling in pytest

Exceptions from one test case, will not affect other test cases.

Pytest provides a construct for handling expected exceptions.

For this to work, you need to import `pytest`

**with** is a special statement for automatically handling extra *enter* and *exit* logic for a caller.

The *enter* logic opens the files, the body reads or writes, and the *exit* logic closes the file.