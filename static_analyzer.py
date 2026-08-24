import subprocess
import sys
import json


def analyze_python(file_path):
    results = []

    # Bandit
    bandit = subprocess.run(
        [
            sys.executable,
            "-m",
            "bandit",
            "-f",
            "json",
            file_path
        ],
        capture_output=True,
        text=True
    )

    try:
        bandit_output = json.loads(bandit.stdout)
    except json.JSONDecodeError:
        bandit_output = {
            "errors": bandit.stderr,
            "results": []
        }

    results.append({
        "tool": "Bandit",
        "output": json.dumps(bandit_output, indent=2)
    })

    # Ruff
    ruff = subprocess.run(
        [
            sys.executable,
            "-m",
            "ruff",
            "check",
            file_path
        ],
        capture_output=True,
        text=True
    )

    results.append({
        "tool": "Ruff",
        "output": ruff.stdout or ruff.stderr
    })

    return results