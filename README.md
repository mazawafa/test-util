# test-util

Simple utility to test a program on predefined test cases. The task to be checked should be described in a JSON file in the following format:
```json
{
    "desc": "Strictly increasing array",
    "cases": [
        {
            "input": "5 1 3 5 6 9",
            "answer": "yes"
        },
        {
            "input": "5 1 2 3 3 4",
            "answer": "no"
        },
        {
            "input": "5 5 4 3 2 1",
            "answer": "no"
        },
        {
            "input": "1 42",
            "answer": "yes"
        },
        {
            "input": "2 1 2",
            "answer": "yes"
        }
    ]
}
```

## Installation

- Clone or download the repository.
- Ensure Python 3 is installed on your system.
- No additional dependencies are required.

## Running

```
python test.py path_to_program path_to_tests.json
```
