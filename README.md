# Art Institute of Chicago Search Tool

A Python CLI tool to search artworks by artist name from the Art Institute of Chicago's public API.

## Installation

```bash
uv sync
```

## Usage

Run the search tool using uv:

```bash
uv run artic-search
```

Or run it as a module:

```bash
uv run python -m artic_search.main
```

## Features

- Search artworks by artist name
- Intelligent relevance filtering
- Clean, formatted output
- Robust error handling

## Package Structure

```text
artic_search/
├── pyproject.toml
├── README.md
└── src
    └── artic_search
        ├── __init__.py
        ├── client.py
        ├── config.py
        ├── display.py
        └── main.py
```

## License

MIT

---

### 🚀 How to Run It with `uv`

Now that the files are fixed, here is the exact workflow you should use in your terminal:

**1. Install the dependencies (this reads `pyproject.toml` and installs `requests`):**
```bash
cd artic_search
uv sync
```

**2. Run your CLI tool:**
```bash
uv run artic-search
```
*(This uses the entry point we defined in `pyproject.toml`)*

**3. Or run it as a module:**
```bash
uv run python -m artic_search.main
```
