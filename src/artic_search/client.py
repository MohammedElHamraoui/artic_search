"""
API client for interacting with the Art Institute of Chicago API.
"""

import sys

import requests

from .config import API_URL, DEFAULT_LIMIT, FIELDS, HEADERS


def search_artworks(artist: str, limit: int = DEFAULT_LIMIT) -> list:
    """
    Fetches artworks from the Art Institute API based on the artist name.

    Args:
        artist: The artist name to search for
        limit: Maximum number of results to return (default: 3)

    Returns:
        A list of artwork dictionaries, or an empty list on failure.
    """
    params = {"q": artist, "limit": limit, "fields": FIELDS}

    # FIX: Added timeout=10 to prevent the script from hanging indefinitely
    response = requests.get(API_URL, params=params, headers=HEADERS, timeout=10)

    # Guard Clause: HTTP Errors
    if response.status_code != 200:
        print(
            f"Error: API request failed with status {response.status_code}.",
            file=sys.stderr,
        )
        return []

    return response.json().get("data", [])
