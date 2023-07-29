# Python API Automation Framework
## Integration test cases for restful booker

URL - https://restful-booker.herokuapp.com/apidoc/index.html

Verify HTTP methods like - GET, POST, PUT, PATCH, DELETE
Also need to validate the response, headers, status code
Authentication - Basic Auth and cookie based auth.
JSON Schema validation


## Tech Stack - What are the technology being used?
1. Request Module
2. Faker CSV,JSON, YAML
3. Pytest, Pytest-html
4. Allure Report
5. CommandLine Execution - Jenkins

P.S - DB Connection (In Future)

## Install pip packages
`pip install requests pytest pytest-html faker allure-pytest jsonschema`
- to check type pip list 
pip stands for python package manager
- To create a requirement text file type 
`pip freeze > requirement.txt`

## How to run locally and see the report
- `pytest test_scripts/* -s -v --alluredir=./reports --html=report.html`

### How to install xdist - `pip install pytest-xdist`

### How to run API test scripts in parallel - `pytest -n auto parallel `


## How to run via jenkins?

