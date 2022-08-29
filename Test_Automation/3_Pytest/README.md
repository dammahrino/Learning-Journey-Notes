# Learning Pytest

Pytest does not require a directory named tests, but most Python projects use it.

Features:
- Test cases are written as functions.
- Naming conventions are important for pytest.
- Both the module and the function must contain `test_`
- When Pytest runs, it will discover tests from its current directory down.
- By default, any functions named **test_** in any modules named **test_**, will be identified and executed as Test Cases. *(this behavior can be overriden with pytest config files)*