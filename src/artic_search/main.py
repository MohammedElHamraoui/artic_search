"""
Main entry point for the Art Institute search CLI tool.
"""

import sys

from .client import search_artworks
from .display import display_results


def main():
    """
    The entry point of the application. Coordinates user input,
    data fetching, and presentation.
    """
    print("Search the Art Institute of Chicago")
    artist = input("Artist: ").strip()

    # Guard Clause: Input validation
    if not artist:
        print("Error: Artist name cannot be empty.", file=sys.stderr)
        sys.exit(1)

    # 1. Fetch the data
    artworks = search_artworks(artist)

    # 2. Display the data
    display_results(artworks, artist)


if __name__ == "__main__":
    main()
