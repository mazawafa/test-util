import subprocess
import sys
import os
import json

# constants
PATH_TO_PROGRAM = 1
PATH_TO_TESTS = 2

# colors
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"

def color(s, c):
    return f"{c}{s}{RESET}"

def load_task(filename):
    with open(filename, "r", encoding="utf8") as f:
        return json.load(f)

def run_program(prog, input_data):
    try:
        result = subprocess.run(
            [prog],
            input=input_data.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=3
        )
        return result.stdout.decode().strip()
    except FileNotFoundError:
        return "ERROR: program not found"
    except Exception as e:
        return f"ERROR: {str(e)}"

if len(sys.argv) < 3:
    print(f"Usage: python test.py program tests")
    sys.exit(1)

# load tasks
tests = sys.argv[PATH_TO_TESTS]
if not os.path.exists(tests):
    print("ERROR: tests not found:", tests)
    sys.exit(1)
task = load_task(tests)

# open program
program = sys.argv[PATH_TO_PROGRAM]
if not os.path.exists(program):
    print("ERROR: program not found:", program)
    sys.exit(1)

# print section
print("=" * 60)
print(task["desc"])
print("=" * 60)

for idx, case in enumerate(task["cases"], start=1):
    out = run_program(program, case["input"])
    # ignore case differences
    ok = (out.lower().strip() == case["answer"].lower().strip())
    print()
    if ok:
        print(color(f"Case {idx}: OK", GREEN))
    if not ok:
        break

if ok:
    print(color("\nAccepted", GREEN))
if not ok:
    print(color(f"Case {idx}: FAIL", RED))
    print(color("Input:", BOLD))
    print(case["input"])
    print(color("Output:", BOLD))
    print(out)
    print(color("Answer:", BOLD))
    print(case["answer"])
