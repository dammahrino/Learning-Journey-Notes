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

## TODO List
- [ ] Review [Hypothesis](https://hypothesis.readthedocs.io/en/latest/) for property-based testing.

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

## Parametrized Test Cases

With `pytest.mark.parametrize` decorator, we enable parameterization of arguments for a test function.

For example, if we want to validate a function that multiplies two numbers, we could have many types of multiplication, as follows:
- Two positive integers
- Multiplying any number by 1
- Multiplying any number by 0
- Positive by a negative
- Negative by a negative
- Multiply floats

Instead of creating a `def` for each one of the scenarios, we can parametrize instead the function, with the following syntax:
```python
import pytest

@pytest.mark.parmetrize('number_1, number_2, product_result', array_with_vars)
def test_multiplication_parameterized(number_1, number_2, product_result):
    assert number_1 * number_2 == product_result

```

## Testing Classes

Unit tests: are small tests that directly cover functions and class methods, more generally, the cover _units_ of work.

Any directory with a file named `__init__.py` is treated as a package, and any modules inside that package may be imported by other modules.
> Dunder -> Colloquialism for __ (double underscore)

Pytest doest not require tests to be a package, in fact, making the tests directory a package, may cause unwanted behavior with some tools, like _tox_.

Private files are declared with a single leading underscore, like `_count`.

Properties can determine, how a class will _get_ and _set_ values (like in Java with _setters_ and _getters_). Python properties are defined with the `@property` decorator.

_AAA_ pattern, for functional test cases.
- **A**rrange (assets for the test, like a setup procedure)
- **A**ct (by exercising the target behavior)
- **A**ssert (that expected outcomes happen)

## Fixtures
With our previous configuration, in every test we have repeated the creation of the Accumulator object, which violates de DRY principle.

Pytest provides an useful feature for this, which are _fixtures_. 

Fixtures are special functions that pytest can call **before** test case functions. They are very useful when creating the **Arrange** steps, which are commonly shared among test cases.

> A fixture should **always** return a value.

### Fixture inner workings
1. When Pytest discovers a test function, it looks at the parameter list.
2. In our case, our function has the parameter _accum_, so it will look at a fixture named accum.
3. Pytest executes the fixture and passes the fixture return value to the function.

Note: This is a clever form of _dependency injection_.

This also severs as a "Separation of Concerns", which adds readability, consistency, and maintainability to our Test Case.

Function based way to handle setup and cleanup operations in Tests.

A test case can have multiple fixtures, just make sure each fixture has an unique name.

If a fixture instead of the `return` keyword, has the `yield` keyword, we get what is called a **generator**.

Generally speaking, everything before the `yield` statement will be the setup, and everything after it will be the cleanup.

The statement after `yield` will be executed after the test case finishes, either if it passed or not.

The scope of the fixture can be changed as well, the default scope is function, which mean that the fixture will run once for eaach function that needs it, however, if you change the scope to _session_, then the fixture then the fixture runs one time for the entire test suite, being executed in the first test that requires it.

Scope levels:
- class
- module
- package

Pytest provides several fixtures out of the box, for example:
- monkeypatch: Temporarily modify classes, functions, dictionaries, `os.environ`, and other objects.
- request: Provide information on the executing test function (test case metadata).
- tmpdir / tmp_path: Provides temporary directories.

### Advanced fixtures tricks
To reuse a fixture among several Test Cases, create a file in the Test Directory called `conftest.py`

## Pytest Commands and Configs
To get information about the commands, run `python -m pytest --help`.

Commands:
- --verbose, -v
  - Pytest prints more data about the Test Execution
  - At the top, prints _cachedir_ and _metadata_.
  - Also print a single line for each TC execution, giving its `path::name::PASSED/FAIL`
  - Failure instrospection for analysis.

- --quiet, -q 
  - Pytest doesn't print the top matter or even the Test Modules, and the Test failures.
  - Good when you want to avoid polluting your console with too many lines.

- --exitfirst, -x
  - Exits the Test Execution on the first Test Case that fails.

- --maxfail=number
  - Specifies after how many failures the execution should stop.

- --junit-xml report_file_path

Configuration:
- Supports multiple configuration files:
  - pytest.ini
  - pyproject.toml
  - setup.cfg

- Configurations should be loaded in the projects' root directory.
- Configuration options:
  - addopts
    - Allows you to set configurations directly, as if they would be entered on the command line.

## Filtering Tests

We can run Tests in a specific directory, adding the folder at the end of the command as follows:

`python3 -m pytest folder_name`

By default, if no folder argument is provided, PyTest will run all the Test Cases.

Similarly, we can run a specific Test File, providing the route in the command line as follows:

`python3 -m pytest folder_name/test_file.py`

Finally, to run specifically a single Test Case, we're able to declare it with double colon after the test file:

`python3 -m pytest folder_name/test_file.py::test_name`

If you don't know the name of a test, or you just want to run every test that has a specific keyword, they can be run with the following command:

`python3 -m pytest -k keyword`

The `-k` flag, also supports boolean logic with _and_, _or_, and _not_ keywords.

For example:

`python3 -m pytest -k "one and not accum"`,

will run the tests that contain the keyword **one**, but not those ones that match the word **accum**.

Sometimes, using the `-k` flag might lead to false positives. To avoid this, we have another option to filter test cases, and this is with **markers**.

>**Markers**: They're basically tags for test cases.

To add a marker, above the test function, add the following decorator

`@pytest.mark.marker_name`

For example, if we want to add the *math* marker to a test, we would do as follows:

```python
@pytest.mark.math
def test_one_plus_one():
  # Test logic

```

And we also need to add them in the python configuration file.

```ini
[pytest]
markers = 
  math
```

Finally, to run the test cases with specific markers, run the following command:

`python -m pytest -m marker_tag`

The markers can also be used along with the *boolean* operators. Below there's a small list of commonly used markers:

- **skip**: always skip a test function
- **skipif**: skip a test function if a certain condition is met
- **xfail**: produce an "expected failure" outcome if a certain condition is met
- **parametrize**: to perform multiple calls to the same test function

More information about this in: [PyTest Markers](https://docs.pytest.org/en/stable/how-to/mark.html)

Pytest will look for Test Cases either in the current directory or from the paths and options given at the command line. But another test paths can be set through the configuration file.

```ini
[pytest]
testpaths = 
  testing
  docs
```

## Feature Tests

There's a difference between testing **code** and testing **features**.

White Box tests, are sometimes called Unit Tests, which is what we've doing so far. This type of tests, test *code* directly. 

> Is the code written to do expected things?

Black Box tests, are commonly called feature tests, integration tests, system tests or end-to-end tests. In this case, these kind of tests interact with a live instance of the product.

> Does the product meet the requirements?

Feature tests require an extra setup, since they require an instance which is either a deployed service, a web app, or something else.

Integration tests are prone to errors due to their dependencies on systems under test and feature tests are *slower* than unit tests, because they need to wait for the product under test to respond.