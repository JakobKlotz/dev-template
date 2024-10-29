import subprocess
from pathlib import Path

use_git = "{{ cookiecutter.git_init }}"

if use_git == "y":
    subprocess.run(["git", "init"])
    subprocess.run(["pre-commit", "autoupdate"])
    subprocess.run(["pre-commit", "install-hooks"])
else:
    Path(".pre-commit-config.yaml").unlink()

subprocess.run(["uv", "sync"])
