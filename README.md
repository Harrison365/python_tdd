## Test-Driven Development in Python

This is a step-by-step guide to test-driven development (TDD) in python. From file set up to running tests.

Please find all of the steps that you need in the TDD.md file.

If you don't fancy following these tests and would like to get started straight away. Simply make your directory, cd into it and run the following command:

```shell
#!/bin/bash

# Step 1: Initialize Git repository
git init

# Step 2: Create virtual environment
python -m venv venv

# Step 3: Activate virtual environment
source venv/bin/activate

# Step 4: Install pytest
pip install pytest

# Step 5: Create .gitignore file
echo '**pycache**/' >> .gitignore
echo '*.py[cod]' >> .gitignore
echo 'build/' >> .gitignore
echo '.coverage' >> .gitignore
echo '.coverage.*' >> .gitignore
echo 'coverage.xml' >> .gitignore
echo '.pytest_cache/' >> .gitignore
echo 'venv/' >> .gitignore
echo '.vscode/' >> .gitignore

# Step 6: Create src and test folders
mkdir src test

# Step 7: Create function file in src folder
echo 'def func_name(x):' > src/func_name.py
echo '    return x + 1' >> src/func_name.py

# Step 8: Create test file in test folder
echo 'import pytest' > test/test_func_name.py
echo 'from src.func_name import func_name' >> test/test_func_name.py
echo '' >> test/test_func_name.py
echo 'def test_func_name():' >> test/test_func_name.py
echo '    assert func_name(0) == 1' >> test/test_func_name.py

# Step 9: Set PYTHONPATH environment variable
export PYTHONPATH=$(pwd)

# Step 10: Reminder to run pytest
echo "Setup complete. Run 'pytest' to execute tests."

```

All you need to do now is change your function and tests to suit your needs.

Enjoy!
