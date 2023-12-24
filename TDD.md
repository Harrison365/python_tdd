1. git init

2. Create a virtual environment using the following command:

```shell
python -m venv venv
```

3. Activate the virtual environment using the following command:

```shell
source venv/bin/activate
```

4. Install pytest using the following command:

```shell
pip install pytest
```

5. create a .gitignore file and add the following:

```
**pycache**/
\*.py[cod]

build/
.coverage
.coverage.\*
coverage.xml
.pytest_cache/

venv/

.vscode/
```

6. Create an src folder and a test folder

7. Put your code file (e.g. func_name.py) in the src folder and your test file (e.g. test_func_name.py) in the test folder. The test file should be named with the prefix "test\_".

8. Create your first test in the following format:

```

import src.func_name
#exporting from the function file is not necessary
import pytest
#(if needed)

def test_a_description_for_the_test():
expected = 1
result = func_name(0)
assert expected == result #assert is built into python

```

9. Set the PYTHONPATH environment variable (so that pytest knows where the function lives) using the following command:

```
export PYTHONPATH=${pwd}
```

10. Run pytest using the following command:

```
pytest test/test_func_name.py
```

Running pytest alone will run all the tests in the test file.

11. Build your funtion and test file using TDD

12. Note: Importing pytest gives us access to the ability to test for errors using the following format:

```
def test_say_hello_raises_type_error():
    with pytest.raises(TypeError):
        say_hello(1)

```
