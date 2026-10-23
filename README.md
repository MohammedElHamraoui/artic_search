# Art Institute of Chicago Search Tool

A Python CLI tool to search artworks by artist name from the Art Institute of Chicago's public API.

## Features

-  Search artworks by artist name
-  Intelligent relevance filtering (Elasticsearch scoring)
- 🖼️ Clean, formatted output with artist info and dates
- 🛡️ Robust error handling and input validation
-  Fast, modern Python with strict type checking

## Installation

### Prerequisites
- Python 3.13+
- [uv](https://github.com/astral-sh/uv) (recommended) or pip

### Using uv (Recommended)
```bash
# Clone the repository
git clone https://github.com/MohammedElHamraoui/artic_search.git
cd artic_search

# Install dependencies
uv sync
```

### Using pip
```bash
pip install -e .
```

## Usage

### Run the CLI tool
```bash
# Using uv
uv run artic-search

# Or using the module directly
uv run python -m artic_search.main
```

### Example
```bash
$ uv run artic-search
Search the Art Institute of Chicago
Artist: Van Gogh

🎨 Found relevant result(s) for 'Van Gogh':

️🖼️ The Bedroom
   By: Vincent van Gogh (Dutch, 1853–1890)
   Date: 1889
   Score: 3454.84

🖼️ Self-Portrait
   By: Vincent van Gogh (Dutch, 1853–1890)
   Date: 1887
   Score: 3327.35
```

## Development

### Running Tests
This project uses pytest for testing. Run the test suite with:

```bash
# Run all tests
uv run pytest

# Run with verbose output
uv run pytest -v

# Run with coverage (if pytest-cov is installed)
uv run pytest --cov=artic_search
```

### Code Quality
The project enforces strict code quality standards:

```bash
# Format code with Ruff
uv run ruff format .

# Lint code with Ruff
uv run ruff check .

# Type checking with mypy
uv run mypy src tests

# Run all checks
uv run ruff check . && uv run mypy src tests && uv run pytest
```

### Pre-commit Hooks (Optional)
For automatic linting and formatting on commit, consider setting up pre-commit hooks.

## Package Structure

```
artic_search/
── pyproject.toml          # Project configuration and dependencies
├── README.md               # This file
├── uv.lock                 # Locked dependencies
├── src/
│   └── artic_search/
│       ├── __init__.py     # Package initialization and public API
│       ├── client.py       # API client for Art Institute API
│       ├── config.py       # Configuration and constants
│       ├── display.py      # Display and presentation logic
│       └── main.py         # CLI entry point
└── tests/
    ├── __init__.py
    ├── test_client.py      # Tests for API client
    ├── test_config.py      # Tests for configuration
    ├── test_display.py     # Tests for display logic
    └── test_main.py        # Tests for main entry point
```

## Configuration

### Environment Variables
None required. The tool uses default configuration values.

### Customization
Edit `src/artic_search/config.py` to customize:
- `API_URL`: Art Institute API endpoint
- `DEFAULT_LIMIT`: Number of results to return
- `MIN_RELEVANCE_SCORE`: Threshold for filtering irrelevant results

## API

The tool uses the [Art Institute of Chicago's public API](https://api.artic.edu/docs/).

### Rate Limiting
Anonymous users are limited to 60 requests per minute.

### Data Licensing
- Artwork descriptions: [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- All other data: [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests (`uv run pytest`)
5. Run linters (`uv run ruff check . && uv run mypy src tests`)
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## License

MIT License - see LICENSE file for details.

## Acknowledgments

- [Art Institute of Chicago](https://www.artic.edu/) for their excellent public API
- Built with [uv](https://github.com/astral-sh/uv) for fast, modern Python development
- Code quality enforced by [Ruff](https://github.com/astral-sh/ruff) and [mypy](https://mypy.readthedocs.io/)
