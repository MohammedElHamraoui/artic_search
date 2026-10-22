"""
Art Institute of Chicago Search Tool
A CLI tool to search artworks by artist name.
"""

# 1. The DRY Versioning Trick
from importlib.metadata import PackageNotFoundError, version

try:
    # This reads the version directly from pyproject.toml!
    __version__ = version("artic-search")
except PackageNotFoundError:
    # Fallback if the package isn't installed yet
    __version__ = "unknown"

__author__ = "Mohammed El Hamraoui"

# 2. Import the public API
from .client import search_artworks
from .display import display_results

# 3. Define the public API (Note the double underscores!)
__all__ = ["display_results", "search_artworks"]
