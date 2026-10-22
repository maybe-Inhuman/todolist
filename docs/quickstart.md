<div align="center">

# Quickstart

Get the ToDo list app running locally in under a minute.

</div>

## Prerequisites

- [Python](https://www.python.org/downloads/) 3.13
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- [Git](https://git-scm.com/)

> [!TIP]
> Don't have uv yet? Install it with:
> ```bash
> curl -LsSf https://astral.sh/uv/install.sh | sh
> ```

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/maybe-Inhuman/todolist.git
cd todolist
```

**2. Install dependencies**

```bash
uv sync
```

This creates a virtual environment in `.venv` and installs everything from `uv.lock`.

**3. Run the app**

```bash
uv run python -m main
```

You should see: `Hello from todolist!`
