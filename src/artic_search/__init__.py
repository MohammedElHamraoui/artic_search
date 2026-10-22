"""
Art Institute of Chicago Search Tool
A CLI tool to search artworks by artist name.
"""

__version__ = "1.0.0"
__author__ = "Mohammed El Hamraoui"

from .client import search_artworks
from .display import display_results

__all__ = ["display_results", "search_artworks"]
