# Cookiecutter development template

Small (opinionated) template for development projects with Python 3.12.

## Usage

You need to have  [`uv`](https://docs.astral.sh/uv/), `cookiecutter` and 
`pre-commit` pre-installed.

Afterwards, simply run:

```bash
cookiecutter https://github.com/JakobKlotz/dev-template.git
```

... which walks you through the set-up of your project. After the project
structure creation, the virtual environment and pre-commit hooks are
automatically installed.

Uses:

- `uv` for package management
- `pre-commit` and `ruff` to formate and lint the code