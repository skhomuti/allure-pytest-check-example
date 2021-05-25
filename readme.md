
```bash
pip install -r requirements
pytest --alluredir allure-results --clean-alluredir test_foo.py
```

`allure-results` directory should contain two files with `*-result.json` mask.
Each file for every test.

Both tests have correct status - failed, 
but test with `pytest-check` hasn't `statusDetails` block with exception info
```json
  "statusDetails": {
    "message": "AssertionError: assert 1 == 2",
    "trace": "def test_simple():\n>       assert 1 == 2\nE       assert 1 == 2\n\ntest_foo.py:9: AssertionError"
  },
```